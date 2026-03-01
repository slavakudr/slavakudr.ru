import random

def fn_random(random_start, random_end):
    random_count = 0
    random_max = random_start
    random_min = random_end
    while True:
        print('Введите "new" или "stop"')
        random_input = input()
        if random_input == 'new':
            result = random.randint(random_start, random_end)
            print(f'Результат: {result}')
            random_count += 1
            if result > random_max:
                random_max = result
            if result < random_min:
                random_min = result
            continue
        elif random_input == 'stop':
            if random_count == 1:
                return print(f'Всего результатов: {random_count}')
            elif random_count > 1:
                return print(f'Всего результатов: {random_count}', f'Максимальный результат: {random_max}', f'Минимальный результат: {random_min}', sep='\n')
            else:
                return print('Нет результатов.')

print('Введите начало диапазона:')
random_start = int(input())
print('Введите конец диапазона:')
random_end = int(input())

fn_random(random_start, random_end)