Ответ на тест
# Количество баллов, которое студент получил за тест.
score = 60

def test_score():
    if score > 50:
        print('Отличная работа!')
        print('Тест сдан.')
    else:
        print('Хорошая попытка!')
        print('Вы отлично постарались, но нужно подготовиться чуть получше.')
        print('Ещё раз пройти тестирование можно в следующую среду.')

test_score()

Пример

users = ['Степан', 'Анатолий', 'Антон', 'Андрей']


def print_users(users):
    for user in users:
        print(user)
print_users(users)


Результат

Степан
Анатолий
Антон
Андрей


Этот код всегда возвращает вариант Сочи

resorts = ['Сочи', 'курорты Краснодарского Края', 'Санкт-Петербург', 'Карелию']

def choose_vacation_place(resorts):
    for resort in resorts:
      if resort == 'Сочи':
        return resort
resort = choose_vacation_place(resorts)
print('Поехали в ' + resort)

Поехали в Сочи