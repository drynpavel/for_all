N = int(input('Введите длину списка: '))

new_list = [1 if i % 2 == 0 else i % 5 for i in range(N)]
print(new_list)
