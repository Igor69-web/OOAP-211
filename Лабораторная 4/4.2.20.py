# Программирование на языке высокого уровня (Python).
# https://www.yuripetrov.ru/edu/python
# Задание task_04_02_20.
#
# Выполнил: Фамилия И.О.
# Группа: !!!
# E-mail: !!!


from collections import defaultdict
SUMS = defaultdict(list)
for e in range(100, 1000):
    SUMS[sum(int(x) for x in str(e))].append(e)

sum_ = int(input('Введите сумму цифр трехзначного числа:'))
print(f"Количество чисел с такой суммой {len(SUMS[sum_])}, а вот собственно и они {SUMS[sum_]}")


# Удалите комментарий и допишите код

# --------------
# Пример вывода
#
# n = 3
# 102 111 120 201 210 300
