import random
N = int(input('Количество чисел в списке: '))


new_list =[random.randint(0,2) for _ in range(N)]
zip_list =[new_list[i] for i in range(N) if new_list[i] != 0]

print('Список до сжатия:', new_list)
print('Список после сжатия:', zip_list)

