import random

def game_start():
    print('Добро пожаловать в числовую угадайку')
    print('В каком диапазоне загадать число?')
    print('Введите начало и конец диапазона:')
    first, last = int(input()), int(input())
    if last < first:
        first, last = last, first

    guess_game(first, last)
    game_proceed()

def is_valid(text, x, y):
    return int(text) in range(x, y)

def check_input(x, y):
    while True:
        question = input()
        if is_valid(question, x, y):
           return int(question)
        else:
            print(f'А может быть все-таки введем целое число от {x} до {y}?')
            continue

def game_proceed():
    print('Начать новую игру? (Да / Нет)')
    if input().lower() in ['да', 'д', 'yes', 'y']:
        game_start()
    else:
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')

def guess_game(first, last):
    num = random.randint(first, last)
    print(f'Введите целое число от {first} до {last}')
    count = 0
    while True:
        answer = check_input(first, last)
        count += 1
        if answer < num:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif answer > num:
            print('Ваше число больше загаданного, попробуйте еще разок')
        else:
            print(f'Вы угадали, поздравляем! \nКоличество попыток: {count}')
            break

game_start()
