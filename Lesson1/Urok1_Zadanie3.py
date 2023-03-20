"""
Задание 3.
Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""
inputnumber = int(input('Введите целое положительное число n:'))
makestrfromint =str(inputnumber)
x1 =int(makestrfromint+makestrfromint)
x2 =int(makestrfromint+makestrfromint+makestrfromint)
print(f"Считаем сумму выражения: n+nn+nnn:\n {makestrfromint}+{x1}+{x2} = {inputnumber+x1+x2}")