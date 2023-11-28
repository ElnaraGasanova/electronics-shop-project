"""Здесь надо написать тесты с использованием pytest для модуля keyboard."""
import pytest
from src.keyboard import Keyboard


def test_keyboard():
    '''Тестирование объекта класса'''
    kb = Keyboard('Dark Project KD87A', 9600, 5, "EN")
    assert str(kb) == "Dark Project KD87A"
    assert str(kb.language) == "EN"
    assert kb.price == 9600
    assert kb.quantity == 5
    kb.change_lang()
    '''Тестирование смены раскладки клавиатуры'''
    assert str(kb.language) == "RU"
