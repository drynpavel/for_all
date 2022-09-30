count_upper = 0
count_digit = 0

while True:
    input_password = input('Придумайте пароль: ')
    if len(input_password) < 8:
        print('Пароль ненадёжный. Попробуйте ещё раз.')
    else:
        for buf_text in input_password:
            if buf_text.isdigit():
                count_digit += 1
            elif buf_text.isupper():
                count_upper += 1
        if count_digit < 3 or count_upper < 1:
            print('Пароль ненадёжный. Попробуйте ещё раз.')
        else:
            print('Это надёжный пароль!')
            break
