# ООП: 1) инкапсуляция: приватное и публичное
# 2) наследование: родительский и дочерние класса, super
# 3) полиморфизм: магические методы

# инкапсуляция:
# class Urok:
#     shkola = 28  # статический публичный атрибут
#     __secret = 123 # статический приватный атрибут
#     def __init__(self, dlitel):  # mag metod
#         self.dlitelnost = dlitel  # динамический публичный атрибут
#         self.__secret2 = 321 # динамический приватный атрибут
#
#     def get5(self):
#         return 5
#
#
# mmm = Urok(50)  # инициализация -> создание obj на основе класса
# print(mmm.get5())  # 5
# print(mmm.dlitelnost) # 40
#
# fiz = Urok(10)
# print(fiz.shkola) # вызов статистеческого атрибута
# Urok.shkola = 'заднеприводная' # menyaem static atribut
# print(mmm.shkola)

# полиморфизм

# class Cls63amg:
#     def __call__(self, *args, **kwargs):  # срабатывает при вызове объекта класса
#         print(args)
#         print(kwargs)
#         return 'пенсил'
#
#     def __add__(self, other):
#         return f"{self} + {other}"
#
#
# class Cls53amg:
#     def __str__(self):  # str(), print()
#         return 'пенис'
#
#
# c1 = Cls63amg()
# c2 = Cls53amg()
# print(c1(1, [''], key1={}))  # __call__
# print(c2)
# print(c1.__add__(c2))  # строка выше = то же самое

# наследование

class Cl1:
    def __init__(self):
        self.penis = 'пенис'

    def take_penis(self):
        print('пенсил')


class Cl2(Cl1):  # cl2 наследник cl1
    def __init__(self):
        super().__init__()
        self.haram = 'жопа'


obj1 = Cl1()
print(obj1.penis)
obj2 = Cl2()
print(obj2.penis)
print(hasattr(obj2, 'penis'))
print(getattr(obj1, 'penis'))