from random import randint


def brain():
    print('brain-even')


def condition():
    print('Answer "yes" if the number is even, '
          'otherwise answer "no".')


def question_task():
    question = randint(0, 100)

    if question % 2 == 0:
        correct = 'yes'
    elif question % 2 != 0:
        correct = 'no'

    type_input = str

    return question, correct, type_input
