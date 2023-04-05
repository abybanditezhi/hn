# first = input().lower().strip()
# second = input().lower().strip()
# h = ['красный', 'желтый', 'синий']
# if first not in h or second not in h:
#     print('другие цвета выбирай негрила')
# elif (first == h[0] or second == h[0]) and (first == h[1] or second == h[1]):
#     print('оранжевый')
# elif (first == h[0] or second == h[0]) and (first == h[2] or second == h[2]):
#     print('фиолетовый')
# elif (first == h[2] or second == h[2]) and (first == h[1] or second == h[1]):
#     print('зеленый')

# a = input('первый урок ')
# b = int(input('длительность '))
# c = int(input('перемена '))
# d = int(input('скок уроков '))
# e = int(a[:2])
# f = int(a[3:])
# time = e * 60 + f
# for i in range(d):
#     e = time // 60
#     f = time % 60
#     print(f'{i+1} урок: {str(e).rjust(2, "0")}:{str(f).rjust(2, "0")} - ', end='')
#     time += b
#     e = time // 60
#     f = time % 60
#     print(f'{str(e).rjust(2, "0")}:{str(f).rjust(2, "0")}')
#     time += c


# a = int(input('кол-во зомби '))
# b = int(input('скок заражать '))
# c = int(input('скок дней '))
# for i in range(1, c+1):
#     print(f'{i} день: {(a * b) ** i}')
a = input().split(' ')


def abv(a):
    lt = []
    for ind, i in enumerate(a):
        if ind == 0:
            ahs = int(a[-1]) + int(a[ind+1])
        elif ind == len(a) - 1:
            ahs = int(a[ind - 1]) + int(a[0])
        else:
            ahs = int(a[ind - 1]) + int(a[ind+1])
        lt.append(ahs)
    return lt


print(abv(a))
