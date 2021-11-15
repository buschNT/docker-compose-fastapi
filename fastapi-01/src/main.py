import uvicorn
from fastapi import FastAPI


app = FastAPI(
    title="FastAPI",
    description="Setup.",
    version="0.0.0",
)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
