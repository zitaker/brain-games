import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'{"Hello, " + name + "!"}')
    return name


def life_user(manual):
    manual.brain()
    name = welcome_user()
    manual.condition()
    # LIFE - кол-во жизней
    N = 0
    LIFE = 3
    for LIFE in range(1, LIFE + 1):
        N += LIFE
        question, correct, type_input = manual.question_task()
        print('Question:', question)
        question_input = type_input(input('Your answer: '))

        if correct == question_input:
            print('Correct!')
        else:
            print(f"'{question_input}'",
                  "is wrong answer ;(. "
                  "Correct answer was",
                  f"'{correct}'" + ". "
                  "Let's try again,", name + "!")
            break

        if LIFE == 3:
            print('Congratulations, ' + name + '!')
            break
