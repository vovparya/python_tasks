"""
Задача 25

Сумма цифр числа

Задание:

Запросите у пользователя целое число и вычислите сумму его цифр.

Ответ:"""

number = input("Введите целое число: ")
sum_digits = 0

for digit in number:
    if digit.isdigit():
        sum_digits += int(digit)

print("Сумма цифр числа:", sum_digits)
