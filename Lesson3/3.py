"""
3. Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]

Далее необходимо собрать аналитику о товарах. Реализовать словарь,
в котором каждый ключ — характеристика товара, например название,
а значение — список значений-характеристик, например список названий товаров.

Пример:

{
“названия”: [“компьютер”, “принтер”, “сканер”],
“цены”: [20000, 6000, 2000],
“количества”: [5, 2, 7],
“ед”: [“шт.”]
}
"""

goods = []
svoistva = {'Название': '', 'Цена': '', 'Количество': '', 'Единица': ''}
analytics = {'Название': [], 'Цена': [], 'Количество': [], 'Единица': []}
n = 0
svoistva_ = None
control = None
while True:
    control = input("Для ввода данных - нажмите любую кнопку , для Выхода - введите q , для просмотра -введите "
                    "латинскую a: ")
    if control == 'q':
        break
    n += 1
    if control == 'a':
        print(f'\n Аналитика')
        for key, value in analytics.items():
            print(f'{key}: {value}')
    for i in svoistva.keys():
        svoistva_ = input(f'Введите свойство {i}: ')
        svoistva[i] = int(svoistva_) if (i == 'Цена' or i == 'Количество') else svoistva_
        analytics[i].append(svoistva[i])
    goods.append((n, svoistva))

