import prompt


def welcome_user_progression():
    print('Для тех - кто ябедничал, кто не понимает английский')
    print('Приветствую тебя в доме своем')
    names = prompt.string('Кто ты друг: ')
    print(f'{"Добро пожаловать, " + names + "!"}')
    return names


name = welcome_user_progression()

print('Варианты: 1 - гостинная, 2 - спальня, 3 - детская')
result_1 = int(input('Оказавшись в доме, в какую комнату из трех пойдешь: '))

def qwerty():
    x = 1
    y = 0
    while x >= 0:
        x - 1
        if result_1 == 1:
            print('тут накрыт стол для пира')
        elif result_1 == 2:
            print('ложишься на кровать и смотришь телевизор')
        elif result_1 == 3:
            print('наступаешь на острый угол игрушки и ударяешься мизинчиком об угол - на этом жизнь заканчивается')
            break


qwerty()