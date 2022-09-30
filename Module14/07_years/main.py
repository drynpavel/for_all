def find_year(year):
    str_year = str(year)
    for buf_year in str_year:
        if str_year.count(buf_year) > 2:
            print(year)
            return 1


first_year = int(input('Введите первый год: '))
second_year = int(input('Введите второй год: '))
print('Годы от', first_year,' до ',second_year, ' с тремя одинаковыми цифрами:')
for buf_year in range(first_year, second_year + 1):
    find_year(buf_year)
