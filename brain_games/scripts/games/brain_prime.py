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


def result_prime():
    # life - кол-во жизней
    life = 3
    while life > 0:
        life = life - 1

        def numbers_verification():

            numbers = randint(0, 100)
            print('Question:', numbers)

            simple_numbers = []
            for i in range(2, numbers + 1):
                for j in range(2, i):
                    if i % j == 0:
                        break
                else:
                    simple_numbers.append(i)

            if numbers in simple_numbers:
                return True
            else:
                return False

            return numbers

        numbers = numbers_verification()

        numbers_input = input('Your answer: ')
        if numbers is True:
            if numbers_input == 'yes':
                print('Correct!')
            else:
                print(f"'{numbers_input}'",
                      "is wrong answer ;(. "
                      "Correct answer was",
                      f"'{'yes'}'" + ". "
                      "Let's try again,", name + "!")
                break

        if numbers is False:
            if numbers_input == 'no':
                print('Correct!')
            else:
                print(f"'{numbers_input}'",
                      "is wrong answer ;(. "
                      "Correct answer was",
                      f"'{'no'}'" + ". "
                      "Let's try again,", name + "!")
                break

    if life <= 0:
        print('Congratulations, ' + name + '!')


result_prime()
