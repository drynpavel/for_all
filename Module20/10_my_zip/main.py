# TODO здесь писать код
# first_text = input('Строка: ')
# second_text = input('Кортеж чисел: ')
def my_zip(first_text, second_text):
    new_text = [(first_text[i], second_text[i])
                for i in range(max(len(first_text), len(second_text)))
    ]
    return tuple(new_text)

first_text = 'abcd'
second_text = (10, 20, 30, 40)

new_text = my_zip(first_text,second_text)
for i in range(len(new_text)):
    print(new_text[i])
