import easygui
# print(ord('а'))
# print(chr(1072))

# c = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# c2 = c[::-1]
# y = ''
# phrase = input('slovo ')
# for i in phrase:
#     y += c2[c.index(i)]
#
# print(phrase)
# print(y)

# a = input('sovo ')
# n = int(input('sdvig '))
#
# fraz = ''
# for i in a:
#     fraz += chr(ord(i)+n)
# print(fraz)

# a = input('pishi ')
# n = int(input('sdvig '))
# hj = ''
# c = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# for i in a:
#     d = c.index(i)
#     d = (d + n) % 33
#     hj += c[d]
# print(hj)

c = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'.upper()
fraz = 'ЫНУЪЫ, УЧЫЧЩДТ ЮЧЫНФЧЪЕ ЙД АЫЧЙД ЩИРЛИМИФС...'
slovo = 'ТЕКСТ'
frazer = ''

for i in fraz:
    if i in c or i == ' ':
        frazer += i
mas = frazer.split(' ')
for shift in range(1, 33):
    mama = ''
    for letter in slovo:
        d = c.index(letter)
        d = (d+shift) % 33
        mama += c[d]
    if mama in mas:
        print('sdvig ', shift)
        break