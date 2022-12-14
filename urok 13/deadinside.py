# set() - преобразование в множества
# myset = {'a', 'b', 'c'} # неупорядочные тип данных
# print(myset)

# set1 = {1, 2, 3, 4, 5}
# set2 = {3, 4, 5, 6, 7}
# print(set1 | set2) # объединение .union()
# print(set1 & set2) # .intersection() - пересечение
# print(set1 - set2) # разность .difference()
# print(set1 ^ set2) # симмметрическая разность .symmetric.difference()

# dict - {'клчю1' : 1,
#         'ключ2' : 'значение2',
#         'ключ3' : {'влож1' : -1}}

from random import randint
# list = []
# for _ in range(5):
#     list.append(randint(1, 5))
# print(list)
# print(f"{len(set(list))} штук: {set(list)}")
#
# list1 = []
# list2 = []
# for i in range(randint(100, 1000)):
#     list1.append(randint(0, 10000))
#     list2.append(randint(0, 10000))
# un1 = set(list1)
# un2 = set(list2)
# oo = un1 & un2
# print(f'{len(oo)} общих чисел')
# print(i, 'генераций')
# print(min(oo))
# print(max(oo))
# print(sorted(oo))

# list = set()
# vvod = ''
# while vvod != 'end':
#     vvod = input()
#     if vvod.lstrip('-').isdigit():
#         if vvod not in list:
#             print('NO')
#             list.add(vvod)
#         else:
#             print('YES')
#     elif vvod == 'end':
#         break
#     else:
#         print('число')

# lst1 = [0, False, 1 - 1, "один", 2, 3.14]
# lst2 = set(lst1)
# print(lst1)
# print(lst2)
# if len(lst2) != len(lst1):
#     print('повторения есть')
# else:
#     print('повторений нет')

# vvod = 'Я люблю movavi, программирование, а ещё я люблю пельмени!'.lower()
# symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '=', '-', ',', '.', '?', '>', '<', "'", '"', '/', ':', ';']
# a = ''
# for i in vvod:
#     if i not in symbols:
#         a += i
# print(a)
# b = a.split(' ')
# b = set(b)
# print(b)
# print(len(b))

n = int(input())
gen = {}
for _ in range(n):
    child, parent = input().upper().split()
    if parent not in gen:
        gen[parent] = [child]
    else:
        gen[parent].append(child)
print(gen)