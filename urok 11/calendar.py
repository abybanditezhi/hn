import datetime
MONTHS = ('январь', "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь")
DAYS = ('понедельник', "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье")

while True:
    year = input('god ')
    if year.isdigit() and int(year) > 0:
        break
while True:
    month = input('month ')
    if month.isdigit() and int(month) > 0:
        year = int(year)
        month = int(month)
        break

cal_text = ''
cal_text += (' ' * 34) + MONTHS[month - 1] + ' ' + str(year) + '\n'
for i in range(7):
    cal_text += DAYS[i] + ' '
cal_text += '\n'
weekSeeparator = ('+----------' * 7 + '\n')
blankRow = ('|          ' * 7 + '|\n')

currentdate = datetime.date(year, month, 1)

while currentdate.weekday() != 0:
    currentdate -= datetime.timedelta(days=1)

while True:
    cal_text += weekSeeparator
    daynumberrow = ''
    for i in range(7):
        daynumberlable = str(currentdate.day).rjust(2)
        daynumberrow += '|' + daynumberlable + (' ' * 8)
        currentdate += datetime.timedelta(days=1)
    cal_text += '|\n'
    cal_text += daynumberrow
    for i in range(3):
        cal_text += blankRow

    if currentdate.month != month:
        break

cal_text += weekSeeparator
print(cal_text)

filename = 'calendar_{}_{}.txt'.format(month, year)
with open(filename, 'w') as file:
    file.write(cal_text)

print('sohraneno v' + filename)