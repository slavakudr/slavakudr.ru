import random

def roll():
    roll_count = 0
    while True:
        roll_input = input()
        if roll_input == 'roll':    
            result = random.randint(1, 100)
            print(f'Результат: {result}')
            roll_count += 1
            continue
        if roll_input == 'end':
            return print(f'Всего результатов: {roll_count}')
roll()