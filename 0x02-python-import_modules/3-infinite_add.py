#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    ac = len(argv)
    num = 0
    if ac > 1:
        i = 1
        for a in argv:
            if i <= ac - 1:
                num = num + int(argv[i])
                i = i + 1
    print(num)
