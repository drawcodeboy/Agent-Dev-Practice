from io import BytesIO

import torch
from torchvision.models import MobileNet_V3_Small_Weights, mobilenet_v3_small

from PIL import Image, UnidentifiedImageError

from fastapi import FastAPI, File, UploadFile

app = FastAPI()

weights = MobileNet_V3_Small_Weights.DEFAULT
model = mobilenet_v3_small(weights=weights)
model.eval()

preprocess = weights.transforms()
categories = weights.meta['categories']

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        image_bytes = await file.read()
        image = Image.open(BytesIO(image_bytes)).convert('RGB')
    except (UnidentifiedImageError, OSError):
        raise HTTPException(status_code=400, detail="유효한 이미지가 아님")

    input_tensor = preprocess(image).unsqueeze(0)
    print(input_tensor.shape)

    with torch.inference_mode():
        logits = model(input_tensor)
        probs = torch.softmax(logits, dim=1)
        confidence, class_id = probs.max(dim=1)

    return {
        "class_id": class_id.item(),
        "label": categories[class_id.item()],
        "confidence": round(confidence.item(), 4)
    }