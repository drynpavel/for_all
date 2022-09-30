# TODO здесь писать код
import random

max_number = int(input('Введите максимальное число: '))
conceived_number_list = []
proposed_number_list = []

while True:
    proposed_number_list.clear()
    for i in range(5):
        proposed_number_list.append(random.randint(1,max_number))
    proposed_number_list.sort()
    print('Нужное число есть среди вот этих чисел:', end=' ')
    for i in range(5):
        print( proposed_number_list[i], end=' ')
    print()
    answer = input('Ответ Артёма: ')#если да, то добавляю в список возможных чисел
    if answer.lower() == 'да' or answer.lower() == 'lf':
        for i in range(5):#если нет такого элемента в списке, то добавялю его
            if conceived_number_list.count(proposed_number_list[i]) == 0:
                conceived_number_list.append(proposed_number_list[i])
    elif answer.lower() == 'нет' or answer.lower() == 'ytn':#удалю из списка данные числа
        for i in range(5):#если нет такого элемента в списке, то удаляю его
            if conceived_number_list.count(proposed_number_list[i]) != 0:
                conceived_number_list.remove(proposed_number_list[i])
    elif answer.lower() == 'помогите' or answer.lower() == 'gjvjubnt':
        break

print('Артём мог загадать следующие числа:', end=' ')
for i in range(len(sorted(conceived_number_list))):
    print(conceived_number_list[i], end=' ')
