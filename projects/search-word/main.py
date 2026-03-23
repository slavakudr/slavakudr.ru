import random

word_list = ['человек', 'друг', 'мама', 'папа', 'ребёнок', 'бабушка', 'дедушка', 'брат', 'сестра', 'семья', 'учитель', 'врач', 'мужчина', 'женщина', 'товарищ', 'девушка', 'мальчик', 'отец', 'мать', 'народ', 'время', 'день', 'год', 'час', 'вечер', 'утро', 'ночь', 'минута', 'неделя', 'месяц', 'дом', 'город', 'улица', 'школа', 'работа', 'страна', 'лес', 'море', 'дорога', 'комната', 'место', 'сад', 'парк', 'музей', 'театр', 'магазин', 'квартира', 'двор', 'вид', 'мир', 'стол', 'стул', 'окно', 'дверь', 'книга', 'ручка', 'карандаш', 'телефон', 'телевизор', 'компьютер', 'машина', 'автобус', 'мяч', 'фотография', 'билет', 'подарок', 'чашка', 'тарелка', 'вода', 'земля', 'свет', 'небо', 'воздух', 'дерево', 'цветок', 'солнце', 'луна', 'ветер', 'дождь', 'снег', 'слово', 'дело', 'вопрос', 'ответ', 'жизнь', 'смерть', 'правда', 'любовь', 'счастье', 'мысль', 'идея', 'чувство', 'мечта', 'цель', 'сила', 'хлеб', 'чай', 'молоко', 'сок', 'яблоко']

def get_word(word_list):
    random_word = random.choice(word_list)
    return random_word.upper()

word = get_word(word_list)

def play(word):
    word_len = len(word)
    word_secret = '*' * word_len
    play_count = 0
    word_input = ''
    while '*' in word_secret:
        print(f'Угадай слово из {word_len} букв: {word_secret}')
        word_input = input('Введи букву, или слово целиком, или 0 для завершения игры: ').upper()
        if len(word_input) == 1 and word_input.isalpha():
            play_count += 1
            if word_input in word_secret:
                print('Буква уже есть в слове, введи другую.')
                continue
            elif word_input not in word:
                print('Буквы нет в слове, введи другую')
                continue
            else:
                print('Буква угадана!')
                
                word_secret_list = list(word_secret)
                word_input_index = []
                for item in range(len(word)):
                    if word[item] == word_input:
                        word_input_index.append(item)
                for item in word_input_index:
                    word_secret_list[item] = word_input
                word_secret = ''.join(word_secret_list)
                continue
        elif len(word_input) == len(word) and word_input.isalpha():
            play_count += 1
            if word_input != word:
                print(f'Слово {word_input} не угадано.')
            else:
                break
        elif word_input == '0':
            break
        else:
            print('Введи букву, или слово целиком, или 0 для завершения игры.')
            continue
    if '*' in word_secret:
        return print('--------------------',f'Игра завершена. Слово было загадано {word}', f'Кол-во попыток: {play_count}', '--------------------', sep='\n')
    else:
        return print('--------------------',f'Слово угадано: {word}', f'Кол-во попыток: {play_count}', '--------------------', sep='\n')

play(word)