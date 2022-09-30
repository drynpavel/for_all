# TODO здесь писать код
def slicer (input_tuple,number):
    count_number = input_tuple.count(number)
    if  count_number == 0:
        return tuple
    elif count_number == 1:
        return  input_tuple[input_tuple.index(number):]
    else:
        return input_tuple[input_tuple.index(number):input_tuple.index(number,count_number) + 1]





print(slicer((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), 2))