ru_lang_up = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
ru_lang_low = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
en_lang_up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
en_lang_low = 'abcdefghijklmnopqrstuvwxyz'

def start():
    direction = int(input('Укажите направление: шифрование (1) / дешифрование (0): '))
    language = input('Выберите язык алфавита: en / ru: ')
    step = int(input('Укажите шаг сдвига: '))
    text = [i for i in input('Введите текст для обработки: ')]

    if direction == 1:
        if language == 'en':
            encrypt_en(text, step)
        elif language == 'ru':
            encrypt_ru(text, step)
    elif direction == 0:
        if language == 'en':
            decrypt_en(text, step)
        elif language == 'ru':
            decrypt_ru(text, step)


def encrypt_en(text, step):
    for i in range(len(text)):
        if text[i] in en_lang_low:
            text[i] = en_lang_low[(en_lang_low.index(text[i])+step) % 26]
        if text[i] in en_lang_up:
            text[i] = en_lang_up[(en_lang_up.index(text[i])+step) % 26]
        else:
            continue
    print(*text, sep='')
    return text


def encrypt_ru(text, step):
    for i in range(len(text)):
        if text[i] in ru_lang_low:
            text[i] = ru_lang_low[(ru_lang_low.index(text[i])+step) % 32]
        if text[i] in ru_lang_up:
            text[i] = ru_lang_up[(ru_lang_up.index(text[i])+step) % 32]
        else:
            continue
    print(*text, sep='')
    return text


def decrypt_en(text, step):
    for k in range(step):
        for i in range(len(text)):
            if text[i] in en_lang_low:
                text[i] = en_lang_low[(en_lang_low.index(text[i])-step) % 26]
            if text[i] in en_lang_up:
                text[i] = en_lang_up[(en_lang_up.index(text[i])-step) % 26]
            else:
                continue
        print(*text, sep='')
    return text


def decrypt_ru(text, step):
    for k in range(step):
        for i in range(len(text)):
            if text[i] in ru_lang_low:
                text[i] = ru_lang_low[(ru_lang_low.index(text[i])-step) % 32]
            if text[i] in ru_lang_up:
                text[i] = ru_lang_up[(ru_lang_up.index(text[i])-step) % 32]
            else:
                continue
        print(*text, sep='')
    return text

start()
