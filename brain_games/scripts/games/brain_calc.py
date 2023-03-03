# !/usr/bin/env python3
import prompt


print('brain-calc')
def welcome_user():
    print('Welcome to the Brain Games!')
    names = prompt.string('May I have your name? ')
    print(f'{"Hello, " + names + "!"}')
    return names

# name = welcome_user()

print('What is the result of the expression?')

calculations = [4 + 10, 5 + 2]

print('Question: 4 + 10')
calculation_calculator = input('Your answer: ')
print(calculations[1])


