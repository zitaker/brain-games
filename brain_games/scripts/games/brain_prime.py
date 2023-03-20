# !/usr/bin/env python3
import prompt
from random import randint


print('brain-prime')


def main():
    print('Welcome to the Brain Games!')


main()


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
    name = prompt.string('May I have your name? ')
    print(f'{"Hello, " + name + "!"}')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    # life - кол-во жизней
    n = 0
    life = 3
    for life in range(0, life + 1):
        n += life
        if life == 3:
            print('Congratulations, ' + name + '!')
            break

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


result_prime()
