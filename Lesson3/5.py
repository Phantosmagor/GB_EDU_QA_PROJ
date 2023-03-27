"""Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
 Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
  В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    6
    -> 5
"""
import random

n = int(input('введите количество элементов в массиве: '))
x = int(input('введите число , к которому будем искать ближайшее в массиве: '))
testlist = []
for i in range(n):
    testlist.append(random.randint(0, n))
print(testlist)


def nearest(list, target):
    return min(list, key=lambda x: abs(x - target))


print(f'число ближайшее к {x} :')
print(nearest(testlist, x))
