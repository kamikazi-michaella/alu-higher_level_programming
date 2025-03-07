#!/usr/bin/python3
import random

# Assign a random number to the variable number
number = random.randint(-10000, 10000)

# Find the last digit
last_digit = abs(number) % 10 if number >= 0 else -(-number % 10)

# Print the result based on the conditions
print(f"Last digit of {number} is {last_digit}", end=" ")

if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
