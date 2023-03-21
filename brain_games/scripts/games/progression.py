import prompt
from random import randint


def result_progression():
    print('brain-progression')
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'{"Hello, " + name + "!"}')
    print('What number is missing in the progression?')

    # LIFE - кол-во жизней
    N = 0
    LIFE = 3
    for LIFE in range(0, LIFE + 1):
        N += LIFE
        if LIFE == 3:
            print('Congratulations, ' + name + '!')
            break

        progression_1 = randint(1, 10)
        progression_2 = randint(1, 200)
        i = []
        y = 10
        for y in range(1, y + 1, 1):
            progression_2 = progression_2 + progression_1
            i.append(progression_2)

        min_progres = 6
        max_progres = randint(0, 10)
        #   progres - список
        progres = (i[0:min_progres]) + (i[min_progres:max_progres])

        #   num_input - номер числа по индексу в рандомном списке
        num_input = randint(0, len(progres) - 1)

        points = '..'
        progres_str = (" ".join(map(str, progres)))
        num_replace = str(progres_str).replace(str(progres[num_input]), points)
        print('Question:', num_replace)

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
