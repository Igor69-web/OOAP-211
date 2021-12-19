# Программирование на языке высокого уровня (Python).
# https://www.yuripetrov.ru/edu/python
# Задание task_06_02_03.
#
# Выполнил: Буц И.Д.
# Группа: АДЭУ-211
# E-mail: !!!
def foo(s):
    """!!!

    Параметры:
        - s (str): строка.

    Сложность: !!!.
    """
    val = 0
    for c in s: # O(N)
        if c.isdigit(): # O(1)
            val += int(c)
    return val

s = '87'
foo(s)

# Алгорит: выводит сумму чисел, которые записаны в str
# Сложность: O(N) * O(1) = O(N)