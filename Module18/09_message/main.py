
def reverse_word(word):
    index_add = 0
    list_word = []
    for buf_word in word:
        if buf_word.isalnum():
            list_word.insert(index_add,buf_word)
        else:
            list_word.append(buf_word)
            index_add = len(list_word)
    return ''.join(list_word)

list_word = input('Сообщение: ').split()
new_word = []

for buf_word in list_word:
    if buf_word.isalnum():
        new_word.append(buf_word[::-1])
    else:
        new_word.append(reverse_word(buf_word))
print('Новое сообщение:', ' '.join(new_word))