import pytest
from greeting import greet


def test_greeting_english():
    """Тест с английскими именами"""
    assert greet("Alice") == "Привет, Alice!"
    assert greet("Bob") == "Привет, Bob!"
    assert greet("John") == "Привет, John!"


def test_greeting_russian():
    """Тест с русскими именами"""
    assert greet("Анна") == "Привет, Анна!"
    assert greet("Иван") == "Привет, Иван!"
    assert greet("Мария") == "Привет, Мария!"


def test_greeting_empty():
    """Тест с пустым именем"""
    assert greet("") == "Привет, !"


def test_greeting_special_chars():
    """Тест со специальными символами"""
    assert greet("John Doe") == "Привет, John Doe!"
    assert greet("Иван-Царевич") == "Привет, Иван-Царевич!"
