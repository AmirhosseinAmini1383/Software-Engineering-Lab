"""Toy order logic. Not concurrent-safe and not a persistent database."""

from app.catalog import find_product

ORDERS = []


def create_order(product_id: int, quantity: int):
    product = find_product(product_id)
    if product is None:
        raise ValueError("Product not found")
    if quantity > product["stock"]:
        raise ValueError("Not enough stock")

    order = {
        "id": len(ORDERS) + 1,
        "product_id": product_id,
        "quantity": quantity,
        "total_price": product["price"] * quantity,
        "status": "created",
    }
    ORDERS.append(order)
    return order
