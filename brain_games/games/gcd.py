from random import randint
import math


print('brain-gcd')


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def task_condition():
    numbers_1 = randint(1, 10)
    numbers_2 = randint(1, 10)

    question = f'{numbers_1} {numbers_2}'

    correct = math.gcd(numbers_1, numbers_2)

    return question, correct
