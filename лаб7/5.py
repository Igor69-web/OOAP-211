# Программирование на языке высокого уровня (Python).
# https://www.yuripetrov.ru/edu/python
# Задание task_07_02_05.
#
# Выполнил: Буц И.Д.
# Группа: АДЭУ-211
# E-mail: !!!


"""
Ошибки (номера строк через пробел, данная строка - №2): !!!
"""
def non_negatives(nums):
    """Удалить из списка чисел 'nums' отрицательные элементы и вернуть
    измененный список."""
    for i in range(len(nums)):
        if nums[i] < 0:
            nums[i] = '-' # было del nums[i]. Из-за удаления отрицательных чисел длинна списка меняется и не пересчитывается, поэтому м заменяем отрицательные значения на '-'
    new_num = []
    for i in range(len(nums)):# Все отрицательные числа стали '-', мы добавляем в новый список числа без '-' и получаются только положительные
        if nums[i] != '-':
            new_num.append(nums[i])
    return new_num

import random
#
n = 10
nums = [round(random.uniform(-10, 10), 2) for i in range(n)]
print(nums)
non_negatives(nums)
