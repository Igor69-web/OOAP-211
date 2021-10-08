# Программирование на языке высокого уровня (Python).
# https://www.yuripetrov.ru/edu/python
# Задание task_04_02_19.
#
# Выполнил: Фамилия И.О.
# Группа: !!!
# E-mail: !!!


a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
for i in range(a,b+1):
    if i%c==0:
        print(i,end=" ")

# --------------
# Пример вывода:
#
# a = 1
# b = 10
# c = 2
# 2 4 6 8 10
