import random

answers = ['Бесспорно', 'Мне кажется - да',	'Пока неясно, попробуй снова', 'Даже не думай', 'Предрешено',
           'Вероятнее всего', 'Спроси позже', 'Мой ответ - нет', 'Никаких сомнений', 'Хорошие перспективы',
           'Лучше не рассказывать', 'По моим данным - нет', 'Определённо да', 'Знаки говорят - да',
           'Сейчас нельзя предсказать', 'Перспективы не очень хорошие', 'Можешь быть уверен в этом', 'Да',
           'Сконцентрируйся и спроси опять', 'Весьма сомнительно']

print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
print('Как тебя зовут?')
print(f'Привет, {input()}')

while True:
    print('Задай мне вопрос')
    question = input()
    print(random.choice(answers))
    print('Хочешь задать еще вопрос? (Да / Нет)')
    if input().lower() in ['да', 'д', 'yes', 'y']:
        continue
    else:
        print('Возвращайся если возникнут вопросы!')
        break
