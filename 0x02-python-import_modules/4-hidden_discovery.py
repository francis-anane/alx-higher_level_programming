#!/usr/bin/python3
if __name__ == "__main__":

    import hidden_4

    names = dir(hidden_4)

    names = list(names)
    names.sort()

    for name in names:
        if name[0] != "_":
            print(name)
