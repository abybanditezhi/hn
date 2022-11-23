import random
import datetime

while True:
    n = input('скок др до 70 ')
    if not n.isdigit() or int(n) > 70 or int(n) < 2:
        print('ты уже в тильте?')
        continue
    else:
        n = int(n)
        break

lst = []
start = datetime.date(2022, 1, 1)
for _ in range(n):
    shift = random.randint(0, 364)
    shift_day = datetime.timedelta(shift)
    btd = start + shift_day
    lst.append(btd)
for i in range(n):
    print(f'{i+1}) {lst[i]} ')

print('=================================')
for i in set(lst):
    if lst.count(i) > 1:
        print(f'- {i.strftime("%d.%m.%y")} встречается {lst.count(i)} раза')
