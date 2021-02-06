def main():
    x, y = 1000, 100
    if (x < y):
        st = 'x is less than y'
    elif (x == y):
        st = 'x is equal to y'
    else:
        st = 'x is greater than y'
    print(st)

    st = 'x is less' if (x < y) else 'x is more'
    print(st)


if __name__ == '__main__':
    main()
