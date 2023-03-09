# !/usr/bin/env python3
import prompt
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

progression_1 = randint(1, 10)
progression_2 = randint(1, 20)
progression_3 = randint(1, 200)


try:
    i = (list(range(progression_2, progression_3, progression_1)))
    print(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9])
# except IndexError:
except IndexError:
    print('qwerty 1')
    print(i[0], i[1], i[2], i[3], i[4], i[5])





# progression_length = 0
# while progression_length <= 2:
#     progression_2 = (progression_2 + progression_1)
#     progression_length = progression_length + 1
#     print(progression_2)



