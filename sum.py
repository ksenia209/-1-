import pytest
from sum import add


def test_add_positive_numbers():
    """Тест сложения положительных чисел"""
    assert add(2, 3) == 5
    assert add(10, 20) == 30


def test_add_negative_numbers():
    """Тест сложения отрицательных чисел"""
    assert add(-2, -3) == -5
    assert add(-10, 5) == -5


def test_add_zero():
    """Тест сложения с нулем"""
    assert add(0, 0) == 0
    assert add(5, 0) == 5
    assert add(0, -3) == -3


def test_add_floats():
    """Тест сложения дробных чисел"""
    assert add(2.5, 3.5) == 6.0
    assert add(-1.5, 1.5) == 0.0
