def convert_rub_to_usd(rubles, rate=0.011):
    """Конвертирует рубли в доллары"""
    if rubles < 0:
        raise ValueError("Сумма не может быть отрицательной")
    return rubles * rate

import pytest
from currency import convert_rub_to_usd


@pytest.mark.parametrize("rubles,expected", [
    (0, 0.0),          
    (100, 1.1),         
    (500, 5.5),        
    (1000, 11.0),       
    (273.5, 3.0085),   
])
def test_convert_rub_to_usd_default_rate(rubles, expected):
    """Параметризованный тест с курсом по умолчанию"""
    assert convert_rub_to_usd(rubles) == pytest.approx(expected, 0.001)


@pytest.mark.parametrize("rubles,rate,expected", [
    (100, 0.01, 1.0),       
    (100, 0.015, 1.5),     
    (500, 0.02, 10.0),     
    (1000, 0.008, 8.0),   
    (250, 0.0115, 2.875),  
def test_convert_rub_to_usd_custom_rate(rubles, rate, expected):
    """Параметризованный тест с кастомным курсом"""
    assert convert_rub_to_usd(rubles, rate) == pytest.approx(expected, 0.001)


def test_convert_rub_to_usd_negative():
    """Тест для отрицательной суммы (должно быть исключение)"""
    with pytest.raises(ValueError, match="Сумма не может быть отрицательной"):
        convert_rub_to_usd(-100)
    
    with pytest.raises(ValueError, match="Сумма не может быть отрицательной"):
        convert_rub_to_usd(-1)


def test_convert_rub_to_usd_large_amount():
    """Тест для большой суммы"""
    assert convert_rub_to_usd(1_000_000, 0.011) == 11000.0


def test_convert_rub_to_usd_precision():
    """Тест на точность вычислений"""
    result = convert_rub_to_usd(100, 0.011111)
    expected = 1.1111
    assert result == pytest.approx(expected, 0.0001)
