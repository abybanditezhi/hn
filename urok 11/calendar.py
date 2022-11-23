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
print(cal_text)
weekSeeparator = ('+----------' * 7 + '\n')
blankRow = ('          ' * 7 + '|\n')