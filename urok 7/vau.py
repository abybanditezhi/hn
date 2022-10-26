import random
while True:
    print("Угадай число")
    try:
        diff = int(input('введи макс число для угадывания '))
        if diff < 1:
            raise Exception
    except Exception:
        print(' число > 0')
        continue
    mini = 0
    maxi = diff
    computer_number = random.randint(0, diff)
    life = 7
    while life > 0:
        try:
            user_number = int(input("Введи число: "))
        except ValueError:
            print('ты в тильте бро')
            continue
        else:
            if user_number < 0 or user_number > diff:
                print(f"Введи число от 0 до {diff}")
                continue
            if computer_number == user_number:
                print("Вы победили!")
                break
            elif computer_number < user_number:
                print("Нужно меньше.")
                maxi = user_number
            else:
                print("Нужно больше.")
                mini = user_number
            print(f">>> Интервал: {mini} – {maxi}")
            life = life - 1
            print("❤️:", life)
    answer = input("Хочешь продолжить?")
    if answer == "Да":
        continue
    else:
        break