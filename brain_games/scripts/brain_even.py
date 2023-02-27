print('Answer "yes" if the number is even, '
      'otherwise answer "no".')

question_numbers = [15, 6, 7]
print('Question:', question_numbers[1])
# print(question_numbers[2])
numbers = int(input('Your answer: '))

if numbers % 2 == 0:
    print('четное')
else:
    print('нечетное')
