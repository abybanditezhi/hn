from klass import Sounds

sound = Sounds()
while True:
    sound.play()
    b = input().lower()
    sound.corin(x=b)
    if b.strip() == '':
        break