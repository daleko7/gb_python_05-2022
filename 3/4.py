"""
4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо
выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
"""

def my_func(x, y):
    c = 1
    for i in range(abs(y)):
        c *= x
    if y>=0:
         return c
    else:
        c = 1 / c
        return c
print("Результат возведения: ", my_func(int(input("Введите число: ")), int(input("Введите отрицательную степень: "))))


