from io import BytesIO

import torch
from torchvision.models import MobileNet_V3_Small_Weights, mobilenet_v3_small
from PIL import Image, UnidentifiedImageError
from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel

import logging, time
from fastapi import Request

app = FastAPI()
logger = logging.getLogger("uvicorn.error")

weights = MobileNet_V3_Small_Weights.DEFAULT
model = mobilenet_v3_small(weights=weights)
model.eval()

preprocess = weights.transforms()
categories = weights.meta['categories']

class PredictionResponse(BaseModel):
    class_id: int
    label: str
    confidence: float

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start = time.perf_counter()
    status_code = 500

    try:
        response = await call_next(request)
        status_code = response.status_code
        return response
    except Exception:
        logger.exception("요청 처리 중 오류 발생")
    finally: 
        elapsed_ms = (time.perf_counter() - start) * 1000
        logger.info(
            "%s %s status=%d latency=%.2fms",
            request.method,
            request.url.path,
            status_code,
            elapsed_ms
        )

@app.post("/predict")
async def predict(file: UploadFile = File(...), response_model=PredictionResponse):
    try:
        image_bytes = await file.read()
        image = Image.open(BytesIO(image_bytes)).convert('RGB')
    except (UnidentifiedImageError, OSError):
        raise HTTPException(status_code=400, detail="유효한 이미지가 아님")

    input_tensor = preprocess(image).unsqueeze(0)

    with torch.inference_mode():
        logits = model(input_tensor)
        probs = torch.softmax(logits, dim=1)
        confidence, class_id = probs.max(dim=1)

    return PredictionResponse(
        class_id = class_id.item(),
        label = categories[class_id.item()],
        confidence = round(confidence.item(), 4)
    )