"""Задача 33

Проверка палиндрома

Задание:

Проверьте, является ли введённая пользователем строка палиндромом (читается одинаково слева направо и справа налево).

Ответ:"""

text = input("Введите строку: ")
if text == text[::-1]:
    print("Строка является палиндромом")
else:
    print("Строка не является палиндромом")
