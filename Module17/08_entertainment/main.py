sum_stick = int(input('Количество палок:'))
stick = ['I' for _ in range(sum_stick)]


sum_stones = int(input('Количество бросков:'))
for i in range(sum_stones):
    print('Бросок', i + 1, 'Сбиты палки с номера', end = ' ')
    fist_nomer = int(input(''))
    second_nomer = int(input('по номер: '))
    stick = ['.'
             if (i >= fist_nomer - 1 and i <= second_nomer - 1)
             else stick[i]
             for i in range(sum_stick)             ]
print('Результат: ',''.join(stick))

