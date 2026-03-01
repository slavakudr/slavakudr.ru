import random


def guess_number():
    print('Добро пожаловать в игру где нужно угадать число.')
    print('Введите начальное число')
    num_start = int(input())
    print('Введите конечное число')
    num_end = int(input())
    num_random = random.randint(num_start, num_end)
    user_input_count = 0
    while True:
        print('Попробуйте угадать число')
        user_input = int(input())
        user_input_count += 1
        if user_input > num_random:
            print('Слишком много, попробуйте еще раз')
            continue
        elif user_input < num_random:
            print('Слишком мало, попробуйте еще раз')
            continue
        else:
            print('Вы угадали, поздравляем!', f'Всего попыток было: {user_input_count}', sep='\n')
            break

guess_number()