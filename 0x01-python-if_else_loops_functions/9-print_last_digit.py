#!/usr/bin/python3
def print_last_digit(number):
    digits = str(number)
    ldigit = digits[-1:]
    ldigit = int(ldigit)
    print(ldigit, end="")
    return ldigit
