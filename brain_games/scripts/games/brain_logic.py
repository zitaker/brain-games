import prompt
from brain_games.scripts.games.even import question_task

from brain_games.scripts.games.even import brain


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'{"Hello, " + name + "!"}')
    print('Answer "yes" if the number is even, '
          'otherwise answer "no".')
    return name


def life_user(game):
    brain()
    name = welcome_user()
    # LIFE - кол-во жизней
    N = 0
    LIFE = 3
    for LIFE in range(1, LIFE + 1):
        N += LIFE
        question, correct = question_task()
        print('Question:', question)
        question_input = input('Your answer: ')

        if correct == question_input:
            print('Correct!')
        elif correct != question_input:
            print(f"'{question_input}'",
                  "is wrong answer ;(. "
                  "Correct answer was",
                  f"'{correct}'" + ". "
                  "Let's try again,", name + "!")
            break

        if LIFE == 3:
            print('Congratulations, ' + name + '!')
            break
