from klasses import Persons
from random import choice


def ofor():
    u = choice(users)
    print(f'Логин: {u.login}')
    print(f'Имя: {u.imya}')
    print(f'Фамилия: {u.falimia}')
    print(f'Посты: {u.posts}')


def session():
    while True:
        ofor()
        print('''[Возможные действия]: 
    - ПОДПИСКИ (посмотреть на кого подписан Ибрагим)
    - ПОДПИСЧИКИ (посмотреть кто подписан на Ибрагима)
    - ПОДПИСАТЬСЯ (стать подписчиком)
    - СЛЕДУЮЩИЙ аккаунт''')
        spros = input('> ').upper()
        if spros == 'ВЫЙТИ':
            break
        elif spros == 'СЛЕДУЮЩИЙ':
            continue


a = Persons()
b = Persons("Чек")
c = Persons('степан', 'пропенко', 'yalox2323', 'jora1337')
users = [a, b, c]
print(ofor())
l = input('скажи логин: ')
p = input('скажи пароль: ')

for i in users:
    if i.log_in(l, p) == True:
        session()
print(a.imya)