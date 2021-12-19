# Программирование на языке высокого уровня (Python).
# https://www.yuripetrov.ru/edu/python
# Задание task_05_02_03.
#
# Выполнил: Буц И.Д.
# Группа: АДЭУ-211
# E-mail: !!!
lucky_num = []
number = []
lk_num = []
def is_lucky(num):
	even = 0
	odd = 0
	for i in map(int, str(num)):
		if i % 2 == 0:
			even += 1
		else:
			odd += 1
	if even == odd:
		lucky_num.append(num)
	else:
		pass
def lucky_numbers(a, b):
	num = a
	while num in range(a, b + 1):
		is_lucky(num)
		if num in lucky_num:
			lk_num.append(num)
			num += 1
		else:
			num += 1

	return lk_num
a = int(input("Первый номер билета: "))
b = int(input("Последний номер билета: "))
print(lucky_numbers(a, b))
# Вывод должен быть осуществлен в строку с одним пробелом-разделителем


# --------------
# Пример вывода:
#
# Первый номер билета: 10
# Последний номер билета: 25
# 10 12 14 16 18 21 23 25