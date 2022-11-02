# # import random
# import random as r
# from random import randint
# from random import *
# # x = random.randint(0, 100)
# # print(x)
#
# spisok = [1, 2, 3, 4, 5]
# print(r.choice(spisok))
# r.shuffle(spisok)
# print(spisok)

# import turtle
#
# screen = turtle.Screen()
# t = turtle.Turtle()
# horizontal = 200
# vertical = 100
# t.color('dark green', 'yellow')
# t.pensize(8)
# t.speed(5)
# # 1 - медленная, 10 - быстрая, 0 - макс
#
# t.begin_fill()
#
# t.forward(horizontal)
# t.right(90)
# t.forward(vertical)
# t.right(90)
# t.fd(horizontal)
# t.rt(90)
# t.fd(vertical)
# t.rt(90)
#
# t.end_fill()
#
# t.penup()
# t.goto(120, -30)
# t.pendown()
# t.forward(30)
#
# t.circle(50)
# t.color('red')
# t.write('тинкерин эбаут)))', font=('Arial black', '50', 'normal'), align='center')
#
# screen.exitonclick()

# import random
# import time
# hacked = 0
# while hacked < 100:
#     hacked += random.randint(1, 10)
#     if hacked >= 100:
#         print('ай сауууууууууу братиш')
#     else:
#         print(f'прогресс: {hacked}%')
#         time.sleep(1)

# import random
# variants = ['1', '2', '3']
# guess = input('gde sharik? 1, 2, 3\n'
#               '-----> ')
# answer = random.choice(variants)
# if guess == answer:
#     print('айй саууууууу брат')
# else:
#     print('двенааааааааадцать танго?!?!?!?!?!')
#     print(f'был в {answer}')

# import turtle
# import random
# screen = turtle.Screen()
# t = turtle.Turtle()
# t.speed(0)
# t.pensize(5)
# colors = ['red', 'green', 'blue', 'yellow', 'pink', 'black']
# i = int(input('storon: '))
#
# side = 100
# for j in range(0, i):
#     t.color(random.choice(colors))
#     t.forward(side)
#     t.rt(360/i)
#
#
# screen.exitonclick()

import time
import random
print('asssalyam aleikum')
abc = True
while abc:
    patron = random.choice([1, 2, 3, 4, 5, 6])
    our = random.choice([1, 2, 3, 4, 5, 6])

    print('zaryazhai')
    time.sleep(2)
    print('krutim baraban')
    time.sleep(1)
    print('vistrel cherez')
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    time.sleep(1)
    if patron == our:
        print('dead inside((((((((')
        abc = False
    else:
        print('вайяяяяяяяяяяяяя брат')
        if (input('igraem? ') == 'нет'):
            abc = False