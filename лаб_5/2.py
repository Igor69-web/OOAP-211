# Программирование на языке высокого уровня (Python).
# https://www.yuripetrov.ru/edu/python
# Задание task_05_02_02.
#
# Выполнил: Буц И.Д.
# Группа: АДЭУ-211
# E-mail: !!!
def avg(new_data):
    return sum(new_data) / len(new_data)
    # Удалите комментарий и допишите код
def cleared_data(data):
    new_data = []
    for x in data:
        if x != None:
            new_data.append(x)
    return new_data

n = int(input('Кол-во измерений: '))

# Если с клавиатуры вводится прочерк, измерения нет
# (необходимо добавить в список None)
data = []

for i in range(n):
    dimension = input('Измерение {}-е: '.format(i + 1))
    if dimension == '-': # dimension - измерение
        data.append(None) # append - добавление элемента
    else:
        data.append(int(dimension))
    i += 1

print("Средняя температура:", avg(cleared_data(data)))

# --------------
# Пример вывода:
#
# Кол-во измерений: 3
# Измерение 1-е: 10
# Измерение 2-е: -
# Измерение 3-е: 20
# Средняя температура: 15.0