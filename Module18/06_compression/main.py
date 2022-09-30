input_text = input('Введите строку: ')
previous_text = input_text[0]
count_str = 1
zip_text = []

for buf_text in input_text[1:]:
    if buf_text == previous_text:
        count_str += 1
    else:
        zip_text.append(''.join([previous_text, str(count_str)]))
        previous_text = buf_text
        count_str = 1
zip_text.append(''.join([previous_text, str(count_str)]))
print(''.join(zip_text))

