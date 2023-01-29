#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    ac = len(argv)
    if ac < 2:
        print("0 arguments.")
    elif ac == 2:
        print("1 argument:")
        print("1: {0}".format(argv[1]))
    elif ac > 2:
        print("{0} arguments:".format(ac-1))
        i = 1
        for a in argv:
            if i <= ac - 1:
                print("{0}: {1}".format(i, argv[i]))
                i = i + 1
