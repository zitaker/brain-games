import prompt


def main():
    print('Welcome to the Brain Games!')


main()


def welcome_user():
    names = prompt.string('May I have your name? ')
    print(f'{"Hello, " + names + "!"}')
    return names
