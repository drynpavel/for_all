first_text = input('Первая строка: ')
second_text = input('Вторая строка: ')


buf_text = list(second_text)
chek = False
for index in range(len(second_text)):
    if ''.join(buf_text) != first_text:
        buf_text.append(buf_text.pop(0))
        print(buf_text)
    else:
        print('Первая строка получается из второй со сдвигом', index)
        chek = True
        break
if chek == False:
    print('Первую строку нельзя получить из второй с помощью циклического сдвига')




