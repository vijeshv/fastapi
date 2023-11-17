
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
        return {"Hello vijeshamabiar november 16 th 2024": "World 2004"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
        return {"item_id": item_id, "q": q}
