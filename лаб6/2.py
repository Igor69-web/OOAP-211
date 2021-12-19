# Программирование на языке высокого уровня (Python).
# https://www.yuripetrov.ru/edu/python
# Задание task_06_02_02.
#
# Выполнил: Буц И.Д.
# Группа: АДЭУ-211
# E-mail: !!!

def foo(i):
    """!!!

    Параметры:
        - i (int): число.

    Сложность: !!!.
    """
    digits = "0123456789"
    if i == 0: # O(1)
        return "0"
    result = ""
    while i > 0: # O(N)
        result = digits[i%10] + result
        i = i // 10
    return result

i = 7998
foo(i)

# Алгорит: выводит то же самое число, превращая его из int в str
# Сложность: O(N) + O(1) = 1 + O(N)