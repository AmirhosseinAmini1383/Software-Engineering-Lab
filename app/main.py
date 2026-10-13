"""MiniOrder API. Visit /docs after starting the server."""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from app.catalog import PRODUCTS, find_product
from app.orders import ORDERS, create_order

app = FastAPI(title="MiniOrder", version="0.1.0")


class OrderRequest(BaseModel):
    product_id: int
    quantity: int = Field(ge=1)


@app.get("/")
def home():
    return {"message": "MiniOrder is running", "docs": "/docs"}


@app.get("/products")
def list_products():
    return PRODUCTS


@app.get("/products/{product_id}")
def get_product(product_id: int):
    product = find_product(product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@app.post("/orders", status_code=201)
def add_order(order: OrderRequest):
    try:
        return create_order(order.product_id, order.quantity)
    except ValueError as error:
        message = str(error)
        status = 404 if message == "Product not found" else 400
        raise HTTPException(status_code=status, detail=message) from error


@app.get("/orders")
def list_orders():
    return ORDERS
