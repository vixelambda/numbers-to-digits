import pytest
from main import words_to_digits, file_reader

def test1():
    # Тест на обработку пустой строки
    assert words_to_digits("") == ""

def test2():
    # Тест на обработку строки
    assert words_to_digits("триста двадцать пять тысяч сто девять птиц съели семнадцать тысяч двести шесть яблок") == "325 109 птиц съели 17 206 яблок"

def test3():
    # Тест на обработку файла
    assert file_reader("input.txt") == "325 109 птиц съели 17 206 яблок"

def test4():
    # Тест на обработку строки
    assert words_to_digits("сто пятнадцать городов") == "115 городов"

pytest.main()