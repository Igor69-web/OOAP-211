# Программирование на языке высокого уровня (Python).
# https://www.yuripetrov.ru/edu/python
# Задание task_07_02_01.
#
# Выполнил: Буц И.Д.
# Группа: !!!
# E-mail: !!!


"""
Ошибки (номера строк через пробел, данная строка - №2): !!!
"""
def sum_of_digits(n):
	"""Вернуть сумму цифр меньших 5 для положительного целого числа `n`.
	Если таких цифр нет, вернуть 0."""
	с = 0
	while n > 0:
		digit = n % 10  # Было digit = n % 10. Нужно найти остаток от деления, а не целочисленное деление, чтобы определить псоледнюю цифру
		if digit < 5:
			c += digit  # Было c = c + 1. C - сумма цифр меньших 5, поэтому нужно прибавлять digit- цифра в числе, а не + 1, так как нужно найти сумму цифр меньше 5, а не количество
		n // = 10
	return с  # нужно, чтобы выводилась сумма, а не число


sum_of_digits(1234)