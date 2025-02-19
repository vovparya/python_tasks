"""
Задача 55

Простые числа в заданном диапазоне

Задание:

Запросите у пользователя два числа и выведите все простые числа в этом диапазоне.

Ответ:"""

start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            print(f"Все простые числа в этом диапазоне: {num}")
