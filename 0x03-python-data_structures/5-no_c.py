#!/usr/bin/python3
def no_c(my_string):
    new = ''
    for i in my_string:
        if ord(i) == 67 or ord(i) == 99:
            continue
        new += i

    return new
