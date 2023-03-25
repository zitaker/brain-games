from random import randint


def brain():
    print('brain-prime')


def condition():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def question_task():
    n = 100
    simple_numbers = []
    for i in range(2, n + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            simple_numbers.append(i)

    question = randint(0, 100)

    if question in simple_numbers:
        correct = 'yes'
    elif question not in simple_numbers:
        correct = 'no'

    type_input = str

    return question, correct, type_input
