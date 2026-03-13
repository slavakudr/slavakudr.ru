import random

# Встроенные данные
DIGIT = '0123456789'
LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
PUNCTUATION = '!#$%&*+-=?@^_'
REMOVE_LETTERS = 'il1Lo0O'
chars = ''

# Пользовательские данные
pw_count = int(input('Количество паролей для генерации: '))
pw_length = int(input('Длина одного пароля: '))
pw_digit = input('Включать цифры? (да/нет): ')
pw_lowercase_letters = input('Включать ли маленькие буквы? (да/нет): ')
pw_upper_letters = input('Включать ли большие буквы? (да/нет): ')
pw_punctuation = input('Включать ли символы? (да/нет)')
pw_remove_letters = input('Исключать ли неоднозначные символы? (да/нет)')

# Настройка пароля
if pw_digit == 'да':
    chars += DIGIT
if pw_lowercase_letters == 'да':
    chars += LOWERCASE_LETTERS
if pw_upper_letters == 'да':
    chars += UPPERCASE_LETTERS
if pw_punctuation == 'да':
    chars += PUNCTUATION
if pw_remove_letters == 'да':
    for item in REMOVE_LETTERS:
        chars = chars.replace(item, '')

# Функция генерации пароля
def generate_password(pw_length, chars):
    password = ''
    for item in range(pw_length):
        password += random.choice(chars)
    return print(password)

# Генерация нескольких паролей
for item in range(pw_count):
    generate_password(pw_length, chars)