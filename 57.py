"""
Задача 57

Вычисление среднего значения списка

Задание:

Запросите у пользователя список чисел и вычислите их среднее значение.

Ответ:"""

numbers = input("Введите числа через пробел: ")
numbers_list = list(map(float, numbers.split()))

if numbers_list:
    average = sum(numbers_list) / len(numbers_list)
    print("Среднее значение: ", average)
else:
    print("Список пуст")
