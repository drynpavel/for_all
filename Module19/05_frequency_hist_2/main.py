# TODO здесь писать код
text = input('Введите текст: ')
# text = 'здесь что-то написано'
symvol_dict = {}
for symvol in text:
    if symvol_dict.get(symvol) == None:
        symvol_dict[symvol] = 1
    else:
        symvol_dict[symvol] += 1

print('Оригинальный словарь частот:')
for y_sym in sorted(symvol_dict):
    print(y_sym, ':', symvol_dict[y_sym])

invert_dict = {}
for frequency in symvol_dict:
    if invert_dict.get(symvol_dict[frequency]) == None:
        invert_dict[symvol_dict[frequency]] = [frequency]
    else:
        invert_dict[symvol_dict[frequency]].append(frequency)

for y_sym in sorted(invert_dict):
    print(y_sym, ':', invert_dict[y_sym])
