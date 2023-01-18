# def add_one(a ,b):
#     return a + b + 1
#
# add_one2 = lambda a, b: a + b + 1
#
# result = lambda answer: True if answer == 'Д' else False
#
#
# # list comprehension
#
# from random import randint
#
# lst = []
# for i in range(5):
#     lst.append(randint(1, 5))
# print(lst)
#
# lst2 = [randint(1 ,5) for i in range(1, 6)]
# print(lst2)

#з1
# c2f = lambda c: 9/5 * c + 32
# print(c2f(200))
# f2c = lambda f:(f - 32) * 5/9
# print(f2c(200))
# c2k = lambda c: c + 273.15
# print(c2k(200))
# k2c = lambda k: k - 273.15
# print(k2c(200))
# f2k = lambda f: c2k(f2c(f))
# print(f2k(203))

#з2
# from random import randint
#
# exit = lambda b: True if b == 'да' else False
# while True:
#     a = int(input('скок '))
#     lst = [randint(1, 6) for i in range(a)]
#     print(lst)
#     if exit(input('да или нет ').lower()) == False:
#         break

field = {"A": ["⬜", "⬜", "⬜"],
         "B": ["⬜", "⬜", "⬜"],
         "C": ["⬜", "⬜", "⬜"]}

cell_letter = ["A", "B", "C"]
cell_number = ["1", "2", "3"]
def draw() -> None:
    print(' 1 2 3')
    for row in range(3):
        print(cell_letter[row], end='')
        for column in range(3):
            print(list(field.values())[row][column], end='')
        print()

def turn(a, b):
    pass
draw()