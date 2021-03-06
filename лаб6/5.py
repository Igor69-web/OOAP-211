# Программирование на языке высокого уровня (Python).
# https://www.yuripetrov.ru/edu/python
# Задание task_06_02_05.
#
# Выполнил: Буц И.Д.
# Группа: АДЭУ-211
# E-mail: !!!


def foo(nums):
    """!!!

    Параметры:
        - nums (list): список.

    Сложность: !!!.
    """
    for x in nums: # O(1)
        if x % 2 == 0: # O(1)
            return True
    else:
        return False

nums = [1, 3, 5, 6]
foo(nums)

# Алгорит: Проверяет на четность или нечетность элементы списка, если хотя бы один из элементов четное число, тогда будет True, если нет четных чисел в списке, тогда False
# Сложность: O(1) + O(1) = 2 * O(1)