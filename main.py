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

