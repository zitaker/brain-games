import prompt


def main():
    print('Welcome to the Brain Games!')


main()


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'{"Hello, " + name + "!"}')
