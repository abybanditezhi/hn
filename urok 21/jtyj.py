# try:
#     x = int(input('vvedi '))
#     print(x)
# except (ValueError, IndexError):
#     print('iiiiiiiiii')
# # except IndexError:
# #     print('eqd')
# else:
#     print('aaa')
# finally:
#     print('s')

# x = input()
# try:
#     if x == 'stas':
#         raise ZeroDivisionError()
# except ValueError as msg:
#     print('gdfg', msg)
# sum = 0
# count = 0
# f = open('stas.txt', 'r', encoding='utf-8')
# x = f.read().split()
# for i in x:
#     try:
#         j = int(i)
#     except ValueError:
#         print(f'{i} skip')
#         continue
#     else:
#         count += 1
#         sum += j
# print(sum / count)
# f.close()
# maxi = -1
# try:
#     f = open('stas.txt', 'r', encoding='utf-8')
# except FileNotFoundError:
#     print('faila net')
#     quit()
# text = f.readlines()
# f.close()
# 
# 
# for i, element in enumerate(text):
#     text[i] = element.split()
# 
# for student in text:
#     try:
#         if int(student[3]) > maxi:
#             maxi = int(student[3])
#     except IndexError:
#         print('netu')
#         continue
#     except ValueError:
#         print('bukvi')
# print(maxi)
# try:
#     f = open('stas.txt', 'r', encoding='utf-8')
# except FileNotFoundError:
#     print('файла нет')
#     quit()
# a = f.read()
# f.close()
# b = input('введи слово ')
# n = a.count(b)
# print(n)

try:
    f = open('stas.txt', 'r', encoding='utf-8')
except FileNotFoundError:
    print('файла нет')
    quit()
a = f.read().split()
n = 1
for i in a:
    try:
        n *= int(i)
    except ValueError:
        print(f'{i} не число')
        continue
print(n)
f.close()