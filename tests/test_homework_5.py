# Выполняю подключение встроенных модулей, чтобы тесты смогли найти файл с кодом
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Выполняю импорт библиотеки для тестов и саму функцию из рабочего файла
import pytest
from homework_5 import plot_functions

# Проверяю, что программа выдаст ошибку если шаг отрицательный
def test_negative_step():
    with pytest.raises(ValueError, match="Шаг должен быть положительным"):
        plot_functions(-3, 3, -1)

# Проверяю, что программа выдаст ошибку если шаг равен нулю
def test_zero_step():
    with pytest.raises(ValueError, match="Шаг должен быть положительным"):
        plot_functions(-3, 3, 0)

# Проверяю, что программа выдаст ошибку если начало больше конца
def test_start_bigger_than_end():
    with pytest.raises(ValueError, match="Начало диапазона не может быть больше или равно концу"):
        plot_functions(5, 3, 1)