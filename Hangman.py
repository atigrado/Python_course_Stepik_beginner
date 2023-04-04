import random

word_list = ['момент', 'режим', 'отличие', 'теория', 'крест', 'предприятие', 'шанс', 'момент', 'деталь', 'признание',
             'князь', 'рассмотрение', 'цвет', 'июнь', 'следователь', 'декабрь', 'восток', 'понимание', 'профессия',
             'зритель', 'записка', 'возвращение', 'разработка', 'земля', 'страница']
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

def start_game():
    while True:
        play(get_word())
        resume = input('Хотите сыграть еще? (да / нет) ')
        if resume == 'да':
            print('\n')
        else:
            break


def play(word):
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False  # сигнальная метка
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток

    print(word)

    print('Давайте играть в угадайку слов!')
    print(display_hangman(tries), '\nПопыток осталось: ', tries)
    print(word_completion)

    while not guessed:
        guess = input('Введите букву или слово целиком: ')
        if not guess.isalpha():
            guess = input('Некорректный ввод. Введите букву или слово целиком: ')
        else:
            if guess.lower() in guessed_letters or guess.lower() in guessed_words:
                print('Это повтор. Попробуй еще раз: ')
            else:
                if len(guess) > 1:
                    guessed_words.append(guess.lower())
                    if guess.lower() == word:
                        print(word.upper())
                        print('Поздравляем, вы угадали слово! Вы победили!')
                        guessed = True
                    else:
                        tries -= 1
                        if tries == 0:
                            print(display_hangman(tries))
                            print('Вы проиграли!')
                            print(word.upper())
                            guessed = True
                        else:
                            print(display_hangman(tries), '\nПопыток осталось: ', tries)
                            print(word_completion)
                else:
                    guessed_letters.append(guess.lower())
                    if guess.lower() in word:
                        for i in range(len(word)):
                            if word[i] == guess.lower():
                                word_completion = word_completion[:i] + guess.upper() + word_completion[i+1:]
                            if word_completion == word.upper():
                                print('Поздравляем, вы угадали слово! Вы победили!')
                                guessed = True
                        print(word_completion)
                    else:
                        tries -= 1
                        if tries == 0:
                            print(display_hangman(tries))
                            print('Вы проиграли!')
                            print(word.upper())
                            guessed = True
                        else:
                            print(display_hangman(tries), '\nПопыток осталось: ', tries)
                            print(word_completion)


def get_word():
    return word_list[random.randrange(26)]


def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        ''' 
                   -------- 
                   |      | 
                   |      O 
                   |     \\|/ 
                   |      | 
                   |     / \\
                   - 
                ''',
        # голова, торс, обе руки, одна нога
        ''' 
                   -------- 
                   |      | 
                   |      O 
                   |     \\|/ 
                   |      | 
                   |     /  
                   - 
                ''',
        # голова, торс, обе руки
        ''' 
                   -------- 
                   |      | 
                   |      O 
                   |     \\|/ 
                   |      | 
                   |       
                   - 
                ''',
        # голова, торс и одна рука
        ''' 
                   -------- 
                   |      | 
                   |      O 
                   |     \\| 
                   |      | 
                   |      
                   - 
                ''',
        # голова и торс
        ''' 
                   -------- 
                   |      | 
                   |      O 
                   |      | 
                   |      | 
                   |      
                   - 
                ''',
        # голова
        ''' 
                   -------- 
                   |      | 
                   |      O 
                   |     
                   |       
                   |      
                   - 
                ''',
        # начальное состояние
        ''' 
                   -------- 
                   |      | 
                   |       
                   |     
                   |       
                   |      
                   - 
                '''
    ]
    return stages[tries]

start_game()
