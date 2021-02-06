f = 0
print(f)

f = '1234'
print(f)

print('asd'+str(123))


def someFunc():
    global f
    f = 'def'
    print(f)


someFunc()
print(f)

del f
