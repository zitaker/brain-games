# !/usr/bin/env python3
import prompt
from random import randint


# def welcome_user_prime():
#     print('brain-prime')
#     print('Welcome to the Brain Games!')
#     names = prompt.string('May I have your name? ')
#     print(f'{"Hello, " + names + "!"}')
#     print('Answer "yes" if given number is prime. Otherwise answer "no".')
#     return names
#
#
# name = welcome_user_prime()
name = '1234567890'


def numbers_verification():

    numbers = randint(0, 100)
    print('Question:', numbers)
    # numbers = 85

    if numbers == 2:
        print('это простое число')
        return True
    elif numbers <= 1:
        print('неправильно numbers <= 1')
        return False
    elif numbers % 2 == 0:
        print('неправильно numbers % 2 == 0')
        return False
    elif numbers / 1 / numbers == 1:
        print('это простое число numbers / 1 / numbers == 1')
        return True
    return numbers


number = numbers_verification()
print(number)

numbers_input = input('Your answer: ')

if number == True:
    if numbers_input == 'yes':
        print('Correct!')
    else:
        print(f"'{numbers_input}'",
              "is wrong answer ;(. "
              "Correct answer was",
              f"'{'yes'}'" + ". "
              "Let's try again,", name + "!")

if number == False:
    if numbers_input == 'no':
        print('Correct!')
    else:
        print(f"'{numbers_input}'",
              "is wrong answer ;(. "
              "Correct answer was",
              f"'{'no'}'" + ". "
              "Let's try again,", name + "!")
