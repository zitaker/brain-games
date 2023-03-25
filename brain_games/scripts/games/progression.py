from random import randint


def brain():
    print('brain-progression')


def condition():
    print('What number is missing in the progression?')


def question_task():
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
    question = str(progres_str).replace(str(progres[num_input]), points)

    correct = progres[num_input]

    type_input = int

    return question, correct, type_input
