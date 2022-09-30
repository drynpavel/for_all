quantity_friend = int(input('Кол-во друзей: '))
quantity_promissory  = int(input('Долговых расписок: '))


debet_friend = []
for _ in range(quantity_friend):
    debet_friend.append(0)

for i in range(quantity_promissory):
    print(i + 1,'-я расписка')
    positive_index_debet = int(input('Кому: '))
    negative_index_debet = int(input('От кого: '))
    summ_money  = int(input('Сколько: '))

    debet_friend[positive_index_debet - 1] += summ_money
    debet_friend[negative_index_debet - 1] -= summ_money

print('Баланс друзей:')
for i in range(quantity_friend):
    print(i + 1,':', debet_friend[i])