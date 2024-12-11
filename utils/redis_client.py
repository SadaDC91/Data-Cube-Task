import redis

redis_client = redis.Redis(host="localhost", port=6379, decode_responses=False)

def create_index(index_name: str, dimension: int):
    redis_client.ft(index_name).create_index([
        redis.VectorField("embedding", "FLOAT32", dimension=dimension, algorithm="HNSW")
    ])
