# Программирование на языке высокого уровня (Python).
# https://www.yuripetrov.ru/edu/python
# Задание task_05_02_05.
#
# Выполнил: Буц И.Д.
# Группа: АДЭУ-211
# E-mail: !!!

def is_leap(year): # Определяем високосный год или нет и следовательно определяем количество дней в феврале
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        febrary_day = 29
    else:
        febrary_day = 28
    return febrary_day
def days(month, year):
    # Вернуть количество дней в месяце 'month' года 'year'.
    month_day_31 = [1,3,5,7,8,10,12]
    month_day_30 = [4,6,9,11]
    if month in month_day_31:
        date= 31
    elif month in month_day_30:
        date = 30
    else:
        date = is_leap(year)
    return date
def previous_date(day, month, year):
    # Вернуть день, месяц, год предыдущего дня
    if day == 1:
        month -= 1
        if month == 0:
            year -= 1
            month = 12
        else:
            year = year
            month = month
    else:
        day -= 1
        month = month
        year=year
    return day, month, year
def next_date(day, month, year):
   # Вернуть день, месяц, год следующего дня.
    if day == days(month, year):
        month += 1
        if month == 13:
            month = 1
            year += 1
            day = 1
        else:
            month += 1
            year = year
            day = 1
    else:
        day += 1
        month = month
        year = year
    return day, month, year
day, month, year = input('День, месяц, год через пробел: ').split()
day = int(day)
month = int(month)
year = int(year)
print('Предыдущий день: ', previous_date(day, month, year))
print('Следующий день: ', next_date(day, month, year))


# --------------
# Пример вывода:
#
# День, месяц, год через пробел: 1 3 2000
# Предыдущий день: (29, 02, 2000)
# Следующий день: (02, 03, 2000)