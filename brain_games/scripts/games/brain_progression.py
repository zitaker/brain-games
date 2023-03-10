# !/usr/bin/env python3
# import prompt
from random import randint


# def welcome_user_progression():
#     print('brain-progression')
#     print('Welcome to the Brain Games!')
#     names = prompt.string('May I have your name? ')
#     print(f'{"Hello, " + names + "!"}')
#     print('What number is missing in the progression?')
#     return names
#
#
# name = welcome_user_progression()
def arithmetic_progression():
    progression_1 = randint(1, 10)
    progression_2 = randint(1, 10)
    progression_3 = randint(100, 200)
    index = (list(range(progression_2, progression_3, progression_1)))
    return index


i = arithmetic_progression()


def result_progression():
    min_progression = 5
    max_progression = randint(0, 10)
    progression = (i[0:min_progression] + i[min_progression:max_progression])

    num_input = randint(0, max_progression)
    print(num_input)
    print(progression[num_input])

    progres_str = (" ".join(map(str, progression)))
    num_replace = str(progres_str).replace(str(progression[num_input]), '..')
    print(num_replace)


result_progression()
