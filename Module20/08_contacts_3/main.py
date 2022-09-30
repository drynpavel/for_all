# TODO здесь писать код
def add_people(people_book):
    family, name = input('Введите имя и фамилию нового контакта (через пробел):').split()
    if (family,name) in people_book:
        print('Такой человек уже есть в контактах')
        return people_book
    else:
        phone = input('Введите номер телефона: ')
        people_book[family,name] = phone
        return people_book


def find_people(people_book):
    family, name = input('Введите имя и фамилию нового контакта (через пробел):').split()
    if (family, name) in people_book:
        print(family, name, people_book[family,name])
    return 0

people_book = {}
while True:
    print('Введите номер действия:')
    print('1. Добавить контакт')
    print('2. Найти человека')
    choose = input()
    print(choose)
    if choose == '1':
        people_book = add_people(people_book)
    if choose == '2':
        people_book = find_people(people_book)
    print()