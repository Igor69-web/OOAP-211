# Программирование на языке высокого уровня (Python).
# https://www.yuripetrov.ru/edu/python
# Задание task_05_02_17.
#
# Выполнил: Буц И.Д.
# Группа: АДЭУ-211
# E-mail: !!!
def digits_sum(value):
# Вернуть сумму цифр числа 'value'. Рекурсивная реализация.
    value_str = str(value)
    sum = 0
    value_len = len(value_str)
    for i in range(value_len + 1):
        sum += i
    return sum
def digits_count(value):
# Вернуть количество цифр числа 'value'. Рекурсивная реализация.
    value_str = str(value)
    value_len = len(value_str)
    return value_len


print(digits_sum(12345))
print(digits_count(12345))

# --------------
# Пример вывода:
#
# 15
# 5