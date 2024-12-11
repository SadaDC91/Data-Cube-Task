from fastapi import APIRouter
from app.utils.embeddings import generate_embedding
from app.utils.redis_client import redis_client

router = APIRouter()

@router.post("/")
async def search_document(query: str):
    query_vector = generate_embedding(query)
    results = redis_client.ft("index_name").search(
        f"*=>[KNN 3 @embedding $vec]",
        query_params={"vec": query_vector}
    )

    return {"matches": [{"document": r.content, "score": r.score} for r in results]}
