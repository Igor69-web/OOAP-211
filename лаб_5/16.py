# Программирование на языке высокого уровня (Python).
# https://www.yuripetrov.ru/edu/python
# Задание task_05_02_16.
#
# Выполнил: Буц И.Д.
# Группа: АДЭУ-211
# E-mail: !!!
def pow1(value, power):
	return value ** power

# """Вернуть 'value' в степени 'power'

def pow2(value, pover):
	# """Вернуть 'value' в степени 'power'. Рекурсивный алгоритм.
	if pover == 0 or value == 1:
		return value
	else:
		return value ** pover


print(pow1(5, 3))
print(pow2(5, 3))

# --------------
# Пример вывода:
#
# 125
# 125