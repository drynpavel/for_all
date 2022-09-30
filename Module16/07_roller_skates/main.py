skates = []
number_skates = int(input('Кол-во коньков: '))
for i in range(number_skates):
    print('Размер', i + 1,'-й пары:', end = ' ')
    skates.append(int(input()))
skates.sort()


count_people = 0
number_foot = int(input('Кол-во людей: '))
for i in range(number_foot):
    print('Размер ноги', i + 1,'-го человека:', end = ' ')
    foot = (int(input()))
    for i in range(len(skates)):
        if foot == skates[i] or foot <= skates[i]:
            skates.pop(i)
            count_people += 1
            break
print ('Наибольшее кол-во людей, которые могут взять ролики:', count_people)

