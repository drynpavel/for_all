input_text = input('Введите текст:')

vowels = 'аоиеёэыуюя'
only_vowels = [c for c in input_text if c in vowels ]
print('Список гласных букв:',only_vowels)
print('Длина списка:', len(only_vowels))

