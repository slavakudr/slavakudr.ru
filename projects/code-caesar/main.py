#code-caesar

# Системные настройки
CC_ENG_UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
CC_ENG_LOWER = 'abcdefghijklmnopqrstuvwxyz'
CC_RUS_UPPER = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
CC_RUS_LOWER = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

# Пользовательские настройки
cc_text = input('Введите русский или английский текст: ')
cc_step = int(input('Введите шаг сдвига [< 0 дешифрование] или [> 0 шифрование]): '))

def main(cc_text, cc_step):
    cc_result = []
    # Определение языка
    if (cc_text[0] in CC_ENG_UPPER) or (cc_text[0] in CC_ENG_LOWER):
        cc_dict_upper = CC_ENG_UPPER
        cc_dict_lower = CC_ENG_LOWER
        cc_dict_count = 26
    elif (cc_text[0] in CC_RUS_UPPER) or (cc_text[0] in CC_RUS_LOWER):
        cc_dict_upper = CC_RUS_UPPER
        cc_dict_lower = CC_RUS_LOWER
        cc_dict_count = 32
    else:
        print('Введен непонятный язык.')
    # Обработка введенного текста
    for item in range(len(cc_text)):
        if cc_text[item].isalpha():
            if cc_text[item].isupper():
                cc_result.append(cc_dict_upper[(cc_dict_upper.find(cc_text[item]) + cc_step) % cc_dict_count])
            else:
                cc_result.append(cc_dict_lower[(cc_dict_lower.find(cc_text[item]) + cc_step) % cc_dict_count])
        else:
            cc_result.append(cc_text[item])
    
    return ''.join(cc_result)

print(main(cc_text, cc_step))