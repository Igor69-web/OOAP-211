# Программирование на языке высокого уровня (Python).
# https://www.yuripetrov.ru/edu/python
# Задание task_07_02_04.
#
# Выполнил: Буц И.Д.
# Группа: АДЭУ-211
# E-mail: !!!


"""
Ошибки (номера строк через пробел, данная строка - №2): !!!
"""
def min_pair(nums):
    """Вернуть минимальную сумму соседних 2-х чисел в списке 'nums'."""
    min_1 = nums[0] + nums[1] # заменить * на +, так как нам нужна сумма, а не произведение
    len_nums = len(nums) # Добавляем переменную, чтобы получислось конкретное число (длинна списка)
    for i in range(2, len_nums - 1): # Нужно вычесть единицу, чтобы цик не выходил за пределы списка
        min_1 = min(nums[i] + nums[i + 1], min_1) # название переменных не может быть min

    return min_1

import random
#
random.seed(50)
#
N_MAX = 10
RANGE_MIN = 1
RANGE_MAX = 100
nums = random.sample(range(RANGE_MIN, RANGE_MAX), N_MAX)
#
print(nums)
#
print(min_pair(nums))