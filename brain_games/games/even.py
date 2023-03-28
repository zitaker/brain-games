from random import randint


print('brain-even')

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def task_condition():
    question = randint(0, 100)

    if question % 2 == 0:
        correct = 'yes'
    elif question % 2 != 0:
        correct = 'no'

    return question, correct
