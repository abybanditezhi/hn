# import easygui
# easygui.msgbox(
#     msg='тинкерин эбаут)))))))',
#     image='img/png-clipart-minion-minion.png',
#     title='скр скр эщкере',
#     ok_button='нахаслил себе на кроссовки за 3 дня'
# )

# easygui.buttonbox(
#     msg='куда сам сядешь...',
#     choices=('жидкий стул', 'твердый стул'),
#     title='капец'
# )

# number = easygui.integerbox(
#     msg='за сколько купишь',
#     lowerbound=5,
#     upperbound=148,
#     image='img/png-clipart-minion-minion.png',
#     default=14.88
#
# )
# print(number)

# text = easygui.enterbox(
#     msg='ты кто',
#     title='мяу',
#     default='скр скр эщкере'
# )
#
# print(text)

import easygui
import random


def rock_paper_scissors():
    slovarik = {'ножницы': 'img/a.png',
                'камень': 'img/ab.png',
                'бумага': 'img/abc.png'}
    result = easygui.buttonbox(
        msg='ытыгшуукашщвмвагшдпыщашолщшщзфыщауцш0',
        title='запрети мне носить стон айленд',
        images=['img/a.png', 'img/ab.png', 'img/abc.png'],
        choices=('выйти',)
    )
    komp = random.choice(list(slovarik.keys()))
    print(result, komp)
    if result == slovarik['камень'] and komp == 'камень':
        easygui.msgbox(msg='ничья')
    elif result == slovarik['камень'] and komp == 'бумага':
        easygui.msgbox(msg='loosee broo')
    elif result == slovarik['камень'] and komp == 'ножницы':
        easygui.msgbox(msg='win broo')
    elif result == slovarik['бумага'] and komp == 'камень':
        easygui.msgbox(msg='win broo')
    elif result == slovarik['бумага'] and komp == 'бумага':
        easygui.msgbox(msg='ничья')
    elif result == slovarik['бумага'] and komp == 'ножницы':
        easygui.msgbox(msg='looseee broo')
    elif result == slovarik['ножницы'] and komp == 'камень':
        easygui.msgbox(msg='слив broo')
    elif result == slovarik['ножницы'] and komp == 'ножницы':
        easygui.msgbox(msg='ничья')
    elif result == slovarik['ножницы'] and komp == 'бумага':
        easygui.msgbox(msg='win broo')


def guess_the_number():
    life = 7
    number = easygui.integerbox(
        msg="Попробуй угадать число",
        lowerbound=1,
        upperbound=100,
    )
    computer = random.randint(1, 100)
    print(computer)
    while life > 0:
        if number < computer:
            number = easygui.integerbox(
                msg=f"Больше \n"
                    f"Жизней осталось: {life}",
                image="img/bolshe.png",

            )
        elif number > computer:
            number = easygui.integerbox(
                msg=f"Меньше \n"
                    f"Жизней осталось: {life}",
                image="img/menshe.png",
            )
        else:
            easygui.msgbox(msg="ура пабеда")
            break
        life -= 1


games = [
    'Камень, ножницы, бумага',
    'Угадай число'
]

games_entry_points = [
    rock_paper_scissors,
    guess_the_number
]

while True:
    res = easygui.buttonbox('Выбери игру!', choices=games)
    if res is None:
        break
    games_entry_points[games.index(res)]()