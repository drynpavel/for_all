# TODO здесь писать код

def is_prime(length_text):# генерю список спростыми числами
    prime_list = []
    for i in range(2,length_text): # простые числа начинаются с 2
        prime = True
        for buf in range(2, i //2 + 1):
            if i % buf == 0:
                prime = False
        if prime == True:
            prime_list.append(i)
    return prime_list

def crypto(input_text):
    return [input_text[i]
        for i in is_prime(len(input_text))
    ]

print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
