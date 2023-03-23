"""*Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
В случае с английским алфавитом очки распределяются
так:
A, E, I, O, U, L, N, S, T, R – 1 очко;
D, G – 2 очка;
B, C, M, P – 3 очка;
F, H, V, W, Y – 4 очка;
K – 5 очков;
J, X – 8 очков;
Q, Z – 10 очков.
А русские буквы оцениваются так:
А, В, Е, И, Н, О, Р, С, Т – 1 очко;
Д, К, Л, М, П, У – 2 очка;
Б, Г, Ё, Ь, Я – 3 очка;
Й, Ы – 4 очка;
Ж, З, Х, Ц, Ч – 5 очков;
Ш, Э, Ю – 8 очков;
Ф, Щ, Ъ – 10 очков.
Напишите программу, которая вычисляет стоимость введенного пользователем слова.
Будем считать, что на вход подается только одно слово, которое содержит либо только английские,либо только русские буквы.

*Пример:*

ноутбук
    12
"""
#Заводим словари
my_dict = {1: "AEIOULNSTR", 2: "DG", 3: "BCMP", 4: "FHVWY", 5: "K", 8: "JX", 10:"QZ"}
my_dict2 = {1: "АВЕИНОРСТ", 2: "ДКЛМПУ", 3: "БГЁЬЯ", 4: "ЙЫ", 5: "ЖЗХЦЧ", 8: "ШЭЮ", 10: "ФЩЪ"}
s = input('Введите слово: ').upper()    #Делаем все буквы Upper регистра, чтобы вводить можно было строчные
result = [key for letter in s for key, value in my_dict.items() if letter in value] #считаем балы за каждую букву для русского словаря
result2 = [key for letter in s for key, value in my_dict2.items() if letter in value]   #считаем балы за каждую букву для английского словаря
print(f'Сумма букв в английском языке: {sum(result)}')
print(f'Сумма букв в русском языке: {sum(result2)}')