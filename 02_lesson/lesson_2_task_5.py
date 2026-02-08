month = int(input("Введите номер месяца (1-12): "))


def month_to_season(month):
    if 2 < month < 6:
        return ('Весна')
    elif 5 < month < 9:
        return ('Лето')
    elif 8 < month < 12:
        return ('Осень')
    elif month == 12 or 0 < month < 3:
        return ('Зима')
    else:
        return ('Некорректный номер месяца')


print(month_to_season(month))
