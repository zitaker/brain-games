# !/usr/bin/env python3
import prompt
from random import randint


print('brain-progression')


def main():
    print('Welcome to the Brain Games!')


main()


def welcome_user_progression():
    name = prompt.string('May I have your name? ')
    print(f'{"Hello, " + name + "!"}')
    print('What number is missing in the progression?')
    return name


name = welcome_user_progression()

def result_progression():
    # life - кол-во жизней
    n = 0
    life = 3
    for life in range(0, life + 1):
        n += life
        if life == 3:
            print('Congratulations, ' + name + '!')
            break

        def arithmetic_progression():
            # progression_1 = randint(1, 10)
            # progression_2 = randint(1, 10)
            # progression_3 = randint(100, 150)
            # i = (list(range(progression_2, progression_3, progression_1)))
            # return i

            progression_1 = randint(1, 10)
            progression_2 = randint(1, 200)
            i = []
            y = 10
            for y in range(1, y + 1, 1):
                progression_2 = progression_2 + progression_1
                i.append(progression_2)
            return i

        i = arithmetic_progression()

        min_progres = 6
        max_progres = randint(0, 10)
        #   progres - список
        progres = (i[0:min_progres]) + (i[min_progres:max_progres])

        #   num_input - номер числа по индексу в рандомном списке
        # num_input = randint(0, max_progres - 1)
        num_input = randint(0, len(progres) - 1)

        # points = '..'
        # progres_str = (" ".join(map(str, progres)))
        # num_replace = str(progres_str).replace(str(progres[num_input]), points)
        # print(num_replace)
        # print(progres[num_input])

        points = '..'
        progres_str = (" ".join(map(str, progres)))
        num_replace = str(progres_str).replace(str(progres[num_input]), points)
        print('Question:', num_replace)
        # print(type(progres[num_input]), progres[num_input])
        # qwerty = str(progres[num_input])        str
        # print(type(qwerty), qwerty)

        # comparison_num_input = str(input('Your answer: '))
        # if comparison_num_input in qwerty:
        #     print('Correct!')
        # elif comparison_num_input not in qwerty:
        #     print(f"'{comparison_num_input}'",
        #           "is wrong answer ;(. "
        #           "Correct answer was",
        #           f"'{progres[num_input]}'" + ". "
        #           "Let's try again,", name + "!")
        #     break

        comparison_num_input = int(input('Your answer: '))
        if comparison_num_input is progres[num_input]:
            print('Correct!')
        elif comparison_num_input is not progres[num_input]:
            print(f"'{comparison_num_input}'",
                  "is wrong answer ;(. "
                  "Correct answer was",
                  f"'{progres[num_input]}'" + ". "
                  "Let's try again,", name + "!")
            break


result_progression()
