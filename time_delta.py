from datetime import date, datetime, timedelta

print(timedelta(days=365, hours=5, minutes=1))

now = datetime.now()
print('today is:', str(now))
print('One year from now:', str(now + timedelta(days=365)))
print('In 2 days and 3 weeks:', str(now + timedelta(days=2, weeks=3)))

t = now - timedelta(weeks=1)
s = t.strftime('%A %B %d, %Y')
print('One week ago it was:', s)


today = date.today()
april_fools_day = date(today.year, 4, 1)

if april_fools_day < today:
    print('April Fool\'s day already went by % d days ago' %
          ((today-april_fools_day).days))
    april_fools_day = april_fools_day.replace(year=today.year+1)

time_to_april_fools_day = april_fools_day - today
print('It\'s just', time_to_april_fools_day, 'until April Fool\'s day')
