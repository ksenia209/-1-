import pytest
from even_odd import is_even


def test_even_numbers():
    """Тест четных чисел"""
    assert is_even(0) == True
    assert is_even(2) == True
    assert is_even(10) == True
    assert is_even(-4) == True


def test_odd_numbers():
    """Тест нечетных чисел"""
    assert is_even(1) == False
    assert is_even(7) == False
    assert is_even(-3) == False


def test_large_numbers():
    """Тест больших чисел"""
    assert is_even(1000) == True
    assert is_even(1001) == False
