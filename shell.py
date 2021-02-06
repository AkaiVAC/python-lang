import os
from os import path
from files import Files
import shutil
from shutil import make_archive
from zipfile import ZipFile


def main():
    file_name = 'text.txt'
    if path.exists(file_name) == False:
        Files().create_test_file(file_name)

    src = path.realpath(file_name)
    dst = src+'.bak'
    shutil.copy(src, dst)
    shutil.copystat(src, dst)

    root_dir, tail = path.split(src)
    shutil.make_archive('archive', 'zip', root_dir)

    with ZipFile('text_zip.zip', 'w') as newzip:
        newzip.write(file_name)
        newzip.write(file_name+'.bak')


if(__name__ == '__main__'):
    main()
