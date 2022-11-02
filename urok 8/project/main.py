import additional
import random

print(additional.logo)
is_game = True
score = 0
data = additional.data
while is_game:
    a = random.choice(data)
    b = random.choice(data)
    while a == b:
        b = random.choice(data)
    print('счет:', score)
    print('------------------------------')
    print(f'A: {a["name"]}. {a["description"]}. из {a["country"]}')
    print(additional.vs)
    print(f'B: {b["name"]}. {b["description"]}. из {b["country"]}')
    select = input('у кого больше?? (A, B)\n'
                   '------> ').upper().strip()
    if select == 'A' or select == "B":
        if a['follower_count'] > b['follower_count'] and select == 'A':
            score += 1
        elif a['follower_count'] < b['follower_count'] and select == 'B':
            score += 1
        else:
            print('ты уже в тильте?')
            is_game = False
    else:
        print('ну я в тильте бро')
        quit()