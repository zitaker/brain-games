from random import randint


def brain():
    print('brain-calc')


def condition():
    print('What is the result of the expression?')


def question_task():
    number_1 = randint(0, 10)
    number_2 = randint(0, 10)

    result = randint(0, 2)

    if result == 0:
        correct = (number_1 + number_2)
        operations = '+'
    elif result == 1:
        correct = (number_1 - number_2)
        operations = '-'
    else:
        correct = (number_1 * number_2)
        operations = '*'

    question = f'{number_1} {operations} {number_2}'

    type_input = int

    return question, correct, type_input
