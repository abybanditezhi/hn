# s1 = {1, 2, 3}
# s2 = {1, 3}
# s3 = {0, 1, 2, 3}
# g = {4, 5}
#
# if s2 < s1:
#     print('pod')
#
# p1 = {'python', 'C#', 'Java'}
# p2 = {'Yoptascript', 'Kotlin', 'BrainFuck', 'C++', 'python'}
#
# if p1 < p2:
#     print('йавы')
# elif p2 < p1:
#     print('sfs')
# else:
#     print('fghjkl')

# def tinker():
#     print('tinkerin about')
#     print('tinkerin')
#     print('tinker')
#     print('tink')
#     print('t')
# tinker()


# def calc(numb, stepen):
#     return  numb ** (1 / stepen)
#
#
# print(calc(int(input()), int(input())))

# l = [0, 1, 2]
# # def is_sorted(l):
# #     if sorted(l) == l:
# #         return True
# #     else:
# #         return False
# # print(is_sorted(l))

# def pudge(words):
#     g = []
#     for i in words:
#         g.append(len(i))
#     maxi =  max(g)
#     boobs = g.index(maxi)
#     return words[boobs]
#
# s = ['mama', 'tinker', 'techies']
# print(pudge(words = s))


# def abduros_obebos(s):
# #     mini, maxi = s[0], s[0]
# #     for i in s:
# #         if i > maxi:
# #             maxi = i
# #         elif i < mini:
# #             mini = i
# #     return {'максимум': maxi, 'минимум': mini}
# # l = [5, 6, 2, 9, 234568]
# # print(abduros_obebos(s = l))


# def momchik(l1, l2):
#     if len(l1) != len(l2):
#         if len(l1) > len(l2):
#             for i in range(len(l2)):
#                 l1[i] += l2[i]
#             return l1
#         else:
#             for i in range(len(l1)):
#                 l2[i] += l1[i]
#             return l2
#
#
# lst1 = [10, 20, 30, 40, 50]
# lst2 = [5, 6, 7]
# print(momchik(l1 = lst1, l2 = lst2))


def batya(numb):
    for i in range(2, numb+1):
        if i == numb:
            return True
        if numb % i == 0:
            break


s = int(input())
print(batya(numb = s))