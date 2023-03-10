# !/usr/bin/env python3
import prompt
from random import randint


def welcome_user_progression():
    print('brain-progression')
    print('Welcome to the Brain Games!')
    names = prompt.string('May I have your name? ')
    print(f'{"Hello, " + names + "!"}')
    print('What number is missing in the progression?')
    return names


name = welcome_user_progression()


def result_progression():
    # life - кол-во жизней
    life = 3
    while life > 0:
        life = life - 1

        def arithmetic_progression():
            progression_1 = randint(1, 10)
            progression_2 = randint(1, 10)
            progression_3 = randint(100, 200)
            index = (list(range(progression_2, progression_3, progression_1)))
            return index

        i = arithmetic_progression()

        min_progression = 5
        max_progression = randint(0, 10)
        progres = (i[0:min_progression] + i[min_progression:max_progression])

        num_input = randint(0, max_progression)

        progres_str = (" ".join(map(str, progres)))
        num_replace = str(progres_str).replace(str(progres[num_input]), '..')
        print(num_replace)

        comparison_num_input = int(input('Your answer: '))
        if comparison_num_input == progres[num_input]:
            print('Correct!')
        else:
            print(f"'{comparison_num_input}'",
                  "is wrong answer ;(. "
                  "Correct answer was",
                  f"'{progres[num_input]}'" + ". "
                  "Let's try again,", name + "!")
            break

        if life <= 0:
            print('Congratulations, ' + name + '!')


result_progression()
