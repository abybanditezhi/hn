import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

bets = []
trigger = 'yes'
while trigger == 'yes':
    name = input('imya ')
    stavka = int(input('stavka '))
    temp_bet = {
        'name': name,
        'bet': stavka
    }
    bets.append(temp_bet)


    trigger = input('next? ')

    os.system('cls||clear')

winner = {'name': '',
          'bet': 0,
}
for i in range(len(bets)):
    if bets[i]['bet'] > winner['bet']:
        winner['name'] = bets[i]['name']
        winner['bet'] = bets[i]['bet']
print(f'победитель {winner["name"]} ставка {winner["bet"]}')