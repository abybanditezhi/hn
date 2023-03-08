# class Person:  # объявление класса
#     def __init__(self, imya, vozrast):  # метод инициализации
#         self.age = vozrast  # Установка значений атрибутов
#         self.name = imya
#
#     def __str__(self):
#         return('че за тяги бархатные')
#
# leha = Person('лепеха', -32)
# print(leha.age)
# print(leha.name)
# print(leha)

# class Kefteme:
#     def __getitem__(self, item):
#         print('подкрадули лютые', item)
#
# obj = Kefteme()
# obj[2]


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def __str__(self):
#         return f"{self.x}, {self.y}"
# gg = Point(20, 40)
# wp = Point(40, 60)
# barhat = Point(32456789,9)
# class Rectangle:
#     def __init__(self):
#         self.xy1 = gg
#         self.xy2 = wp
#     def s(self):
#         a = self.xy2.x - self.xy1.x
#         b = self.xy2.y - self.xy1.y
#         return a * b
#     def p(self):
#         a = self.xy2.x - self.xy1.x
#         b = self.xy2.y - self.xy1.y
#         return (a+b)*2
#     def haspoint(self, huh):
#         if (self.xy1.x <= huh.x <=  self.xy2.x) and (self.xy1.y <= huh.y <=  self.xy2.y):
#             return True
#         else:
#             return False
# pr = Rectangle()
# print(pr.s())
# print(pr.p())
# print(pr.haspoint(barhat))

import random
class Wall:
    def __init__(self, shir):
        self.shir = shir
        self.height = random.randint(3, 7)
    def print_figure(self):
        d = '''⬛'''
        for i in range(self.height):
            print(d * self.shir)
obj = Wall(3)
print(obj.print_figure())