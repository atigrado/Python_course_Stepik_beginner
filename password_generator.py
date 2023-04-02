import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
ex_symbols = 'il1Lo0O'
chars = ''

pw_cuantity = int(input('Количество паролей для генерации: '))
pw_digits = input('Включать ли цифры 0123456789? (y/n) ')
if pw_digits == 'y':
    chars += digits
pw_uppers = input('Включать ли прописные буквы? (y/n) ')
if pw_uppers == 'y':
    chars += uppercase_letters
pw_lowers = input('Включать ли строчные буквы? (y/n) ')
if pw_digits == 'y':
    chars += lowercase_letters
pw_punct = input('Включать ли символы !#$%&*+-=?@^_? (y/n) ')
if pw_punct == 'y':
    chars += punctuation
pw_exclude = input('Исключать ли неоднозначные символы il1Lo0O? (y/n) ')
if pw_exclude == 'y':
    for i in ex_symbols:
        chars = chars.replace(i, '')

def generate_password(length, chars):
    return random.sample(chars, length)

def start_generate():
    length = int(input('Длина пароля: '))
    for _ in range(pw_cuantity):
        print(*generate_password(length, chars), sep='')

start_generate()
