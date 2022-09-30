# TODO здесь писать код
zakaz_dict = {}
sum_zakaz = int(input('Введите количество заказов: '))
for i in range(sum_zakaz):
    print(i+1, 'заказ:', end=' ')
    zakaz = input().split()
    if zakaz_dict.get(zakaz[0],{}).get(zakaz[1],None) == None:
        if zakaz_dict.get(zakaz[0]) == None:
            zakaz_dict[zakaz[0]] = {}
        zakaz_dict[zakaz[0]][zakaz[1]] = int(zakaz[2])
    else:
        zakaz_dict[zakaz[0]][zakaz[1]] += int(zakaz[2])

for klient in zakaz_dict:
    print(klient)
    for zakaz_pizza in zakaz_dict[klient]:
        print('\t',zakaz_pizza, ':', zakaz_dict[klient][zakaz_pizza])



