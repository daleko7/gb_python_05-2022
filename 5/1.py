"""
1. Создать программный файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая
строка.
"""

file = open("1.txt", "w", encoding="utf-8")
data = ("a")
while data:
    data = str(input("Введите данные для записи в файл или оставьте строку пустой и нажмите Enter для заверщения ввода: "))
    file.writelines(data)
    if not data:
        break

file.close()