# x = int(input())
# if x <= 7:
#     print('skr')
# else:
#     print('da')
# print(x == 7)


# x = int(input())
# if x > 0:
#     print('+')
# elif x < 0:
#     print('-')
# else:
#     print('=')

# year = int(input())
#
# if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
#     print('vis')
# else:
#     print('nevis')

# number1 = float(input('pervoe: '))
# oper = input('operacia(+ - * / ** abs): ')
# number2 = float(input('vtoroe: '))
#
# list = ['+', '-', '*', '/', '**', 'abs']
# if oper in list:
#     if oper == '-':
#         print(number1 - number2)
#     elif oper == '+':
#         print(number1 + number2)
#     elif oper == '*':
#         print(number1 * number2)
#     elif oper == '**':
#         print(number1 ** number2)
#     elif oper == 'abs':
#         print(abs(number1), abs(number2))
#     else:
#         print(number1 / number2)
# else:
#     print('ya te na russkom napisal boksmaster ti shtopanniy')

# num1 = int(input('pervoe: '))
# num2 = int(input('vtoroe: '))
# num3 = int(input('tretie: '))
# count_pol = 0
# count_otr = 0
#
# if num1 < 0:
#     count_otr += 1
# elif num1 > 0:
#     count_pol += 1
#
# if num2 < 0:
#     count_otr += 1
# elif num2 > 0:
#     count_pol += 1
#
# if num3 < 0:
#     count_otr += 1
# elif num3 > 0:
#     count_pol += 1
# print(f'полож {count_otr} отр {count_pol}, это что за хук?!?!?!?!??!?!?!?')

# list = [num1, num2, num3]
# print('max', max(list))
# print('min', min(list))


# hours = int(input('hours '))
# minutes = int(input('minutes '))
# seconds = int(input('seconds '))
#
#
# if (hours < 24 and hours > 0) or hours == 0:
#     if (minutes < 60 and minutes > 0) or minutes == 0:
#         if (seconds < 60 and seconds > 0) or seconds == 0:
#             print(f'время {hours}:{minutes}:{seconds}')
# else:
#     print('slabi')

# ticket = input('nomer (6 cifr) ')
# if len(ticket) == 6 and ticket.isdigit():
#     fir = ticket[:3]
#     sec = ticket[3:6]
#     firs = int(fir[0]) + int(fir[1]) + int(fir[2])
#     sesc = int(sec[0]) + int(sec[1]) + int(sec[2])
#     if firs == sesc:
#         print('mechta')
#     else:
#         print('lox')
# else:
#     print('ti dayn?')

# month = int(input('mesyac (po schetu) '))
# if month > 0 and month < 13:
#     if month >= 1 and month < 3:
#         print('zima')
#     elif month >= 3 and month < 6:
#         print('vesna')
#     elif month >= 6 and month < 9:
#         print('leto')
#     elif month >=9 and month < 12:
#         print('osen')
#     else:
#         print('zima')
# else:
#     print('ti na ugare?')

# homyaks = int(input('homyaki: '))
#
# if 11 <= homyaks <= 19:
#     print(homyaks, 'хомяков')
# elif homyaks % 10 == 1:
#     print(homyaks, 'хомяк')
# elif 2 <= homyaks % 10 <= 4:
#     print(homyaks, 'хоямка')
# else:
#     print(homyaks, 'хомяков')