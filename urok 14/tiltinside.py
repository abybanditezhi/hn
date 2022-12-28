# text = input().lower()
# s = list('!,.?')
# d = {}
# text_clear = ''
# for i in text:
#     if i not in s:
#         text_clear += i
#
# text_prepared = text_clear.split()
# print(text_prepared)
#
# for j in text_prepared:
#     if j not in d:
#         d[j] = 1
#     else:
#         d[j] += 1
# print(d)

# d = {'бананы': 50,
#      'богдан': 999,
#      'чипсы': 0.5}
# ass = 0
# for i in d.values():
#     ass += i
#
# print(ass)
#
# DIE_SIDES = 6
# DIES = 2
# dd = {}
#
# for i in range(1, DIE_SIDES+1):
#     for j in range(1, DIE_SIDES+1):
#         if i + j not in dd:
#             dd[i+j] = [(i, j)]
#         else:
#             dd[i + j].append((i, j))
# for i in dd:
#     print(f'{i}: {dd[i]}')

# text = input().lower()
# s = list('!,.?')
# d = {}
# text_clear = ''
# for i in text:
#     if i not in s:
#         text_clear += i
#
# text_prepared = text_clear.split()
# print(text_prepared)
#
# for j in text_prepared:
#     if j not in d:
#         d[j] = 1
#     else:
#         d[j] += 1
# maxi = max(d.values())
# print(maxi)
# for i, j in d.items(): #("ветер", 2) key = 'ветер', value = 2
#     if j == maxi:
#         print(f'{i} | {j}')
#         break

# dict = {'k1': 1,
#         'k2': 2,
#         'k3': 3,
#         'k4': 4,
#         'k5': 5}
# a = dict['k1']
# dict['k1'] = dict['k5']
# dict['k5'] = a
# del dict['k2']
# dict['new_key'] = 'new_value'
# print(dict)