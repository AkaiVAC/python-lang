class TestFiles():
    def __init__(self, name='text.txt'):
        self.file_name = name
        self.create_file()
        self.append_file()
        self.read_file_by_line()

    def create_file(self):
        open(self.file_name, 'w+').close()

    def append_file(self):
        self.create_file()
        f = open(self.file_name, 'a')
        for i in range(10):
            f.write('This is line ' + str(i) + '\n')
        f.close()

    def read_file(self):
        f = open(self.file_name, 'r')
        if f.mode == 'r':
            contents = f.read()
            print(contents)
        f.close()

    def read_file_by_line(self):
        f = open(self.file_name, 'r')
        if f.mode == 'r':
            fl = f.readlines()
            for l in fl:
                print(l)
        f.close()


if (__name__ == '__main__'):
    TestFiles()
