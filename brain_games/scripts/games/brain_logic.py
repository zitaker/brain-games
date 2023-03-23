import prompt
from brain_games.scripts.games.even import beginning_task


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
    N = 0
    LIFE = 3
    for LIFE in range(1, LIFE + 1):
        N += LIFE
        beginning_task()
        if LIFE == 3:
            print('Congratulations, ' + name + '!')
            break