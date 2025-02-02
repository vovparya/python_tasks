"""
Задача 21

Квадратное уравнение

Задание:

Напишите программу, которая принимает коэффициенты a, b и c квадратного уравнения ax^2 + bx + c = 0 и вычисляет его корни.

Ответ:"""

import math

a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

discriminant = b ** 2 - 4 * a * c

if discriminant > 0:
    x1 = (-b + math.sqrt(discriminant)) / (2 * a)
    x2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print("Два корня: x1 =", x1, ", x2 =", x2)
elif discriminant == 0:
    x = -b / (2 * a)
    print("Один корень: x =", x)
else:
    print("Корней нет")
