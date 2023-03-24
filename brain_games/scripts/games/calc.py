import prompt
from random import randint


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
    print('brain-calc')
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'{"Hello, " + name + "!"}')
    print('What is the result of the expression?')

    # LIFE - кол-во жизней
    N = 0
    LIFE = 3
    for LIFE in range(0, LIFE + 1):
        N += LIFE
        if LIFE == 3:
            print('Congratulations, ' + name + '!')
            break
        result_expressions = types_operation()
        answers = input('Your answer: ')
        answer = int(answers)

        if answer == result_expressions:
            print('Correct!')
        else:
            print(f"'{answer}'",
                  "is wrong answer ;(. "
                  "Correct answer was",
                  f"'{result_expressions}'" + ". "
                  "Let's try again,", name + "!")
            break
