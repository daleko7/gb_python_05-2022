"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия. Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""

from sys import argv

script, time, payment, bonus = argv
time = int(time)
payment = int(payment)
bonus = int(bonus)
result = time * payment + bonus
print(f"Зарплата работника за {time} часов: {result} ")
