# class Car:
#     def __init__(self):
#         self.x = 0
#     def zaved(self):
#         self.x = 1
#         return 'zaveden, nelzya zav'
#     def nezaved(self):
#         self.x = 0
#         return 'nezaveden, nelzya glush'
#     def year(self, y):
#         self.y = y
#         return self.y
#     def type(self, t):
#         self.t = t
#         return self.t
#     def color(self, c):
#         self.c = c
#         return self.c
#
# a = Car()
# print(a.zaved())
# print(a.year(2005))
# print(a.color('red'))
# print(a.type('sedan'))
#
# import string
#
# class Alphabet:
#     def __init__(self):
#         self.lang = 'en'
#         self.__letters = string.ascii_lowercase
#     def print(self):
#         return self.__letters
#     def letters_sum(self):
#         return len(self.__letters)
#
# a = Alphabet()
# print(a.print())
# print(a.letters_sum())

# import datetime
# class Chasi:
#     def __init__(self):
#         self.__time = datetime.datetime.now().strftime('%H:%M:%S')
#         self.__h, self.__m, self.__s = self.__time.split(':')
#     def test_h(self):
#        if self.__h
#     def test_m(self):
#
#     def test_s(self):
#
#     def hour(self):
#         self.__h = int(self.__h)+1
#     def min(self):
#         None
#     def sec(self):
#         None
#     def cock(self):
#         return self.__h+':'+self.__m+':'+self.__s
#
# c = Chasi()
from random import choice
class BlaBlaBla:
    def __init__(self):
        self.__counter = 5

    def increment(self):
        self.__counter += 1

    def decrement(self):
        self.__counter -= 1

    def ret(self):
        return self.__counter


counter = BlaBlaBla()
l = [counter.increment, counter.decrement]

while 0 < counter.ret() < 10:
    choice(l)()
    print(counter.ret())
