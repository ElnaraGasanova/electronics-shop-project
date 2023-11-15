"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_item():
    item1 = Item("Samsung", 15000, 10)
    assert item1.name == "Samsung"
    assert item1.price == 15000
    assert item1.quantity == 10
    assert item1.calculate_total_price() == 150000
    Item.pay_rate = 0.5
    item1.apply_discount()
    assert item1.price == 7500
