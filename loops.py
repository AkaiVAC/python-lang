

def main():
    x = 0
    while (x < 5):
        print(x)
        x = x+1

    for x in range(5, 10):
        print(x)

    days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
    for x in (days):
        print(x)

    for x in range(5, 10):
        if (x == 7):
            break
        print(x)

    for x in range(5, 10):
        if (x % 2 == 0):
            continue
        print(x)

    for i, x in enumerate(days):
        print(i, x)


if __name__ == '__main__':
    main()
