import requests
from random import randint


class Persons:

    def __init__(self, imya="", falimia='', login='', parol=''):
        self.__data = requests.get('https://api.randomdatatools.ru/').json()
        self.__lorem = 'Mauris in est non sapien efficitur fringilla ac ut lorem. Morbi eu ante ex. Aenean nec lobortis ex, at efficitur nisl. Praesent eu pellentesque diam, posuere laoreet orci. Cras porta facilisis lacus, et consectetur eros bibendum a. Curabitur maximus ex tincidunt, ornare nisi vitae, venenatis eros. Praesent imperdiet ultricies urna.'
        self.imya = self.__data['FirstName'] if not imya else imya
        # имя = случайному если атрибут ="" (пустоте if not) иначе передаваемое
        self.falimia = self.__data['LastName'] if not falimia else falimia
        self.login = self.__data['Login'] if not login else login
        self.__parol = self.__data['Password'] if not parol else parol
        self.podpiski = []
        self.podpischiki = []
        self.posts = [self.__lorem[randint(1, 20):randint(20, 40)] for i in range(randint(1, 10))]

    def log_in(self, login, parol):
        if self.login == login and self.__parol == parol:
            return True
        else:
            return False