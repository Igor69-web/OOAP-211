# Программирование на языке высокого уровня (Python).
# https://www.yuripetrov.ru/edu/python
# Задание task_04_02_13.
#
# Выполнил: Фамилия И.О.
# Группа: !!!
# E-mail: !!!
import math
a = int(input("a = "))
b =int(input("b = "))
n_mult = b
if a<=b:
    for i in range(a,b):
        n_sum= sum(range(a,b+1))
        n_mult*=i
        n_avg = sum(range(a,b+1))/ (len(range(a,b+1)))
        n_avg_geom = round(math.sqrt(a*b),2)
print("Сумма =", n_sum)
print("Произведение =", n_mult)
print("Среднее арифметическое = {}".format(n_avg))
print("Среднее геометрическое нечетных чисел = {}".format(n_avg_geom))
print("Отрезок",list(range(a,b+1)))



# --------------
# Пример вывода:
#
# a = 1
# b = 5
# Сумма = 15
# Произведение = 120
# Среднее арифметическое = 3.00
# Среднее геометрическое нечетных чисел = 2.24
