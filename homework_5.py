# Выполняю импорт библиотек
import numpy as np
import matplotlib.pyplot as plt
import logging

# Настраиваю вывод логов
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

# Создаю функцию для ввода и проверки данных
def get_user_input():
    try:
        # Запрашиваю ввод значений с клавиатуры, при отсутствии - значение по умолчанию
        start = float(input("Введите начало диапазона (по умолчанию -3) ") or -3)
        end = float(input("Введите конец диапазона (по умолчанию 3) ") or 3)
        step = float(input("Введите шаг (по умолчанию 0.5) ") or 0.5)
            
        return start, end, step
        
    except ValueError as e:
        # Если введен текст вместо цифр, берутся настройки по умолчанию
        logging.warning(f"Ошибка ввода - {e}. Используются значения по умолчанию")
        return -3.0, 3.0, 0.5

# Создаю функцию для построения графиков функций
def plot_functions(start, end, step):

    # Проверяю, что введен шаг больше нуля
    if step <= 0:
        logging.error("Шаг должен быть больше нуля")
        raise ValueError("Шаг должен быть положительным")
                
    # Проверяю, что начало меньше конца
    if start >= end:
        logging.error("Начало должно быть меньше конца")
        raise ValueError("Начало диапазона не может быть больше или равно концу")
    
    # Задаю значения для оси X
    x = np.arange(start, end + step / 2, step)
    
    # Считаю Y по формулам
    y_square = x ** 2
    y_cube = x ** 3

    # Делаю размер графика 8 на 5
    fig, ax = plt.subplots(figsize=(8, 5))
    
    '''Рисую график функции x^2, задаю линию - синий пунктир 
    с точками  пересечения - кружочками, а также название, 
    которое будет отображено в легенде'''
    ax.plot(x, y_square, color='blue', linestyle='--', marker='o', label='у = х^2')
    
    '''Рисую график функции x^3, задаю цвет линии - красный, 
    метки - квадратики, также название для легенды'''
    ax.plot(x, y_cube, color='red', linestyle='-', marker='s', label='у = х^3')

    # Добавляю заголовок, подписи осей, сетку и легенду
    ax.set_title('Графики функций у = х^2 и у = х^3')
    ax.set_xlabel('Значения X')
    ax.set_ylabel('Значения Y')
    ax.grid(True)
    ax.legend(loc='upper left')

    logging.info("Графики успешно построены")
    
    # Вывод графика
    plt.show()

# Запуск программы
if __name__ == '__main__':
    logging.info("Запуск программы")
    a, b, h = get_user_input()
    try:
        plot_functions(a, b, h)
    except ValueError as e:
        logging.warning(f"Программа не построила график - {e}")

'''При создании программы я обращалась к ИИ-ассистенту 
за консультациями по коду и помощью в разборе ошибок 
для грамотного освоения материалов лекции и вебинара'''