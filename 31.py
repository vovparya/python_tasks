"""Задача 31

Сумма нечётных чисел

Задание:

Найдите сумму всех нечётных чисел от 1 до n, где n вводится пользователем.

Ответ:"""

n = int(input("Введите число n: "))
total = 0

for i in range(1, n + 1, 2):
    total += i

print(f"Сумма нечётных чисел от 1 до {n}, равна, {total}")
