from genericpath import exists
import os
import time
from os import path
from datetime import datetime
from test_files import TestFiles


def main():
    file_name = 'text.txt'

    if (path.exists(file_name) == False):
        TestFiles()

    print(os.name)
    print('Item exists: ' + str(path.exists(file_name)))
    print('Item is a file: ' + str(path.isfile(file_name)))
    print('Item is a directory: ' + str(path.isdir(file_name)))
    print('Item path: ' + str(path.realpath(file_name)))
    print('Item path: ' + str(path.split(path.realpath(file_name))))
    print('Modification time: ' + time.ctime(path.getmtime(file_name)))
    td = datetime.now() - datetime.fromtimestamp(path.getmtime(file_name))
    print('It has been ' + str(td) + ' since the file was modified')
    print('Or ' + str(td.total_seconds()) + ' seconds')


if __name__ == '__main__':
    main()
