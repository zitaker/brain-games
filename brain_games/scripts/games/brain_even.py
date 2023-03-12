# !/usr/bin/env python3
import prompt
from random import randint


def welcome_user_even():
    print('brain-even')
    print('Welcome to the Brain Games!')
    names = prompt.string('May I have your name? ')
    print(f'{"Hello, " + names + "!"}')
    print('Answer "yes" if the number is even, '
          'otherwise answer "no".')
    return names


name = welcome_user_even()


def life_user():
    # life - кол-во жизней
    life = 3
    while life > 0:
        life = life - 1
        #   randint - задать random число в промежутке
        question_numbers = randint(0, 10)
        #   correct_response - считать ответы
        correct_response = 0
        print('Question:', question_numbers)
        even_input = input('Your answer: ')

        if question_numbers % 2 == 0:
            if even_input == 'yes':
                print('Correct!')
                correct_response = correct_response + 1
            else:
                print(f"'{even_input}'",
                      "is wrong answer ;(. "
                      "Correct answer was",
                      f"'{'yes'}'" + ". "
                      "Let's try again,", name + "!")
                correct_response = correct_response - 1

        else:
            if even_input == 'no':
                print('Correct!')
                correct_response = correct_response + 1
            else:
                print(f"'{even_input}'",
                      "is wrong answer ;(. "
                      "Correct answer was",
                      f"'{'no'}'" + ". "
                      "Let's try again,", name + "!")
                correct_response = correct_response - 1

        if correct_response < 0:
            break
        else:
            print('Congratulations, ' + name + '!')


life_user()
