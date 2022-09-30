first_class = []
second_class = []


# заполняю первый клас
for i in range(160, 176 + 1, 2):
    first_class.append(i)
#заполняю второй клас
for i in range(162, 180 + 1, 3):
    second_class.append((i))

print('Первый клас по росту', first_class)
print('второй клас по росту', second_class)

first_class.extend(second_class)
first_class.sort()

print('Отсортированный список учеников:', first_class)

