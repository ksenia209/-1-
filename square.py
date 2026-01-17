def square(x):
    """Возвращает квадрат числа"""
    return x * x

import pytest
from square import square


@pytest.mark.parametrize("input_value,expected", [
    (0, 0),         
    (1, 1),          
    (2, 4),         
    (5, 25),        
    (-3, 9),       
    (-10, 100),    
    (2.5, 6.25),    
    (-1.5, 2.25),   
])
def test_square(input_value, expected):
    """Параметризованный тест для функции square"""
    assert square(input_value) == expected


def test_square_large_number():
    """Тест с большим числом"""
    assert square(100) == 10000
