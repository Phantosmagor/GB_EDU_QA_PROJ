"""адача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
 Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
 Помогите Кате отгадать задуманные Петей числа."""

try:
    strange1 = int(input('Введите первое число от 0 до 1000:'))
    strange2 = int(input('Введите второе число от 0 до 1000:'))
    if strange1 > 1000 or strange1 < 0:
        print('Одно или оба ведённых числа находятся вне диапазона')
        raise Exception()
    elif strange2 > 1000 or strange2 < 0:
        print('Одно или оба ведённых числа находятся вне диапазона')
        raise Exception()
    else:
        pass
except ValueError:
    print('Введите числа, а не текст')
for i in range(strange1):  # пробегаюсь от нуля до введённого числа
    for j in range(strange2):  # пробегаюсь от нуля до введённого числа
        if strange1 == i + j and strange2 == i * j:  # Вполне очевидная математика
            print(i, j)
