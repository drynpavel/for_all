def reverse_number(number):
    integer_number = int(round(number,0))
    buf_number =0
    while integer_number != 0:
        buf_number += integer_number % 10
        integer_number //= 10
        if integer_number != 0:
            buf_number *= 10
    return buf_number


def fraction_to_int(number):
    count = 0
    while number - round(number,0) != 0:
        number *= 10
        count += 1
    number = reverse_number(number)
    for i in range(1, count + 1):
        number /= 10
    return number

first_number = float(input('Введите первое число: '))
second_number = float(input('Введите второе число: '))
reverse_first_number = reverse_number(round(first_number,0))+ fraction_to_int(round(first_number - round(first_number,0),5))
reverse_second_number = reverse_number(round(second_number,0))+ fraction_to_int(round(second_number - round(second_number,0),5))
print('Первое число наоборот:', reverse_first_number)
print('Второе число наоборот:', reverse_second_number)
print('Сумма:', reverse_first_number + reverse_second_number)




