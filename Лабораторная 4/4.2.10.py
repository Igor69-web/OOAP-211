# Программирование на языке высокого уровня (Python).
# https://www.yuripetrov.ru/edu/python
# Задание task_04_02_10.
#
# Выполнил: Буц И.Д.
# Группа: АДЭУ-211
# E-mail: ButsID2mgpu.ru


n = int(input("n = "))
n_sum = 0
n_count = len(str(n))
while n>0:
    n1 = n%10
    n_sum = n_sum + n1
    n = n//10
print("Сумма=",n_sum)
print("Колличество=",n_count)

# --------------
# Пример вывода:
#
# n = 12345
# Сумма = 15
# Количество = 5
