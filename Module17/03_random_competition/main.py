import random


first_command = [round(random.random() * 100, 2) for _ in range(20)]
second_command = [round(random.random() * 100, 2) for _ in range(20)]

only_win = [first_command[i] if first_command[i] >second_command[i]
            else second_command[i]
            for i in range(20)]
print('Первая команда:', first_command)
print('Вторая команда:', second_command)
print('Победители тура:', only_win)
