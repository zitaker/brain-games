import prompt
from brain_games.games.constant import ROUNDS


def start(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'{"Hello, " + name + "!"}')

    print(game.DESCRIPTION)

    for _ in range(1, ROUNDS + 1):
        question, correct = game.task_condition()
        print('Question:', question)
        question_input = input('Your answer: ')

        if correct == question_input:
            print('Correct!')
        else:
            print(f"'{question_input}'",
                  "is wrong answer ;(. "
                  "Correct answer was",
                  f"'{correct}'" + ". "
                  "Let's try again,", name + "!")
            break

    print('Congratulations, ' + name + '!')
    return
