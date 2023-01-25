import random

a = int(input('скока '))
dick = {}
for i in range(a, a*6 + 1):
    dick[i] = 0
for _ in range(1_000_000):
    d = 0
    for _ in range(a):
        d += random.randint(1, 6)
    dick[d] += 1
print(dick)
for i in dick:
    print(i, dick[i], round((dick[i]/1000000) * 100, 2))