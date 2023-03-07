# !/usr/bin/env python3
import prompt
import math
from random import randint


# def welcome_user_gcd():
#     print('brain-gcd')
#     print('Welcome to the Brain Games!')
#     names = prompt.string('May I have your name? ')
#     print(f'{"Hello, " + names + "!"}')
#
#     print('What is the result of the expression?')
#     return names
#
#
# name = welcome_user_gcd()

print('Find the greatest common divisor of given numbers.')

numbers_1 = randint(0, 100)
numbers_2 = randint(0, 100)

print(numbers_1)
print(numbers_2)

print(math.gcd(numbers_1, numbers_2))
