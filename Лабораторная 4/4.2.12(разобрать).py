# Программирование на языке высокого уровня (Python).
# https://www.yuripetrov.ru/edu/python
# Задание task_04_02_12.
#
# Выполнил: Фамилия И.О.
# Группа: !!!
# E-mail: !!!


a = int(input("a ="))
b = int(input("b ="))
i = 1
if a<b:
    while i<b:
     print(i,end = ' ')
     i+=1
else:
  for i in range(b,a):
      print( i, end = ' ')
      i=i+1
if a<b:
  i=b+1
  while i!=a-1:
    print(i)
    i=i-1
else:
  i=a+1
  while i!=b-1:
    print(i)
    i=i-1


# --------------
# Пример вывода:
#
# a = 1
# b = 5
# 1 2 3 4 5
# 5
# 4
# 3
# 2
# 1
