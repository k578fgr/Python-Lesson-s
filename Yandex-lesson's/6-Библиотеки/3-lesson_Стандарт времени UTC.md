Позже этот всемирный формат заменили на новый, определяемый атомными часами. Это UTC — «coordinated universal time» — всемирное координированное время. 
У любой переменной типа данных datetime можно вызвать метод utcnow(). Он вернёт текущий момент времени по UTC с эталонной точностью до микросекунд.
Напишем программу-часы:

import datetime as dt

utc_time = dt.datetime.utcnow()
print(utc_time)

Не беда! На такой случай есть тип данных timedelta, в котором можно сохранить определённый промежуток времени — в часах, днях, годах, как угодно. Этот тип данных тоже хранится в библиотеке dt. А объект такого типа создаётся функцией timedelta()

import datetime as dt

# Как и раньше - определяем текущее время UTC
utc_time = dt.datetime.utcnow()

# Создаём промежуток времени в три часа
period = dt.timedelta(hours=3)

# И прибавляем к значению времени по UTC поправку в три часа:
moscow_time = utc_time + period

# Печатаем
print(moscow_time) 

Задание 1

import datetime as dt

UTC_OFFSET = {
    'Санкт-Петербург': 3,
    'Москва': 3,
    'Самара': 4,
    'Новосибирск': 7,
    'Екатеринбург': 5,
    'Нижний Новгород': 3,
    'Казань': 3,
    'Челябинск': 5,
    'Омск': 6,
    'Ростов-на-Дону': 3,
    'Уфа': 5,
    'Красноярск': 7,
    'Пермь': 5,
    'Воронеж': 3,
    'Волгоград': 3,
    'Краснодар': 3,
    'Калининград': 2
}

def what_time(city):
    # Напишите код тела функции;
    utc_time = dt.datetime.utcnow()
    period = dt.timedelta(hours = UTC_OFFSET[city])
    result = utc_time + period
    return result
    # она должна вернуть текущее время в городе city


print(what_time('Екатеринбург'))

Результат

2023-07-26 03:25:02.166688

Задание 2

import datetime as dt

DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь'
}

UTC_OFFSET = {
    'Санкт-Петербург': 3,
    'Москва': 3,
    'Самара': 4,
    'Новосибирск': 7,
    'Екатеринбург': 5,
    'Нижний Новгород': 3,
    'Казань': 3,
    'Челябинск': 5,
    'Омск': 6,
    'Ростов-на-Дону': 3,
    'Уфа': 5,
    'Красноярск': 7,
    'Пермь': 5,
    'Воронеж': 3,
    'Волгоград': 3,
    'Краснодар': 3,
    'Калининград': 2
}

def what_time(friend):
    # напишите код тела функции
    utc_time = dt.datetime.utcnow()
    city = DATABASE[friend]
    period = dt.timedelta(hours = UTC_OFFSET[city])
    result = utc_time + period
    return result
    # пусть она вернет время у друга из аргумента friend


print(what_time('Соня'))