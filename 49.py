"""
Задача 49

Замена местами первой и последней цифры числа

Задание:

Запросите у пользователя целое число и поменяйте местами его первую и последнюю цифру.

Ответ:"""

number = input("Введите целое число: ")

if len(number) <= 1:
    swapped_number = number
else:
    swapped_number = number[-1] + number[1:-1] + number[0]

print(f"Результат: {swapped_number}")
