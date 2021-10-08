# Программирование на языке высокого уровня (Python).
# https://www.yuripetrov.ru/edu/python
# Задание task_04_02_11.
#
# Выполнил: Буц И.Д.
# Группа: АДЭУ-211
# E-mail: ButsID@mgpu.ru


start = int(input("start = "))
k = int(input("k = "))
s = int(input("s = "))
n_count = 0
while n_count<10:
    if start%10==k and start%s==0:
        n_count+=1
        print(start,end=" ")
    start+=1


# --------------
# Пример вывода:
#
# start = 100
# k = 7
# s = 9
# 117 207 297 387 477 567 657 747 837 927