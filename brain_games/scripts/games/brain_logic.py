import prompt
import brain_constants *


def welcome_user():
    print('brain-even')
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'{"Hello, " + name + "!"}')
    print('Answer "yes" if the number is even, '
          'otherwise answer "no".')
    return name


def life_user():
    name = welcome_user()

    # LIFE - кол-во жизней
    # N = 0
    # LIFE = 3
    for LIFE in range(0, LIFE + 1):
        N += LIFE
        if LIFE == 3:
            print('Congratulations, ' + name + '!')
            break
