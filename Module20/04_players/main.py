players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}

# TODO здесь писать код
new_list = []
for data_key in players:
    new_list.append(tuple((data_key[0], data_key[1],players[data_key][0],players[data_key][1],players[data_key][2])))
print(new_list)
