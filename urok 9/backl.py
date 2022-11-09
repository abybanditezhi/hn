import random
length = 3
life = 20
answer = random.randint(100, 999)
answer = str(answer)
answer = list(answer)

# print(answer)


while life:
    is_guessed = False
    print('=' * 10)
    print('жизней', end=' ')
    for _ in range(0, life):
        print('❤', end='')
    print()
    guess = input('введи число бро:\n'
                  '------> ')
    if len(guess) != 3 or not guess.isdigit():
        print('ты в тильте брат? ты че написал. переписывай')
        continue

    if list(guess) == answer:
        print('АЙ САУУУУУУУУУУ БРАТАН')
        is_guessed == True
        break
    if not is_guessed:
        for i in range(0, length):
            if guess[i] == answer[i]:
                print('ба ма шеги ба))')
                is_guessed = True
                break
    if not is_guessed:
        for j in guess:
            if j in answer:
                print('чо за фермент???7?')
                is_guessed = True
                break
    if not is_guessed:
        print('принглс((((((9(((9((')
    life -= 1
print(answer)