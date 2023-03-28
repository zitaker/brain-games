from random import randint


print('brain-progression')


DESCRIPTION = 'What number is missing in the progression?'


def task_condition():
    increase_by_number = randint(1, 10)
    first_number = randint(1, 200)
    # i - список прогрессии длинною равной (y)
    i = []
    y = 10
    for y in range(1, y + 1, 1):
        first_number = first_number + increase_by_number
        i.append(first_number)

    min_progres = 6
    max_progres = randint(0, 10)

    #   progres - список прогрессии
    progres = (i[0:min_progres]) + (i[min_progres:max_progres])

    #   num_input - номер числа по индексу в рандомном списке
    num_input = randint(0, len(progres) - 1)

    points = '..'
    progres_str = (" ".join(map(str, progres)))
    question = str(progres_str).replace(str(progres[num_input]), points)

    correct = str(progres[num_input])

    return question, correct
