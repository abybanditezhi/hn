# money = int(input('Введите ваше кол-во денег в рублях: '))
# money *= 100
# cost = int(input('Введите цену в копейках за 1 пирожок: '))
# n = int(input('Введите кол-во: '))
# fincost = cost * n
#
# if money < fincost:
#     print('не хватает бро')
#     nehvatka = (fincost - money) / 100
#     print('Вам не хватает', nehvatka, 'рублей')
# else:
#     if fincost > 100:
#         first = fincost // 100
#         second = (fincost % 100)
#         print('С вас', first, 'рублей и', second, 'копеек' )
#         sdacha = (money - fincost) / 100
#         print('Ваша сдача:', sdacha, 'рублей')
#     elif money <= 100:
#         print('С вас', fincost, 'копеек')
#         sdacha = (money - fincost) / 100
#         print('Ваша сдача:', sdacha, 'рублей')

# time = int(input('Введите кол-во секунд: '))
# hours = time // 3600
# minutes = (time - hours * 3600) // 60
# seconds = (time - hours * 3600) - 60 * minutes
# if hours < 10 and minutes < 10 and seconds < 10:
#     hours = '0' + str(hours)
#     minutes = '0' + str(minutes)
#     seconds = '0' + str(seconds)
#     print(hours, ':', minutes, ':', seconds)
# else:
#     print(hours, ':', minutes, ':', seconds)

# x = input()
# print(len(x))

# name_1 = 'lox'
# name_2 = 'bezdar'
# name_3 = 'nefor'
#
# doteri = [name_1, name_2, name_3]
# print(doteri)
# print(doteri[1][2:])


# path = 'c:/Python3/Python.exe'
# print('Имя файла', path[11:])
# print('Расширение', path[-3:])
# print('Имя каталога', path[3:10])
# print("Полный путь к каталогу", path[:10])

# path = 'c:/Python3/Python.exe'
# temp = path.split('/')
# print('Имя файла', temp[-1])
# print('Расширение', temp[-1][-3:])
# print('Имя каталога', temp[1])
# print("Полный путь к каталогу", temp[0] + '/' + temp[1])

# chapter_1 = input('glava 1: ')
# page_1 = input('stranitsa: ')
# chapter_2 = input('glava 2: ')
# page_2 = input('stranitsa: ')
# chapter_3 = input('glava 3: ')
# page_3 = input('stranitsa: ')
# print(chapter_1.ljust(15) + page_1.rjust(15))
# print(chapter_2.ljust(15) + page_2.rjust(15))
# print(chapter_3.ljust(15) + page_3.rjust(15))


# x = '123456789'
# x[::2]
# x[::-1]
# x[::-2]

# x = '12.345.678'
# temp = x.split('.')  # поумнел
# print(temp[0] + temp[1] + temp[2])

# x = '12.345.678'
# temp = x[:2] + x[3:6] + x[7:] # ну ты бездарь чел фу
# number = int(temp)
# print(number)

# x = '12.345.678'
# temp = x.replace('.', '') # вау вау че как так вау вау чел что это аййййй
# print(temp)