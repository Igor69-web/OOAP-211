# Составьте программу, которая запрашивает у пользователя 2 целых числа и выполняет операции:
# Выводя на экран результат каждого действия. В случае получение вещественного результата, округлите
# его до 2-х знаков после запятой (используя функцию round()).

# Программирование на языке высокого уровня (Python).
# https://www.yuripetrov.ru/edu/python
# Задание task_03_02_01.
#
# Выполнил: Буц И.Д.
# Группа: АДЭУ-211
# E-mail: ButsID@mgpu.ri


a = int(input("a="))
b = int(input("b="))
round(a)
round(b)


print(a + b)
print(a - b)
print(a * b)
print(round(a / b))
print(a // b)
print(a % b)
print(a ** b)

print(a < b)
print(a <= b)
print(a > b)
print(a >= b)
print(a != b)
print(a == b)


# --------------
# Пример вывода:
#
# a=2
# b=3
# 5
# -1
# 6
# 0.67
# 0
# 2
# 8
# True
# True
# False
# False
# True
# False