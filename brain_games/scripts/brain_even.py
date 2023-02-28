import prompt


print('brain-even')

print('Welcome to the Brain Games!')
name = prompt.string('May I have your name? ')
print(f'{"Hello, " + name + "!"}')

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
                  "Let's try again, " + name + '!')

    else:
        if input('Your answer: ') == 'no':
            print('Correct!')
        else:
            print("'yes' is wrong answer ;(."
                  " Correct answer was 'no'. "
                  "Let's try again, " + name + '!')


print('Congratulations, ' + name + '!')