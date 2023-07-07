#!/usr/bin/python3
"""This module prints the ASCII alphabet,
in reverse order, alternatinglowercase and
uppercase (z in lowercase and Y in uppercase) , not followed by a new line.
"""

i = 0
for c in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(c - i)), end="")
    if i == 0:
        i = 32
    else:
        i = 0
