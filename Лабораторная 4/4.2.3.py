# Программирование на языке высокого уровня (Python).
# https://www.yuripetrov.ru/edu/python
# Задание task_04_02_03.
#
# Выполнил: Буц И.Д.
# Группа: АДЭУ-211
# E-mail: ButsID@mgpu.ru


a = int(float(input("a=")))
b = int(float(input("b=")))
d = int(float(input("d=")))
c = min(a,b,d)
if c<0:
    print("Проверьте код!")
# Введенные числа должны быть положительными, если так - осуществляем
# расчет, иначе выводим "Проверьте ввод"
if d+1>=a and d+1>=b:
    print("Нет")
else:
    print("Да")
    fix = 1 # Зазор

    # Вывести "Да" или "Нет"

# --------------
# Пример вывода:
#
# Ширина форточки: 5
# Высота форточки: 6
# Диаметр головы: 6
# Нет

# Ширина форточки: 6
# Высота форточки: 7
# Диаметр головы: 4
# Да
