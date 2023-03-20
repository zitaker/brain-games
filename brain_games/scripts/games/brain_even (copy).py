# !/usr/bin/env python3
import prompt
from random import randint


print('brain-even')


# def main():
#     print('Welcome to the Brain Games!')
#
#
# main()


def life_user():
    name = prompt.string('May I have your name? ')
    print(f'{"Hello, " + name + "!"}')
    print('Answer "yes" if the number is even, '
          'otherwise answer "no".')

    # life - кол-во жизней
    n = 0
    life = 3
    for life in range(0, life + 1):
        n += life
        if life == 3:
            print('Congratulations, ' + name + '!')
            break

        #   randint - задать random число в промежутке
        question_numbers = randint(0, 100)

        print('Question:', question_numbers)
        even_input = input('Your answer: ')

        if question_numbers % 2 == 0:
            if even_input == 'yes':
                print('Correct!')
            else:
                print(f"'{even_input}'",
                      "is wrong answer ;(. "
                      "Correct answer was",
                      f"'{'yes'}'" + ". "
                      "Let's try again,", name + "!")
                break

        else:
            if even_input == 'no':
                print('Correct!')
            else:
                print(f"'{even_input}'",
                      "is wrong answer ;(. "
                      "Correct answer was",
                      f"'{'no'}'" + ". "
                      "Let's try again,", name + "!")
                break


life_user()
