# Программирование на языке высокого уровня (Python).
# https://www.yuripetrov.ru/edu/python
# Задание task_06_02_04.
#
# Выполнил: Буц И.Д.
# Группа: АДЭУ-211
# E-mail: !!!

def foo(n):
    """!!!

    Параметры:
        - n (int): число.

    Сложность: !!!.
    """
    res = []
    for i in range(1, n + 1): #O(N)
        divisors = 0
        j = 2
        while j < i and divisors == 0: # O(1)
            if i % j == 0: # O(1)
                divisors += 1
            j += 1

        if divisors == 0: # O(1)
            res.append(i)

    return res

n = 13
foo(n)

# Алгорит: выводит все числа простые числа до введенного числа, включая само число, при условии, что оно простое
# Сложность: O(N) * (O(1) * O(1) + O(1))= 2 * O(N)