import random
import visela
print(visela.intro)

vocabulary = ['Anton', 'Alex', 'Alexandr', 'Arsalan', 'Danil', 'Kirill', 'Sergey', 'Nikolay', 'Nasty', 'Natasha',
              'Ivan', 'Igor', 'Gosha', 'Galina', 'Olya', 'Oksana', 'Oleg', 'James', 'Bill']
word_answer = random.choice(vocabulary).lower()
word_display = []
for _ in range(len(word_answer)):
    word_display.append('_')
print(word_display)
life = 6
counter = 0
print(word_answer)

while life > 0 and counter != len(word_answer):
    print(visela.stages[life])
    letter = input('bukvu: ')
    letter_b = False
    for i in range(0, len(word_answer)):
        if letter == word_answer[i]:
            if word_display[i] != '_':
                letter_b = True
            else:
                word_display[i] = letter
                letter_b = True
                counter += 1
    if letter_b == False:
        life -= 1
    print(word_display)

if counter == len(word_answer):
    print('ай сауууу лев тигрррррррррррррррррр🦁')
else:
    print(visela.stages[life])
    print('бездарь фууууууууууу')