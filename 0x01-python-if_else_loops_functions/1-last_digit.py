#!/usr/bin/python3
import random
import math
number = random.randint(-10000, 10000)
lastNum = number % 10 if number > 10 else number % -10
if lastNum > 5:
    print(f"Last digit of {number} is {lastNum} and is greater than 5")
elif lastNum < 6 and lastNum != 0:
    print(f"Last digit of {number} is {lastNum} and is less than 6 and not 0")
elif lastNum == 0:
    print(f"Last digit of {number} is {lastNum} and is 0")
