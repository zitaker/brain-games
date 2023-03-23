from random import randint


question_numbers = []
N = 0
list_numbers = 10
for list_numbers in range(1, list_numbers + 1):
    N += list_numbers
    question_numbers.append(randint(0, 100))


def beginning_task():
        print('Question:', question_numbers[randint(0, 9)])
        question_input = input('Your answer: ')


        # if question_numbers % 2 == 0:
        #     if question_input == 'yes':
        #         print('Correct!')
        #     else:
        #         print(f"'{question_input}'",
        #               "is wrong answer ;(. "
        #               "Correct answer was",
        #               f"'{'yes'}'" + ". "
        #               "Let's try again,", name + "!")
        #         break
        #
        # else:
        #     if question_input == 'no':
        #         print('Correct!')
        #     else:
        #         print(f"'{question_input}'",
        #               "is wrong answer ;(. "
        #               "Correct answer was",
        #               f"'{'no'}'" + ". "
        #               "Let's try again,", name + "!")
        #         break
