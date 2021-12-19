# Программирование на языке высокого уровня (Python).
# https://www.yuripetrov.ru/edu/python
# Задание task_05_02_08.
#
# Выполнил: Буц И.Д.
# Группа: АДЭУ-211
# E-mail: !!!
def print_with_border(s, k):
    s_len = len(s)
    print(k * (s_len + 2))
    print(k + s + k)
    print(k * (s_len + 2))

s = input("Введите строку: ")
k = input("Введите символ: ")
print_with_border(s, k)

# --------------
# Пример вывода:
#
# Введите строку: Просто текст
# Введите символ: +
# ++++++++++++++
# +Просто текст+
# ++++++++++++++