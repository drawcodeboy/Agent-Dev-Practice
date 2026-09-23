from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello FastAPI"}

@app.get("/health")
def health():
    return {"status": "ok"}

class User(BaseModel):
    name: str
    age: int

@app.post("/users")
def create_users(user: User):
    return {
        "message": f"{user.name} 님이 등록되었습니다.",
        "age": user.age
    }