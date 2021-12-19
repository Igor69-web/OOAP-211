# Программирование на языке высокого уровня (Python).
# https://www.yuripetrov.ru/edu/python
# Задание task_05_02_01.
#
# Выполнил: Буц И.Д.
# Группа: АДЭУ-211
# E-mail: !!!
def sgn(a):
    x = a
    y = a
    if a > 0:
        return 1
    elif a < 0:
        return -1
    else:
        return 0
x = float(input("Введите х: "))
y = float(input("Введите y: "))
z = ((sgn(x) + y**2)/(sgn(y) - abs(x)**0.5)) # abs - модуль

print("Ответ:", round(z,2))

# --------------
# Пример вывода:
#
# Введите x: -9
# Введите y: 0
# Ответ: 0.33