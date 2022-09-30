# TODO здесь писать код
text = input('Введите строку: ')
buf_text = set()
for i in text:
    if i in buf_text:
        buf_text.remove(i)
    else:
        buf_text.add(i)
print(('можно','нельзя')[len(buf_text)>1], 'сделать полиндром')