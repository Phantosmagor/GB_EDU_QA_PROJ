"""Задача 2: Найдите сумму цифр трехзначного числа.

*Пример:*

123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) |
"""


enterthenumber = input('пожалуйста введите трехзначное число:')
pervrazr = int(enterthenumber[0])
vtrazr = int(enterthenumber[1])
trrazr = int(enterthenumber[2])

print(f"сумма цифр числа = {pervrazr+vtrazr+trrazr}")