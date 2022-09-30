# TODO здесь писать код
# competition_dict = {}
# заполняю справочник
number = int(input('Сколько записей вносится в протокол?'))
for i in range(number):
    print(i+1, 'запись:', end=' ')
    competition_dict[i] = input().split()

# number = 5
# competition_dict = {0: ['1', 'q'], 1: ['2', 'w'], 2: ['3', 'e'], 3: ['4', 'q'], 4: ['3', 'w']}

print('Итоги соревнований:')
# print(competition_dict)
win_list = [] #список победителей
for i in range(3):
# лист результатов соревнований в конце - максимальный результат
    max_rezult = sorted([competition_dict[z][0]
                        for z in range(len(competition_dict))
                         if competition_dict[z][1] not in win_list
    ])
    for index_step in range(number):# ищу первое появление этого результата и вывожу результат
        # print(competition_dict[index_step][0], '=', max_rezult[-1])
        if competition_dict[index_step][0] == max_rezult[-1] and competition_dict[index_step][1] not in win_list:
            print(i + 1, 'место -', competition_dict[index_step][1],'(', competition_dict[index_step][0],')')
            win_list.append(competition_dict[index_step][1])#веду список победителей чтобы не выбрать его второй раз
            break



