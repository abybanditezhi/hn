from gmtr import box_close, box_empty, box_carrot
from random import choice
def generate_boxes(s1, s2):
    res = ''
    if s1 == 'ПУСТОТА':
        box1 = box_empty.format(COLOR1.center(13)).split('\n')
    elif s1 == 'МОРКОВКА':
        box1 = box_carrot.format(COLOR1.center(13)).split('\n')
    else:
        box1 = box_close.format(COLOR1.center(13)).split('\n')
    if s2 == 'ПУСТОТА':
        box2 = box_empty.format(COLOR2.center(13)).split('\n')
    elif s2 == 'МОРКОВКА':
        box2 = box_carrot.format(COLOR2.center(13)).split('\n')
    else:
        box2 = box_close.format(COLOR2.center(13)).split('\n')

    for j in zip(box1, box2):
        res += '   '.join(j) + '\n'
    res += p1Name[:10].center(13) + ' ' * 7 + p2Name[:10].center(13) + '\n'
    return res


COLORS = ['ФИОЛЕТОВАЯ', 'КАЙФОВАЯ', 'МАГАДAНСКАЯ', 'УНЫЛАЯ']
COLOR1 = choice(COLORS)
COLOR2 = choice(COLORS)
while COLOR1 == COLOR2:
    COLOR2 = choice(COLORS)






p1Box = 'ЗАКРЫТО'
p2Box = 'МОРКОВКА'

p1Name = input('1st player ')
p2Name = input('2nd player ')
while p1Name.strip() == '':
    p1Name = input('1st player ')
while p2Name.strip() == '':
    p2Name = input('2nd player ')

print(generate_boxes('ПУСТОТА', 'g'))

while True:
    print(f'{p2Name} в твоей коробке {p2Box}')

    action = input(f'нужно выбрать\n'
                   f'1 блеф: сказать что в коробке {p1Box}\n'
                   f'2 правда: сказать что в коробке {p2Box}\n'
                   f'(б - блеф, п - правда)').lower()
    while action != 'Б' and action != 'П':
        action = input(f'нужно выбрать\n'
                       f'1 блеф: сказать что в коробке {p1Box}\n'
                       f'2 правда: сказать что в коробке {p2Box}\n'
                       f'(б - блеф, п - правда)').lower()
    print('\n' * 70)
    input(f'{p1Name} открывает глаза(ЭНТЕР)...')
    if action == 'Б':
        print(f'{p2Name} сообщает, что в его коробке {p1Box}')
    else:
        print(f'{p2Name} сообщает, что в его коробке {p2Box}')