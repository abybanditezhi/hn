# a = int(input('1 число: '))
# b = int(input('2 число: '))
# lst = []
# for i in range(a+1, b):
#     lst.append(i ** 2)
# print(lst)

# a = input()
# b = a.split(' ')
# b.reverse()
# print(b)

# chet = 0
# nechet = 0
# lst = []
# number = ' '
# while number != 'end':
#     number = input('ввод: ')
#     if number.lstrip('-').isdigit():
#         number = int(number)
#         lst.append(number)
#     elif number == 'end':
#         break
#     else:
#         print('число')
#         continue
#
#     if number % 2 == 0:
#         chet += 1
#     else:
#         nechet += 1
# print(f'четных {chet}')
# print(f'нечетных {nechet}')

# phrase = input()
# lst = phrase.split(' ')
# for i in range(1, len(lst)):
#     if int(lst[i]) > int(lst[i-1]):
#         print(f'я считаю что {lst[i]} больше, чем {lst[i-1]}')

# lst = [-5, 14, 2, -8, 1]
# maxi = max(lst)
# mini = min(lst)
# lst[lst.index(maxi)], lst[lst.index(mini)] = lst[lst.index(mini)], lst[lst.index(maxi)]
# print(lst)
# import random
# count = int(input())
# lst = []
# for _ in range(count):
#     lst.append(random.randint(150, 200))
# lst.sort(reverse=True)
# print(lst
#       )
# peter = int(input('rost '))
# lst.append(peter)
# lst.sort(reverse=True)
# print(lst)
# c = lst[::-1]
# peterpos = len(lst) - c.index(peter)
# print(peterpos)

nums = [4, 5, 6, 7, 8, 9, 10]
step = int(input())
if step < 0:
    step = abs(step)
    for i in range(step):
        nums.append(nums.pop(0))
else:
    for i in range(step):
        nums.insert(0, nums.pop())
print(nums)