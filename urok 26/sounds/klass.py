import playsound
from random import choice

class Sounds:
    def __init__(self):
        self.variants = 'zuxuplja'
        self.score = 1
        self.sequence = choice(self.variants)

    def __next(self):
        self.sequence += choice(self.variants)

    def corin(self, x):
        if x == self.sequence:
            self.score += 1
            playsound.playsound('sounds/correct.wav')
            self.__next()
        else:
            self.score -= 0.5
            playsound.playsound('sounds/incorrect.wav')

    def play(self):
        for i in self.sequence:
            playsound.playsound(f'sounds/{i}.mp3')


# playsound.playsound('sounds/correct.wav')
# playsound.playsound('sounds/incorrect.wav')
# playsound.playsound('sounds/z.mp3')
# playsound.playsound('sounds/a.mp3')
# playsound.playsound('sounds/l.mp3')
# playsound.playsound('sounds/y.mp3')
# playsound.playsound('sounds/p.mp3')
# playsound.playsound('sounds/a.mp3')