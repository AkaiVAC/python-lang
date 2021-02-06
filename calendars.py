import calendar
from datetime import date


c = calendar.TextCalendar(calendar.MONDAY)
st = c.formatmonth(2021, 2, 0, 0)
print(st)

html_cal = calendar.HTMLCalendar(calendar.MONDAY)
st = html_cal.formatmonth(2021, 2)
print(st)

for i in (c.itermonthdays(2021, 2)):
    print(i)

for name in calendar.month_name:
    print(name)
print('\n')
for name in calendar.day_name:
    print(name)

print('Team meetings will be on:')

for m in range(1, 13):
    cal = calendar.monthcalendar(2021, m)
    weekone = cal[0]
    weektwo = cal[1]

    if weekone[calendar.FRIDAY] != 0:
        meetday = weekone[calendar.FRIDAY]
    else:
        meetday = weektwo[calendar.FRIDAY]

    print('%10s %2d' % (calendar.month_name[m], meetday))

today = date.today()
bday = date(today.year, 7, 1)
diff = (bday-today).days
if diff > 0:
    print('Birthday in %d days' % diff)
else:
    print('Birthday in %d days' % (diff+365))

days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
print('Tomorrow will be a:', days[(today.weekday()+1) % 7])
