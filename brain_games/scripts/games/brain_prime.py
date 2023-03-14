# !/usr/bin/env python3
import prompt
from random import randint


def welcome_user_prime():
    print('brain-prime')
    print('Welcome to the Brain Games!')
    names = prompt.string('May I have your name? ')
    print(f'{"Hello, " + names + "!"}')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    return names


name = welcome_user_prime()


n = 100


def simple_number_list():
    simple_numbers = []
    for i in range(2, n + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            simple_numbers.append(i)
    return simple_numbers


simple_numbers = simple_number_list()


def result_prime():
    # life - кол-во жизней
    life = 3
    while life > 0:
        life = life - 1
        numbers = randint(0, 100)
        print('Question:', numbers)

        def numbers_verification():
            if numbers in simple_numbers:
                correct = 'yes'
            elif numbers not in simple_numbers:
                correct = 'no'

            return correct

        correct = numbers_verification()

        numbers_input = input('Your answer: ')

        if numbers_input == correct:
            print('Correct!')
        else:
            print(f"'{numbers_input}'",
                  "is wrong answer ;(. "
                  "Correct answer was",
                  f"'{correct}'" + ". "
                  "Let's try again,", name + "!")
            break

    return life


life = result_prime()

if life <= 0:
    print('Congratulations, ' + name + '!')
