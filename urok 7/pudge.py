# ZeroDivisionError: division by zero
# x = 7 / 0

# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# x = 15 + 'a'

# IndexError: list index out of range
# x = [0, -55, 'pyat']
# print(x[3])

# SyntaxError: unterminated string literal (detected at line 11)
# x = 'privet fdsgdgs

# ValueError: invalid literal for int() with base 10: 'a'
# int('a')

# NameError: name 'x' is not defined
# print(x)


#assert
# def nhgnh(x):
#     return sum(x)
#
# assert nhgnh([1, 2]) == 3
# AssertionError
# assert nhgnh([1, 2]) == 4

# try:
# #     x = int(input())
# #     sum = 5/x
# # except ValueError:
# #     print('/a???????????')
# # # except Exception:
# # #     print('a')
# # else:
# #     print('kakoy krutoy')
# # finally:
# #     print('skr skr')

# lst = []
# try:
#     f = open('file.txt')
#
# except FileNotFoundError:
#     print('gde')
# else:
#     try:
#         for line in f:
#             lst.append(int(line))
#     except ValueError:
#         print('я в тильте')
#     else:
#         print('ok')
#     finally:
#         f.close()
# print(lst)

# try:
#     x = 5/0
# except ZeroDivisionError as error_message:
#     print(error_message)


# x = input().lower().strip()
# try:
#     if x == 'антон':
#         raise Exception('ты уже в тильте?')
# except Exception:
#     print('да')

# try:
#     x = 5/0
# except ZeroDivisionError:
#     pass