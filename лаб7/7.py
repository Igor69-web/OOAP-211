# Программирование на языке высокого уровня (Python).
# https://www.yuripetrov.ru/edu/python
# Задание task_07_02_07.
#
# Выполнил: Буц И.Д.
# Группа: АДЭУ-211
# E-mail: !!!


"""
Ошибки (номера строк через пробел, данная строка - №2): !!!
"""
def power(x, y = 2):
    """Вернуть x^y."""
    if y == 0:
        return 1
    elif x == 0:
        raise ValueError('Невозможно определить число при введенных значениях')
    else:
        return x * power(x, y - 1)

try:
    x = int(input("x= "))
    y = int(input("y= "))
    print(power(x, y))

except ValueError as err:
    print("Ошибка:", err)