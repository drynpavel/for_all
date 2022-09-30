first_list = []
second_list = []

for i in range(3):
    print('Введите', i + 1,'-е число для первого списка', end = ' ')
    first_list.append(input(''))
for i in range(7):
    print('Введите', i + 1,'-е число для второго списка', end = ' ')
    second_list.append(input(''))


print('Первый список:', first_list)
print('Второй список:', second_list)

first_list.extend(second_list)
unique_list = list(set(first_list))
print('Новый первый список с уникальными элементами: ', unique_list)
