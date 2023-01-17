#!/usr/bin/python3
for i in range(0, 100):
    if i < 10:
        print("{0}{1},".format(0, i), end=" ")
    elif i > 9 and i < 99:
        print("{0},".format(i), end=" ")
    elif i == 99:
        print(i)
