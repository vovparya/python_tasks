"""
Задача 36

Калькулятор с выбором операции

Задание:

Создайте простой калькулятор, который запрашивает у пользователя два числа и знак операции (+, -, *, /), затем выполняет соответствующую операцию и выводит результат.

Ответ:"""

num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
operation = input("Введите операцию (+, -, *, /): ")

if operation == '+':
    result = num1 + num2
    print(f"Результат: {result}")
elif operation == '-':
    result = num1 - num2
    print(f"Результат: {result}")
elif operation == '*':
    result = num1 * num2
    print(f"Результат: {result}")
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"Результат: {result}")
    else:
        print("Деление на ноль невозмоно!")
else:
    print("Некорректная операция")
