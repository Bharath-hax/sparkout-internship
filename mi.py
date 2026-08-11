from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 1. A basic GET endpoint
@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "query": q}

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None

@app.post("/items/")
def create_item(item: Item):
    return {
        "message": "Item created successfully",
        "item_name": item.name,
        "item_price": item.price
    }