def func1():
    print('This is a function')


def func2(arg1, arg2):
    print(arg1, ' ', arg2)


def cube(x):
    return (x*x*x)


def power(num, x=1):
    res = 1
    for i in range(x):
        res = res*num
    return res


def multi_add(*args):
    res = 0
    for x in args:
        res = res+x
    return res


func1()
print(func1())
print(func1)

func2('Arun', 'Chithambaram')
print(func2('Arun', 'Chithambaram'))
print(cube(20))

print(power(2))
print(power(2, 3))
print(power(x=3, num=2))

print(multi_add(1, 2, 3))
