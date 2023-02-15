# f = open('восьмой бэ дежурный класс.txt', 'w', encoding='utf-8')
# f.write('тинкерин\nэбаут')
# f.close()

# f = open('восьмой бэ дежурный класс.txt', 'r', encoding='utf-8')
# print(f.read())
# t1 = f.readlines()
# print(t1)
# for line in t1:
#     print(line.rstrip())

# a = input('введи имя файла ')
# f = open(a, 'w', encoding='utf-8')
# b = input('введи фразу ')
# c = b.split()
# print(c)
# for i in c:
#     print(i)
#     f.write(i + '\n')
# print('файл записан')

# f = open('papa.txt', 'r', encoding='utf-8')
# b = f.readlines()
# n = 0
# while b != []:
#     d = b[:3]
#     n += 1
#     del b[:3]
#     artem = open(f'{n}.txt', 'w', encoding='utf-8')
#     for i in d:
#
#         artem.write(i)
#     artem.close()

# f = open('papa.txt', 'r', encoding='utf-8')
# b = f.readlines()
# n = int(input('vvedi '))
# d = b[len(b) - n:]
# for i in d:
#     print(i.rstrip())

a = []
f = open('papa.txt', 'r', encoding='utf-8')
g = open('mama.txt', 'r', encoding='utf-8')
d = f.readlines()
a.append(d)
f.close()
c = g.readlines()
a.append(c)
g.close()
h = open('sin.txt', 'w', encoding='utf-8')
print(a)
for i in a:
    print(i)
    # h.write(i)
h.close()
