# TODO здесь писать код
family_list = {
    ("Сидоров", "Никита"): (30),
    ("Сидорова", "Алина"): (45),
    ("Сидоров", "Павел"): (12),
    ("Иванов", "Антон"): (99)
}

input_family = input('Введите фамилию: ')
for family in family_list:
    if input_family.lower() in str(family[0]).lower():
        print(str(family[0]), str(family[1]), str(family_list[family]))

