#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    length = len(argv)
    print('{}'.format(length - 1), end=' ')

    if length == 1:
        print('arguments.')
    elif length == 2:
        print('argument:')
    else:
        print('arguments:')

    for i in range(1, length):
        print('{}: {}'.format(i, argv[i]))
