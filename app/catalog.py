"""The initial sample product catalog (simple enough to read in class)."""

PRODUCTS = [
    {"id": 1, "name": "Notebook", "price": 50000, "stock": 10},
    {"id": 2, "name": "Pencil", "price": 10000, "stock": 20},
    {"id": 3, "name": "Backpack", "price": 400000, "stock": 5},
]


def find_product(product_id: int):
    return next((product for product in PRODUCTS if product["id"] == product_id), None)
