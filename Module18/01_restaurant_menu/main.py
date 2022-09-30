#menu_text = input('Ведие меню с разделителем точка с запятой: ')
menu_text = 'утиное филе;фланк-стейк;банановый пирог;плов'


print('Доступное меню: ',menu_text)
menu_list = menu_text.split(';')
print('На данный момент в меню есть:', ', '.join(menu_list))
