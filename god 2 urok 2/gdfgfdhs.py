# lst = [1, 2, 3, 4, 5]
# print(sum(lst))
# print(min(lst))
# print(max(lst))
# a = sorted(lst)
# print(f'min {a[0]}, max {a[-1]}')

# f = 'Тетради Ус Москва обнимать?!'
# print(f'{f[3:16:3]}{f[-5:-2]}')

# l = [1, 2, 2, 3, 1, 4]
# for i in l:
#      if l.count(i) > 1:
#          l.remove(i)
# print(l)

# lst = [1, 3.14, 2, 'бабабабаб']
# dcc = {}
# for i in lst:
#     if type(i) not in dcc:
#         dcc[type(i)] = 1
#     else:
#         dcc[type(i)] += 1
# print(dcc)

# lst = [1, 4, 5, 6]
# lst2 = [2, 7]
# print(sorted(lst + lst2))

# x = input().lower()
# l = '1234567890.,?!: ()'
# d = {}
# for i in x:
#     if i in l:
#         continue
#     else:
#         if i in d:
#             d[i] += 1
#         else:
#             d[i] = 1
# print(d)

# import string
# bol = string.ascii_uppercase
# mal = string.ascii_lowercase
# d = {}
# for i in range(len(mal)):
#     d[mal[i]] = bol[i]
# print(d)

# c = 0
# while True:
#     x = input().lower().split(' ')
#     if x[0] == 'zero':
#         c = 0
#     elif 'add' in x:
#         c += int(x[1])
#     elif x[0] == 'result':
#         print(c)
#     elif x[0] == 'exit':
#         break
#     elif 'div' in x:
#         c //= int(x[1])
#     elif 'mul' in x:
#         c *= int(x[1])
#     elif 'minus' in x:
#         c -= int(x[1])

c = 0
dd = {'add': lambda x: c + x,
      'mul': lambda x: c * x,
      'minus': lambda x: c - x,
      'div': lambda x: c // x,
      }
while True:
    vvod = input().split()
    if len(vvod) == 1:
        vvod = vvod[0]
        if vvod == 'exit':
            break
        elif vvod == 'result':
            print(c)
        elif vvod == 'zero':
            c = 0
    else:
        c = dd[vvod[0]](int(vvod[1]))