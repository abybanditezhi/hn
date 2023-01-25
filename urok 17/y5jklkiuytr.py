import time
import random

input('нажмите ентер чтобы начать')

def igra(mt):
    while True:
        time.sleep(random.randint(1, 3))
        starttime = time.time()
        input('стреляй')
        lasttime = starttime
        laptime = round(time.time() - lasttime, 5)
        if  mt - 0.02 < laptime < mt + 0.02:
            print('выиграл')
            b = 'win'
        else:
            print('проиграл')
            b = 'lose'
        print(laptime)
        with open('mama.txt', 'a') as f:
            f.write(str(laptime) + f' {b}\n')
        a = input('да или нет ').lower()
        if a == 'да':
            continue
        else:
            break
print(igra(0.5))