# TODO здесь писать код


kolvo_people = int(input('Введите количество человек: '))
family_tree = {}
input_members = []
for i in range(kolvo_people - 1):
    print(i + 1, 'пара:', end=' ')
    input_members = input().split()
    if family_tree.get(input_members[1]) == None: # если нет такого родителя? Добавляю родителя
        family_tree[input_members[1]] = i
    family_tree[input_members[0]] = family_tree.get(input_members[1]) + 1  # добавляю потомка
    print(family_tree)

print()
print('«Высота» каждого члена семьи:')
print_member = []
print_member = family_tree.keys()
for name in sorted(print_member):
    print(name, ':', family_tree[name])


