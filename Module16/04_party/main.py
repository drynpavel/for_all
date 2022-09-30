guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

def add_guest(name_guest):
    if len(guests) == 6:
        print('Прости,', name_guest, ' , но мест нет.')
    else:
        guests.append(name_guest)


def exit_guest(name_guest):
    print('Пока,', name_guest,'!')
    guests.remove(name_guest)

operation = ''
while True:
    print('Сейчас на вечеринке', len(guests) ,' человек: ', guests)
    operation = input('Гость пришёл или ушёл? ')
    if operation == 'Пора спать':
        break
    name_guest = input('Имя гостя: ')

    if operation == 'пришёл':
        add_guest(name_guest)
    elif operation == 'ушёл':
        exit_guest(name_guest)

print('Вечеринка закончилась, все легли спать.')
