import json
import requests
# salad = {
#     "Помидоры": [5, "Порезать"],
#     "Огурцы": [3, "Проверить на горькость", "Порезать"],
#     "Соль": "По вкусу",
#     "Сахар": False
# }
# json.dump(salad, f, ensure_ascii=False)
# f = open('data.json', 'r', encoding='utf-8')
# a = json.load(f)
# print(a)
# f.close()

# f = open('file.txt', 'r', encoding='utf-8')
# a = f.readlines()
# print(a)
# f.close()
# d = {}
# for i in a:
#     k = i.split(': ')
#     d[k[0]] = k[1].rstrip('\n')
# print(d)
# b = open('data.json', 'w', encoding='utf-8')
# json.dump(d, b, ensure_ascii=False)
# b.close()

# b = open('data.json', 'r', encoding='utf-8')
# a = json.load(b)
# b.close()
# for i, j in enumerate(a):
#     c = type(j)
#     if c == str:
#         a[i] += '!'
#     elif c == int or c == float:
#         a[i] += 1
#     elif c == bool:
#         a[i] = not a[i]
#     elif j == None:
#         a.pop(i)
#     elif c == list:
#         a[i] += a[i]
#     elif c == dict:
#         a[i]['newkey'] = None
# print(a)

a = requests.get(url='http://api.open-notify.org/iss-now.json')
data = a.json()['iss_position']
print(data)
print(f'{data["latitude"]} широта')
print(f'{data["longitude"]} долгота')