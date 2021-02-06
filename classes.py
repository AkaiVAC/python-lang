
from typing import no_type_check


class myClass:
    def method1(self):
        print('myClass method1')

    def method2(self, someString):
        print('myClass method2 says:', someString)


class myOtherClass(myClass):
    def method1(self):
        myClass.method1(self)
        print('myOtherClass method1')

    def method2(self, someString):
        print('myOtherClass method2 says:')


def main():
    c = myClass()
    c.method1()
    c.method2('YOLO!')

    c2 = myOtherClass()
    c2.method1()
    c2.method2('YOLO!')


if __name__ == '__main__':
    main()
