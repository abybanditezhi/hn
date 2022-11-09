import random
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

print(logo)

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
hand_p = [random.choice(cards)]
hand_c = [random.choice(cards)]
score_p = 0
score_c = 0
get_card = 'y'

while get_card == 'y':
    hand_p.append(random.choice(cards))

    if sum(hand_p) > 21 and 11 in hand_p:
        for i in range(0, len(hand_p)):
            if hand_p[i] == 11:
                hand_p[i] = 1
                break
    score_p = sum(hand_p)
    print(f'твоя рука: {hand_p}. Очков {score_p}')
    print(f'первая карта дилера: {hand_c[0]}')
    if score_p > 21:
        get_card = 'n'
    else:
        get_card = input('добираем карту? y - да, n - нет\n'
                         '-----> ')

while sum(hand_c) < 17:
    hand_c.append(random.choice(cards))
    if sum(hand_c) > 21 and 11 in hand_c:
        for i in range(0, len(hand_c)):
            if hand_c[i] == 11:
                hand_c[i] = 1
                break

score_c = sum(hand_c)

print('======================' * 2)
print(f'итоговая рука дилера: {hand_c}. Очков {score_c}')
print(f'твоя рука: {hand_p}. Очков {score_p}')

if score_p > 21 and score_c > 21:
    print('ничья. перелетели братья')
elif score_p > 21:
    print('перелетел брат, проиграл(((')
elif score_c > 21:
    print('ахахахах дилер лох перелетел. братан ты выиграл')
elif score_p > score_c:
    print('изи изи бро ты выиграл')
elif score_c == score_p:
    print('ничья')
else:
    print('жалко тебя(( ты уже в тильте?')