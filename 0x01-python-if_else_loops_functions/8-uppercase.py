#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            u = ord(c) - 32
        else:
            u = ord(c)
        print("{0}".format(chr(u)), end="")
    print("".format())
