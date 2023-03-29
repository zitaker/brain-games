from random import randint


print('brain-prime')

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime():
    question = randint(2, 100)
    n = 0

    for i in range(2, question // 1):
        if question % i == 0:
            n = n + 1
    if n <= 0:
        result = True
    else:
        result = False
    return result, question


def task_condition():
    result, question = is_prime()

    if result is True:
        correct = 'yes'
    elif result is False:
        correct = 'no'

    return question, correct
