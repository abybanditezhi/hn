import easygui
import random

sila = 1
ability = 1
intelekt = 1


def kachalka():
    global sila, ability, intelekt
    while True:
        n = easygui.buttonbox(
            msg=f'СИЛА: {sila}\n'
                f'ЛОВКОСТЬ: {ability}\n'
                f'ИНТЕЛЕКТ: {intelekt}',
            images=['img/s.png', 'img/abil.png', 'img/um.png'],
            choices=('выйти',)

        )
        if n == 'выйти' or n == None:
            break
        elif n == 'img/s.png':
            sila += round(random.random() + 0.5, 1)
        elif n == 'img/abil.png':
            ability += round(random.random() + 0.5, 1)
        else:
            intelekt += round(random.random() + 0.5, 1)
        print(n)


games = [
    'качалка',
]

games_entry_points = [
    kachalka,
]

while True:
    res = easygui.buttonbox('Выбери игру!', choices=games)
    if res is None:
        break
    games_entry_points[games.index(res)]()