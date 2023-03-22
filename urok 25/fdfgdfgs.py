# class Class:
#     prosto1 = True
#     __pr = True
#
#     def __init__(self, x='кефтеме'):
#         self.prosto2 = x
#         self.__pr2 = x
#
#
# obj = Class()
# print(obj.prosto1, obj.prosto2)

import random
import easygui
class Human:
    default_age = 40
    default_name = 'саня'

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 10000000
        self.__house = 'нету'


    def info(self):
        return self.name, self.age, self.__money, self.__house


    def earn_money(self):
        self.__money += 100000
        return self.__money


    def default_info(self):
        return  Human.default_age, Human.default_name


    def __make_deal(self):
        if self.__money >= b.final_price():
            self.__house = 'хата есть'
            self.__money -= b.final_price()
            return 'хата есть', self.__money
        else:
            return 'денег нет'

class House:
    skida = random.randint(5, 30)
    def __init__(self, x, y):
        self.__area = x
        self.__price = y


    def final_price(self, skid=skida):
        return self.__price * (1 - (skid / 100))

a = Human()
b = House(100, 6000000)



j = easygui.enterbox(
    msg='твое имя и возраст',
    default=(a.default_age, a.default_name),
    title='опрос'
)
otb = j.split()
a.name = otb[0]
a.age = otb[1]


# def vibor():

def farm():
    while True:
        frm = easygui.msgbox(
            msg=a._Human__money,
            ok_button='фарм',
        )
        if frm == 'фарм':
            a.earn_money()
        else:
            break
def infr():
    inf = easygui.msgbox(
        msg=a.info()
    )
def buy():
    boy = easygui.buttonbox(
        msg='купить?',
        choices=('купить', 'отказаться')
    )
    if boy == 'купить':
        print(easygui.msgbox(
            msg=a._Human__make_deal()
        ))


hjhjh = [
    'информация',
    'покупка',
    'фарм'
]

vbrs = [
    infr,
    buy,
    farm
]

while True:
    c = easygui.buttonbox(
        msg=j,
        choices=hjhjh,
        title='братан'
    )
    if c is None:
        break
    vbrs[hjhjh.index(c)]()