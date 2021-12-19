# Программирование на языке высокого уровня (Python).
# https://www.yuripetrov.ru/edu/python
# Задание task_07_02_09.
#
# Выполнил: Буц И.Д.
# Группа: АДЭУ-211
# E-mail: !!!


"""
Ошибки (номера строк через пробел, данная строка - №2): !!!
"""
def f(x):
    """Вернуть значение функции.

    Функция не обрабатывает исключения.
    """
    try:
        return x**2 / (x + 2) - 3
    except ZeroDivisionError:
        return '-'


k = int(input("Введите границу интервала [-k; k]: "))
h = float(input("Введите шаг табуляции: "))

x = -k
print("{:>10} {:>10}".format("x", "f(x)"))
while x <= k:
    try:
        print("{:10.2f} {:10.2f}".format(x, f(x)))
    except ValueError:
        pass

    x += h
