"""
Задача 22

Максимальное из трёх чисел

Задание:

Попросите пользователя ввести три числа и выведите максимальное из них.

Ответ:"""

num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
num3 = float(input("Введите третье число: "))

max_num = max(num1, num2, num3)
print("Максимальное число:", max_num)
