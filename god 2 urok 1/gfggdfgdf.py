# x = [1, 2, 3]
# y = x # y ssilaetsa na x
# y.append(5)
# print(x)
# print(y)
#
# x = [1, 2, 3]
# y = x[:] # glubokaya kopiya
# y.append(5)
# print(x)
# print(y)
#


# a = 'robert'
# b = '22'
# c = 262
# print(f'Его имя {a} Полсон(уодлоу)... Возраст {b} года, рост {c} см.')
# yn = input('Ваше имя: ')
# yh = int(input('ваш рост: '))
# print(f'{yn}, ты ниже {a}, на {c-yh} сантиметров')

# first = input().lower().strip()
# second = input().lower().strip()
# h = ['красный', 'желтый', 'синий', 'жёлтый']
# if first not in h or second not in h:
#     print('другие цвета выбирай черномазый')
# elif (first == h[0] or second == h[0]) and (first == h[1] or second == h[1]):
#     print('оранжевый')
# elif (first == h[0] or second == h[0]) and (first == h[2] or second == h[2]):
#     print('фиолетовый')
# elif (first == h[2] or second == h[2]) and (first == h[1] or second == h[1]):
#     print('зеленый')
# elif first == second:
#     print('ты че на приколе')
# a = int(input('1 number: '))
# b = int(input('2 number: '))
# if a <= b:
#     for i in range(a, b+1):
#         print(i**2)
# else:
#     for i in range(a, b-1, -1):
#         print(i**2)

# a = int(input('1 number: '))
# b = int(input('2 number: '))
# if a <= b:
#     for i in range(a, b+1):
#         print(i**3)
# else:
#     for i in range(a, b-1, -1):
#         print(i**3)

# a = int(input('number: '))
# sum = 1
# for i in range(1, a+1):
#     sum *= i
# print(sum)

# start = int(input('start population: '))
# plas = int(input('plas (%): ').strip('%')) / 100
# count = int(input('count of days: '))
# for i in range(0, count):
#     print(round(start, 3))
#     start += start * plas

# x = [7, 6, 5, 3, 1, 2, 9, 8, 3, 2, 1]
#
# print('+{}({}{}{}){}{}{}-{}{}-{}{}'.format(*x))

# import string
# small = list(string.ascii_lowercase)
# x = 'The sun is good, but i am an anime character'.lower()
# chc = ''
# for i in x:
#     if i in small:
#         chc += str(small.index(i) + 1) + ' '
#     else:
#         chc += i
# print(chc)

x = int(input())
print('{0:,}'.format(x))