# !/usr/bin/env python3
import prompt
from random import randint


print('brain-calc')


# def main():
#     print('Welcome to the Brain Games!')
#
#
# main()


def types_operation():
    number_1 = randint(0, 10)
    number_2 = randint(0, 10)

    result = randint(0, 2)

    if result == 0:
        result_expression = (number_1 + number_2)
        operations = '+'
    elif result == 1:
        result_expression = (number_1 - number_2)
        operations = '-'
    else:
        result_expression = (number_1 * number_2)
        operations = '*'

    print('Question:', number_1, operations, number_2)
    return result_expression


def checking_answers():
    name = prompt.string('May I have your name? ')
    print(f'{"Hello, " + name + "!"}')
    print('What is the result of the expression?')

    # life - кол-во жизней
    life = 3
    while life > 0:
        life = life - 1
        result_expressions = types_operation()
        answer = int(input('Your answer: '))

        if answer == result_expressions:
            print('Correct!')
        else:
            print(f"'{answer}'",
                  "is wrong answer ;(. "
                  "Correct answer was",
                  f"'{result_expressions}'" + ". "
                  "Let's try again,", name + "!")
            break

        if life <= 0:
            print('Congratulations, ' + name + '!')


checking_answers()
