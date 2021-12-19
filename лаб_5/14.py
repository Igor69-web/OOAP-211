# Программирование на языке высокого уровня (Python).
# https://www.yuripetrov.ru/edu/python
# Задание task_05_02_14.
#
# Выполнил: Буц И.Д.
# Группа: АДЭУ-211
# E-mail: !!!
minus = []
plus = []
numbers = list(map(int,input().split()))
def split_numbers(numbers):
   for n in numbers:
     if n < 0:
        minus.append(n)
     else:
        plus.append(n)
   plus.sort()
   minus.sort()
   minus.reverse()
   return minus, plus

print(split_numbers(numbers))

# --------------
# Пример вывода:
#
# ([-5, -33], [0, 1, 4])