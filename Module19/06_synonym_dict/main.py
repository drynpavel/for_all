# TODO здесь писать код
dict_sinonim = {}
# count_sinonim = int(input('Введите количество пар слов: '))
# for i in range(count_sinonim):
#     print(i + 1, 'пара:', end=' ')
#     current_sinonim = input().split('-')
#     print(current_sinonim)
#     dict_sinonim[current_sinonim[0]] = current_sinonim[1]
dict_sinonim = {'a':'b','c':'d','e':'f'}
print(dict_sinonim)
find = False
while True:
    enter_word = input('Введите слово: ').lower()
    for sin1,sin2 in dict_sinonim.items():
        if sin1.lower() == enter_word:
            print('Синоним: ', sin2)
            find = True
            break
        elif sin2.lower() == enter_word:
            print('Синоним: ', sin1)
            find = True
            break
    if find == True:
        break
    print('Такого слова в словаре нет.')

