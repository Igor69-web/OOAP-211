# С начала суток прошло m минут (0<m≤24∗60).
# Определите:целое количество часов, прошедших с начала суток;
# количество минут, прошедших с момента начала последнего часа


# Программирование на языке высокого уровня (Python).
# https://www.yuripetrov.ru/edu/python
# Задание task_03_02_05.
#
# Выполнил: Буц И.Д.
# Группа: АДЭУ-211
# E-mail: ButsID@mgpu.ru


# Количество минут
m = int(input("m="))
# Количество часов, прошедших с начала суток
h = int(input("h="))
h2 = 120   # Колличестов минут в 2-х часах
# Количество минут, прошедших с момента начала последнего часа
m2 = 3
sut= h2+m2

print("Количество часов, прошедших с начала суток:", sut)

# --------------
# Пример вывода:
#
# Количество минут, прошедшее с начала суток: 123
# Количество часов, прошедших с начала суток: 2
# Количество минут, прошедших с момента начала последнего часа: 3