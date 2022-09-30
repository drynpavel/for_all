# TODO здесь писать код
def tpl_sort(input_tuple):
    for i in input_tuple:
        if type(i) != int:
            return input_tuple
    return tuple(sorted(list(input_tuple)))


print(tpl_sort((6, 3, -1, 8, 4, 10, -5)))