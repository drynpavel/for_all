# Антон, помимо программирования, также увлекается и географией, поэтому он решил связать эти две области и
# написать для своего проекта небольшую программу-навигатор.
#
# Пользователь вводит количество стран N, а затем N раз вводит страну и города, которые в этой стране находятся,
# в одну строку. После пользователь вводит три названия городов. Реализуйте такую программу и для каждого из
# трёх городов укажите, в какой стране он находится. Если такого города нет, то выведите соответствующее сообщение.
# TODO здесь писать код
def find_name_country(country, name_town):
    for name_country,list_town in country.items():
        for i in range(len(list_town)):
            if list_town[i] == name_town:
                return 'Город {} расположен в стране {}'.format(name_town, name_country)
    return 'По городу {} данных нет'.format(name_town)

country = {}
count_country = int(input('Количество стран: '))
for i in range(count_country):
    print(i + 1, 'страна', end =': ')
    info_country =input().split()
    country[info_country[0]] = info_country[1:]

for i in range(3):
    print(i + 1, ' город:', end=' ')
    name_town = input()
    print(find_name_country(country, name_town))



