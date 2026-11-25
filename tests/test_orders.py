from app.orders import can_place_order

def test_enough_stock():
    # Arrange
    stock = 3
    quantity = 3

    # Act
    result = can_place_order(stock, quantity)

    # Assert
    assert result is True