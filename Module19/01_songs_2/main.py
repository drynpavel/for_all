violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

# TODO здесь писать код
sum_sound = 0
count_song = int(input('Сколько песен выбрать?: '))
for i in range(count_song):
    print('Название', i + 1, ' песни', end=' ')
    name_song = input()
    sum_sound += violator_songs.get(name_song, 0)
print('Общее время звучания песен %.2f' % sum_sound)

