import prompt
from random import randint


def life_user():
    print('brain-even')
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'{"Hello, " + name + "!"}')
    print('Answer "yes" if the number is even, '
          'otherwise answer "no".')

    # LIFE - кол-во жизней
    N = 0
    LIFE = 3
    for LIFE in range(0, LIFE + 1):
        N += LIFE
        if LIFE == 3:
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