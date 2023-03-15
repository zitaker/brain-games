# !/usr/bin/env python3
import prompt
import math
from random import randint


print('brain-gcd')


def main():
    print('Welcome to the Brain Games!')


main()


def welcome_user_gcd():
    names = prompt.string('May I have your name? ')
    print(f'{"Hello, " + names + "!"}')
    print('Find the greatest common divisor of given numbers.')
    return names


name = welcome_user_gcd()


def checking_answers_qcd():
    # life - кол-во жизней
    life = 3
    while life > 0:
        life = life - 1
        numbers_1 = randint(1, 10)
        numbers_2 = randint(1, 10)

        print('Question:', numbers_1, numbers_2)
        result_gcd = math.gcd(numbers_1, numbers_2)

        answer = int(input('Your answer: '))

        if answer == result_gcd:
            print('Correct!')
        else:
            print(f"'{answer}'",
                  "is wrong answer ;(. "
                  "Correct answer was",
                  f"'{result_gcd}'" + ". "
                  "Let's try again,", name + "!")
            break

        if life <= 0:
            print('Congratulations, ' + name + '!')


checking_answers_qcd()
