quantity_number = int(input('Кол-во чисел: '))
quantity = []

for i in range(quantity_number):
    quantity.append(int(input('Число: ')))
print('Последовательность: ',quantity)
i = 0
while quantity != quantity[::-1]:
    quantity.insert(quantity_number, quantity[i])
    i += 1
print('Нужно приписать чисел:',i)
print('Сами числа:',quantity[:i][::-1])