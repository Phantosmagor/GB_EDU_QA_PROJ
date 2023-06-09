"""
Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

*Пример:*

A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8
"""


def func(base, exp):
    if exp == 1:
        return base
    elif exp != 1:
        return base * func(base, exp - 1)


base = int(input('Введите число: '))
exp = int(input('Введите его степень: '))
print("Результат возведения в степень равен:", func(base, exp))
