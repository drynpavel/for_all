#input_text = input('Введите сообщение: ')
alhabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
input_text = 'это питон'
cesar_step = int(input('Введите сдвиг: '))


new_text = [alhabet[(alhabet.index(sym) + cesar_step) % 33]
            if sym != ' '
            else ' '
            for sym in input_text]
print('Закодированный текст', ''.join(new_text))

