"""
Задача 45

Вывод таблицы умножения

Задание:

Выведите таблицу умножения чисел от 1 до 10.

Ответ:"""

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i * j:4}", end='')
    print()
