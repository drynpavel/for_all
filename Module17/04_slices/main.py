alphabet = 'abcdefg'

new = alphabet[:]
print('1Копию строки:',alphabet[:])
print('2Элементы строки в обратном порядке.',alphabet[::-1])
print('3Каждый второй элемент строки (включая самый первый).',alphabet[0::2])
print('4Каждый второй элемент строки после первого.',alphabet[1::2])
print('5Все элементы до второго.',alphabet[:1])
print('6Все элементы начиная с конца до предпоследнего.',alphabet[len(alphabet) - 1:len(alphabet) - 2:-1])
print('7Все элементы в диапазоне индексов от 3 до 4 (не включая 4).',alphabet[3:4])
print('8Последние три элемента строки.',alphabet[len(alphabet) - 3:])
print('9Все элементы в диапазоне индексов от 3 до 4.',alphabet[3:5])
print('То же, что и в предыдущем пункте, но в обратном порядке.',alphabet[4:2:-1])
