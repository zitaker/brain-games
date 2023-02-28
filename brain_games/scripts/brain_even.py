from brain_games.cli import welcome_user


print('brain-even')
welcome_user()

print('1111111111')
print(name)
print('2222222222')

print('Answer "yes" if the number is even, '
      'otherwise answer "no".')

question_numbers = [15, 6, 7]
# numbers равен элементу в списке question_numbers
for numbers in question_numbers:
    print('Question', numbers)

    if numbers % 2 == 0:
        if input('Your answer: ') == 'yes':
            print('Correct!')
        else:
            print("'yes' is wrong answer ;(."
                  " Correct answer was 'no'. "
                  "Let's try again, Bill!")

    else:
        if input('Your answer: ') == 'no':
            print('Correct!')
        else:
            print("'yes' is wrong answer ;(."
                  " Correct answer was 'no'. "
                  "Let's try again, Bill!")

print('Congratulations, Bill!')