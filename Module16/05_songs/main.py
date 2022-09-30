violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]


total_sound = 0
quantity_songs = int(input('Сколько песен выбрать? '))
for i in range(quantity_songs):
    print('Название', i + 1, 'песни:', end = ' ')
    name_song = input('')
    for x in range(len(violator_songs)):
        if violator_songs[x][0] == name_song:
            total_sound += violator_songs[x][1]

print('Общее время звучания песен:', total_sound ,' мин')

