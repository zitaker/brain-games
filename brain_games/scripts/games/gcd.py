import prompt
import math
from random import randint


def checking_answers_qcd():
    print('brain-gcd')
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'{"Hello, " + name + "!"}')
    print('Find the greatest common divisor of given numbers.')

    # life - кол-во жизней
    n = 0
    life = 3
    for life in range(0, life + 1):
        n += life
        if life == 3:
            print('Congratulations, ' + name + '!')
            break

        numbers_1 = randint(1, 10)
        numbers_2 = randint(1, 10)

        print('Question:', numbers_1, numbers_2)
        result_gcd = math.gcd(numbers_1, numbers_2)

        answer = int(input('Your answer: '))

        if answer == result_gcd:
            print('Correct!')
        else:
            print(f"'{answer}'",
                  "is wrong answer ;(. "
                  "Correct answer was",
                  f"'{result_gcd}'" + ". "
                  "Let's try again,", name + "!")
            break
