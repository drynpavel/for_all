## Задача 8. Развлечение
### Что нужно сделать
N палочек выставили в один ряд, пронумеровав их слева направо числами от 1 до N. Затем по этому ряду бросили K камней, при этом i-й камень сбил все палки с номерами от L_i до R_i включительно. Определите, какие палки остались стоять на месте.

~~~~
Напишите программу, которая получает на вход количество палок N и количество бросков K. Далее идёт K пар чисел Left_i, Right_i, при этом 1 ≤ Left_i ≤ Right_i ≤ N.

Программа должна вывести последовательность из N символов, где j-й символ есть “I”, если j-я палка осталась стоять, или “.”, если j-я палка была сбита.

Пример:

```
Количество палок: 10 
Количество бросков: 3
Бросок 1. Сбиты палки с номера 8 
по номер 10.
Бросок 2. Сбиты палки с номера 2 
по номер 5.
Бросок 3. Сбиты палки с номера 3 
по номер 6.

Результат: I.....I...
```
### Что оценивается
- Результат вычислений корректен.
- input содержит корректные приглашения для ввода. 
- Формат вывода соответствует примеру.
- Переменные и функции имеют значащие имена, не только a, b, c, d (подробнее об этом в видео 2.3).
