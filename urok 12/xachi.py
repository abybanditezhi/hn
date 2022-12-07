from collections import namedtuple
citizen = namedtuple('житель', 'имя возраст статус')
alex = citizen(имя='леха алексеев', возраст="27", статус="бездарь")
print(alex.имя)
print(alex)