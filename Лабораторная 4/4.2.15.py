# Программирование на языке высокого уровня (Python).
# https://www.yuripetrov.ru/edu/python
# Задание task_04_02_15.
#
# Выполнил: Фамилия И.О.
# Группа: !!!
# E-mail: !!!


p = int(input("Грузоподъемность грузовика (кг.) = "))
n = int(input("Количество предметов = "))
total = 0
for i in range(n):
    m =int(input("Масса {}-го предмета (кг.) = ".format(i+1)))
    total+=m
print(total<=p)



# Удалите комментарий и допишите код

# --------------
# Пример вывода:
#
# Грузоподъемность грузовика (кг.) = 10
# Количество предметов = 2
# Масса 1-го предмета (кг.) = 3
# Масса 2-го предмета (кг.) = 3
# Да