def min_divider(number):
    divider = 2
    while True:
        if number % divider == 0:
            return divider
        else:
            divider += 1


number = int(input('Введите число: '))
divider = min_divider(number)
print('Наименьший делитель, отличный от единицы:', divider)

