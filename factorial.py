def factorial(n):
    """Вычисляет факториал числа"""
    if n < 0:
        raise ValueError("Факториал определен только для неотрицательных чисел")
    if n == 0:
        return 1
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

import pytest
from factorial import factorial


@pytest.mark.parametrize("n,expected", [
    (0, 1),      
    (1, 1),      
    (2, 2),     
    (3, 6),    
    (4, 24),     
    (5, 120),    
    (6, 720),    
    (7, 5040),  
])
def test_factorial_positive(n, expected):
    """Параметризованный тест для положительных чисел"""
    assert factorial(n) == expected


def test_factorial_negative():
    """Тест для отрицательного числа (должно быть исключение)"""
    with pytest.raises(ValueError, match="Факториал определен только для неотрицательных чисел"):
        factorial(-1)
    
    with pytest.raises(ValueError, match="Факториал определен только для неотрицательных чисел"):
        factorial(-5)


def test_factorial_large():
    """Тест для относительно большого числа"""
    assert factorial(10) == 3628800
