from fastapi import APIRouter, File, UploadFile
from app.utils.embeddings import generate_embedding
from app.utils.redis_client import redis_client

router = APIRouter()

@router.post("/")
async def upload_document(file: UploadFile = File(...)):
    content = await file.read()
    text = content.decode("utf-8").strip()
    embedding = generate_embedding(text)

    redis_client.hset(file.filename, mapping={"content": text, "embedding": embedding})
    return {"message": "Document uploaded successfully"}
