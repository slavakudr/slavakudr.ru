import random

def roll():
    roll_count = 0
    roll_max = 0
    roll_min = 100
    while True:
        roll_input = input()
        if roll_input == 'roll':    
            result = random.randint(1, 100)
            print(f'Результат: {result}')
            roll_count += 1
            if result > roll_max:
                roll_max = result
            elif result < roll_min:
                roll_min = result
            continue
        elif roll_input == 'end':
            return print(f'Всего результатов: {roll_count}', f'Максимальный результат: {roll_max}', f'Минимальный результат: {roll_min}', sep='\n')
roll()