"""Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

*Пример:*

3 2 4 -> yes
3 2 1 -> no
"""
n = int(input('введите размер n от шоколадки: '))
m = int(input('введите размер m от шоколадки: '))
k = int(input('ввелите число долек , которые хотите отломить от шоколадки:'))

print(f"Исходные данные по шоколадке:\n Размеры: {n}x{m}\n Количество долек, которые хотим отломить: {k}")

if k <= n*m and (k%m==0 or k%n==0):
    print(f"Шоколадку можно поделить!")
else:
    print(f"Шоколадку нельзя поделить :(")