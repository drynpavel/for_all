goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# TODO здесь писать код
for product in goods:
    id_product = goods[product]
    sum_tovar = 0
    sum_price = 0
    for current_store in store[id_product]:
        sum_tovar += current_store['quantity']
        sum_price += current_store['quantity'] * current_store['price']
    print('{} — {} штук, стоимость {} рубля'.format(product, sum_tovar, sum_price))

