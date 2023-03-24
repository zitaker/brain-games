from random import randint


def brain():
    print('brain-even')


def question_task():
    question = randint(0, 100)

    if question % 2 == 0:
        correct = 'yes'
    elif question % 2 != 0:
        correct = 'no'

    return question, correct
