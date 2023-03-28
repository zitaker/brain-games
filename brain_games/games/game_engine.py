import prompt


def start(manual):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'{"Hello, " + name + "!"}')

    print(manual.DESCRIPTION)
    ROUNDS = 3
    for ROUNDS in range(1, ROUNDS + 1):
        question, correct = manual.task_condition()
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
