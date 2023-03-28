from random import randint, choice


print('brain-calc')

DESCRIPTION = 'What is the result of the expression?'


def task_condition():
    number_1 = randint(0, 10)
    number_2 = randint(0, 10)

    operations = choice('+-*')

    if operations == '+':
        correct = str(number_1 + number_2)
    elif operations == '-':
        correct = str(number_1 - number_2)
    else:
        correct = str(number_1 * number_2)

    question = f'{number_1} {operations} {number_2}'

    return question, correct
