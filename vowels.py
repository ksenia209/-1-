def count_vowels(text):
    """Считает количество гласных букв в строке"""
    vowels = "аеёиоуыэюяaeiou"
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count

import pytest
from vowels import count_vowels


@pytest.mark.parametrize("text,expected", [
    ("", 0),                  
    ("hello", 2),             
    ("HELLO", 2),             
    ("привет", 2),             
    ("ПРИВЕТ", 2),             
    ("аеёиоуыэюя", 10),        
    ("aeiou", 5),               
    ("бвгджзйклмнпрстфхцчшщ", 0),  
    ("Hello, мир!", 3),        
    ("Эй, как дела?", 5),       
    ("12345", 0),           
    ("@#$%", 0),               
    ("аАеЕёЁиИоОуУыЫэЭюЮяЯ", 20), 
])
def test_count_vowels(text, expected):
    """Параметризованный тест для подсчета гласных"""
    assert count_vowels(text) == expected


def test_count_vowels_mixed_case():
    """Дополнительный тест со смешанным регистром"""
    assert count_vowels("Hello World") == 3
    assert count_vowels("Программирование") == 6
