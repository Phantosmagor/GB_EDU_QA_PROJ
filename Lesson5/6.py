"""
В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
Решите через рекурсию. В задании нельзя применять циклы.
"""
import random
p = random.randint(1, 101)
print(p)

def ugadaika(k): # k - это количество попыток, в базовом варианте = 0
    n = int(input("Введите число от 0 до 100: "))
    i = 1+k
    if i == 10: #Базовый случай
        print(f'Загаданное число =', p)
    if n == p:
            print("Вы угадали!")
    # Рекурсивное условие
    while i != 10 and n != p:
        if n > p:
            print("Ваше число больше")
            return (str(ugadaika(k+1)))
        if n < p:
            print("Ваше число меньше")
            return (str(ugadaika(k+1)))
ugadaika(10)