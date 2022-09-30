students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def f(dict):
    list_interest = [dict[i]['interests']
        for i in dict
    ]
    length_family = 0
    for i in dict:
        length_family += len(dict[i]['surname'])
    return list_interest, length_family


pairs = [(i, students[i]['age'])
    for i in students
]
print('Список пар "ID студента — возраст":', pairs)

list_interest, lenght_family  = f(students)
print('Полный список интересов всех студентов:', list_interest)
print('Общая длина всех фамилий студентов:', lenght_family)
