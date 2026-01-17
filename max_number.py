import pytest
from max_number import find_max


def test_find_max_positive():
    """Тест с положительными числами"""
    assert find_max([1, 2, 3, 4, 5]) == 5
    assert find_max([10, 20, 30]) == 30
    assert find_max([100, 200, 150]) == 200


def test_find_max_negative():
    """Тест с отрицательными числами"""
    assert find_max([-5, -1, -10]) == -1
    assert find_max([-100, -50, -200]) == -50


def test_find_max_mixed():
    """Тест со смешанными числами"""
    assert find_max([-10, 0, 10]) == 10
    assert find_max([-5, 5, 0]) == 5


def test_find_max_single():
    """Тест с одним элементом"""
    assert find_max([42]) == 42
    assert find_max([-7]) == -7


def test_find_max_empty():
    """Тест с пустым списком"""
    assert find_max([]) is None


def test_find_max_duplicates():
    """Тест с дубликатами"""
    assert find_max([5, 5, 5]) == 5
    assert find_max([1, 2, 2, 1]) == 2
