#!/usr/bin/python3
for i in range(48, 58):
    for j in range(48, 58):
        if i != j and i < j:
            print("{0}{1}".format(chr(i), chr(j)), end="")
            if j == 57 and i == 56:
                break
            print(",".format(), end=" ")
print("".format())
