"""Здесь надо написать тесты с использованием pytest для модуля phone."""
import pytest

from src.item import Item
from src.phone import Phone


def test_phone():
    phone1 = Phone("iPhone 14", 120000, 5, 2)
    assert phone1.name == "iPhone 14"
    assert phone1.price == 120000
    assert phone1.quantity == 5
    assert phone1.number_of_sim == 2


@pytest.fixture
def phone1():
    """Создаем экземпляр класса в фикстуре"""
    return Phone("iPhone 14", 120_000, 5, 2)


def test_str(phone1):
    """Тест для __str__"""
    assert str(phone1) == 'iPhone 14'


def test_repr(phone1):
    """Тест для __repr__"""
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_add(phone1):
    """Тест для __add__"""
    phone1 = Phone("iPhone 14", 120000, 5, 2)
    item1 = Item("Смартфон", 10000, 20)
    assert item1.quantity + phone1.quantity == 25
    assert item1.price + phone1.price == 130000
    assert phone1.quantity + phone1.quantity == 10


def chek_number_of_sim():
    phone1 = Phone("iPhone 14", 120000, 5, 2)
    assert phone1.chek_number_of_sim == 0
    # ValueError: Количество физических SIM-карт должно быть целым числом больше нуля.
