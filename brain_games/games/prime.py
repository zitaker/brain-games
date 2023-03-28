from random import randint


print('brain-prime')


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def simples():
    n = 100
    simple_numbers = []
    for i in range(2, n + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            simple_numbers.append(i)

    return simple_numbers


def task_condition():
    simple_numbers = simples()

    question = randint(0, 100)

    if question in simple_numbers:
        correct = 'yes'
    elif question not in simple_numbers:
        correct = 'no'

    return question, correct
