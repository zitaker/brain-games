# !/usr/bin/env python3
import prompt
from random import randint


def qwerty():
    print('Welcome to the Brain Games!')
    names = prompt.string('May I have your name? ')
    print(f'{"Hello, " + names + "!"}')

    print('Answer "yes" if the number is even, '
          'otherwise answer "no".')
    return names


name = qwerty()


def life_user():
    # life - кол-во жизней
    life = 1
    while life > 0:
        #   randint - задать random число в промежутке
        question_numbers = [randint(0, 10)]
        #   correct_response - считать ответы
        correct_response = 0
        # numbers равен элементу в списке question_numbers
        for numbers in question_numbers:
            print('Question:', numbers)

            if numbers % 2 == 0:
                if input('Your answer: ') == 'yes':
                    print('Correct!')
                    correct_response = correct_response + 1
                else:
                    print("'yes' is wrong answer ;(."
                          " Correct answer was 'no'. "
                          "Let's try again, " + name + '!')
                    correct_response = correct_response - 1

            else:
                if input('Your answer: ') == 'no':
                    print('Correct!')
                    correct_response = correct_response + 1
                else:
                    print("'yes' is wrong answer ;(."
                          " Correct answer was 'no'. "
                          "Let's try again, " + name + '!')
                    correct_response = correct_response - 1

        if correct_response < 0:
            break
        else:
            print('Congratulations, ' + name + '!')

        life = life - 1


life_user()
