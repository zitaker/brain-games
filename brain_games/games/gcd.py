from random import randint


print('brain-gcd')


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def task_condition():
    numbers_1 = randint(1, 10)
    numbers_2 = randint(1, 10)

    question = f'{numbers_1} {numbers_2}'

    while numbers_1 != 0 and numbers_2 != 0:
        if numbers_1 > numbers_2:
            numbers_1 = numbers_1 % numbers_2
        else:
            numbers_2 = numbers_2 % numbers_1
    gcd = (numbers_1 + numbers_2)

    correct = str(gcd)

    return question, correct
