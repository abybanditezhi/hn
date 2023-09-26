# def fkkk(x: int = 'y') -> int:
#     '''пенсил'''
#     return x
#
#
# result = fkkk(2)
# print(result)

# def fefd(y, *args, **kwargs):
#     #args - pos args
#     #kwargs - keywords args
#     print(args) #кортеж
#     print(kwargs) # dict
#     print(y)
#
#
# print(fefd(1, 2, 3, a=1488, b=228))


#1

# def fu(**kwargs):
#     for i in kwargs:
#         print(i.ljust(30), str(kwargs[i]).rjust(10))
#     print('-'*41)
#     print(str(sum(kwargs.values())).rjust(41))
#
#
# fu(apple=105, banana=230, penis=132)

#2

# def cs(x:str) -> str:
#     res = ''
#     for i in x:
#         if i.islower():
#             res += i
#         else:
#             res += '_' + i.lower()
#     return res
#
#
# print(cs('word'))
# print(cs('wordSecond'))

#3

# ООП: инкапсуляция, полиморфизм, наследование

class Human:
    def say(self, phrase): # метод public
        self.__vdoh()
        return phrase + ' сам чурка'

    def __vdoh(self):
        print('*делает невероятно плотную хапочку для мориарти*')

    def __init__(self):
        self.age = 5



petr = Human() # создание объекта на основе класса
print(petr.say('эээ чурка'))
print(petr._Human__vdoh())
igor = Human()
print(petr.age)