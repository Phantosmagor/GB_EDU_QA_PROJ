"""Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое
количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
*Пример:*

6 -> 1  4  1
24 -> 4  16  4
    60 -> 10  40  10
"""
vsego = int(input('Введите сколько журавликов было сделано:'))
petya = vsego//6
serj = vsego//6
katya = (petya+serj)*2
print(f"Кто же и сколько сделал журавликов?:\n"
      f" Петя сделал: {petya}\n Катя сделала: {katya}\n Сережа сделал: {serj}\n")

#Конечно можно было и в принте всё это делать, но так очевиднее