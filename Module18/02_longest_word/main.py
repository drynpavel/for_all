list_word = input(('Введите строку: ')).split()


max_word = max(list_word, key = len)
max_len = len(list_word[list_word.index((max_word))])

print('Самое длинное слово: ', max_word)
print('Длина этого слова:', max_len)

