# Дано слово объектно-ориентированный.
# Используя индексацию и срезы составьте из него слова объект, ориентир, тир, кот, рента и выведите их на экран.
# Программирование на языке высокого уровня (Python).
# https://www.yuripetrov.ru/edu/python
# Задание task_03_02_09.
#
# Выполнил: Буц И.Д.
# Группа: АДЭУ-211
# E-mail: ButsID@mgpu.ru


word = "объектно-ориентированный"

w1 = word[:6]  # (слово объект)
word1 = "ориентированный"
w2 = word1[:8]
w3 = word1[5:8]
w4 = word[4:16:5]
w5 = word1[1:4:2]+word1[4]+word1[5:11:5]

print(w1, w2, w3, w4, w5, sep="\n")


# --------------
# Пример вывода:
#
# объект
# ориентир
# тир
# кот
# рента