import prompt
from random import randint


def simple_number_list():
    n = 100
    simple_numbers = []
    for i in range(2, n + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            simple_numbers.append(i)

    return simple_numbers


def result_prime():
    simple_numbers = simple_number_list()

    print('brain-prime')
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'{"Hello, " + name + "!"}')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    # life - кол-во жизней
    n = 0
    life = 3
    for life in range(0, life + 1):
        n += life
        if life == 3:
            print('Congratulations, ' + name + '!')
            break

        numbers = randint(0, 100)
        print('Question:', numbers)

        num_input = input('Your answer: ')

        if numbers in simple_numbers:
            correct = 'yes'
        elif numbers not in simple_numbers:
            correct = 'no'

        if (numbers in simple_numbers and num_input == 'yes')\
                or (numbers not in simple_numbers and num_input == 'no'):
            print('Correct!')
        else:
            print(f"'{num_input}'",
                  "is wrong answer ;(. "
                  "Correct answer was",
                  f"'{correct}'" + ". "
                  "Let's try again,", name + "!")
            break
