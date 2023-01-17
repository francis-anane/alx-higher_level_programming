#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digits = str(number)
ldigit = digits[-1:]

if number < 0:
        ldigit = "-" + ldigit

if int(ldigit) > 5:
    print(f"Last digit of {number} is {ldigit} and is greater than 5")
elif int(ldigit) == 0:
    print(f"Last digit of {number} is {ldigit} and is 0")

elif (int(ldigit) < 6) and (int(ldigit) != 0):
    print(f"Last digit of {number} is {ldigit} and is less than 6 and not 0")
