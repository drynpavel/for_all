def sum_number(number):
    sum = 0
    while number != 0:
        sum += number % 10
        number //= 10
    return sum



def count_number (number):
    count = 0
    while number != 0:
        count += 1
        number //= 10
    return count

first_number = int(input('Введите число: '))

sum = sum_number(first_number)
count = count_number(first_number)

print('Сумма чисел:', sum)
print('Количество цифр в числе:',count )
print('Разность суммы и количества цифр:', sum - count)