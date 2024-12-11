from fastapi import FastAPI
from app.routers import upload, search

app = FastAPI()

app.include_router(upload.router, prefix="/upload", tags=["Upload"])
app.include_router(search.router, prefix="/search", tags=["Search"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
