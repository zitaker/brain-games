# !/usr/bin/env python3
from brain_games.cli import welcome_user


def main():
    print('brain-games')
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print(f'{"Hello, " + name + "!"}')


if __name__ == '__main__':
    main()
