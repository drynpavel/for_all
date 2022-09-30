shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]


name_detal = input('Название детали: ')

count_detal = 0
total_price = 0
for i in range(len(shop)):
        if shop[i][0]  == name_detal:
                count_detal += 1
                total_price += shop[i][1]

print('Кол-во деталей — ', count_detal)
print('Общая стоимость -', total_price)
