from random import randint
import math


def brain():
    print('brain-gcd')


def condition():
    print('Find the greatest common divisor of given numbers.')


def question_task():
    numbers_1 = randint(1, 10)
    numbers_2 = randint(1, 10)

    question = f'{numbers_1} {numbers_2}'

    correct = math.gcd(numbers_1, numbers_2)

    type_input = int

    return question, correct, type_input
