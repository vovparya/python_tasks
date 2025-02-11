"""
Задача 40

Поменять местами наибольший и наименьший элементы списка

Задание:

Запросите у пользователя список чисел, найдите в нём наибольший и наименьший элементы и поменяйте их местами. Выведите полученный список.

Ответ:"""

numbers = input("Введите числа через пробел: ")
numbers_list = list(map(int, numbers.split()))

max_index = numbers_list.index(max(numbers_list))
min_index = numbers_list.index(min(numbers_list))

# Меняем местами
numbers_list[max_index], numbers_list[min_index] = numbers_list[min_index], numbers_list[max_index]

print("Результат:", numbers_list)
