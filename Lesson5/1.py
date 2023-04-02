"""
Задание 1. Написать программу, которая будет складывать, вычитать,
умножать или делить два числа. Числа и знак операции вводятся пользователем.
После выполнения вычисления программа не должна завершаться, а должна
запрашивать новые данные для вычислений. Завершение программы должно
выполняться при вводе символа '0' в качестве знака операции. Если пользователь
вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна
сообщать ему об ошибке и снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, / - ШАГ РЕКУРСИИ
- условие завершения рекурсии - введена операция 0 - БАЗОВЫЙ СЛУЧАЙ
Решите через рекурсию. В задании нельзя применять циклы.
Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):
"""
import operator

list_operators = {
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv}

def calculator (a, b, z):
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))

    if b == 0:
        print ("Ошибка ввода, нельзя делить на 0 ")
        b = int(input("Введите второе число: "))

    z = input("Введите знак умножения *, деления / или вычитания :")

    while z != '0' and z not in list_operators:
        print("Ошибка ввода")
        z = input("Введите знак умножения *, деления / или вычитания :")

    if z == '0':    # Пишем базовый случай рекурсии
        print('Конец игры')
    else:   # Рекурсивное условие
        print(list_operators[z](a, b))
        return(str(calculator (a, b, z)))

print(calculator(a, b, z)) #не успел! :(