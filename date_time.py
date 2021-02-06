from datetime import date
from datetime import datetime


def main():
    today = date.today()
    print('Today's date is', today)

    print('Date components', today.day, today.month, today.year)
    print('Weekday number', today.weekday())
    days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
    print('Which is a', days[today.weekday()])

    print('Current datetime:', datetime.now())
    print('Current time:', datetime.time(datetime.now()))


if __name__ == '__main__':
    main()
