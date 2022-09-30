# TODO здесь писать код
import random
original_list = [random .randint(1,100)
    for _ in range(10)]
print(original_list)
new_list = []
for i in range(0,10,2):
    new_list.append(tuple(original_list[i:i+2]))
print(new_list)