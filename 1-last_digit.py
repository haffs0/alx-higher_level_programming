#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
positive_number = 0
check = 0
if number < 0:
    positive_number = -1 * number
    check = (positive_number % 10) * -1
else:
    positive_number = number
    check = positive_number % 10
if check > 5:
    print(f"Last digit of {number} is {check} and is greater that 5")
elif check == 0:
    print(f"Last digit of {number} is {check} and is 0")
elif check < 6 and check != 0:
    print(f"Last digit of {number} is {check} and is less than 6 and not 0")
