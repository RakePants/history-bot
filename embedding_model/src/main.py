from typing import Annotated, List

from fastapi import Body, FastAPI, status
from fastapi.responses import JSONResponse

from src.utils.embedder import embed

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello from embedder model!"}


@app.post("/embed", status_code=status.HTTP_200_OK)
def embed_route(text: Annotated[str, Body()]) -> List:
    result = embed(text)

    return list(result)
