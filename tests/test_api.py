"""Automated tests for use during the testing and CI sessions."""

import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.orders import ORDERS

client = TestClient(app)


@pytest.fixture(autouse=True)
def reset_orders():
    ORDERS.clear()
    yield
    ORDERS.clear()


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["docs"] == "/docs"


def test_products():
    response = client.get("/products")
    assert response.status_code == 200
    assert len(response.json()) == 3


def test_create_order():
    response = client.post("/orders", json={"product_id": 1, "quantity": 2})
    assert response.status_code == 201
    assert response.json()["total_price"] == 100000
    assert len(client.get("/orders").json()) == 1


def test_invalid_quantity():
    response = client.post("/orders", json={"product_id": 1, "quantity": 0})
    assert response.status_code == 422


def test_insufficient_stock():
    response = client.post("/orders", json={"product_id": 3, "quantity": 6})
    assert response.status_code == 400
