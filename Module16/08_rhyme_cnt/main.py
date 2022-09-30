quantity_people = int(input('Кол-во человек:'))
number = int(input('Какое число в считалке?'))
print('Значит, выбывает каждый', number ,'-й человек')
people = []
for i in range(quantity_people):
    people.append(i + 1)


index_start = 0
index_delete = 0
for circle in range(1, quantity_people ):
    print('\nТекущий круг людей:', people)
    print('Начало счёта с номера', people[index_start])
    index_delete =  index_start +  int(abs(len(people) - number)) - 1
    while index_delete + 1 > len(people):
        index_delete -= len(people)
    print('Выбывает человек под номером', people[index_delete])
    people.pop(index_delete)
    if index_delete + 1 > len(people):
        index_start = 0
    else:
        index_start = index_delete

print('Остался человек под номером', people[0])


