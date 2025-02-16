"""
Задача 50

Подсчёт количества гласных и согласных

Задание:

Попросите пользователя ввести предложение и подсчитайте количество гласных и согласных букв в нём.

Ответ:"""

text = input("Введите предложение: ").lower()
vowels = "аеёиоуыэюяaeiouy"
consonants = "бвгджзйклмнпрстфхцчшщbcdfghjklmnpqrstvwxz"

vowel_count = sum(1 for char in text if char in vowels)
consonant_count = sum(1 for char in text if char in consonants)

print(f"Количество гласных: {vowel_count}")
print(f"Количество согласных: {consonant_count}")
