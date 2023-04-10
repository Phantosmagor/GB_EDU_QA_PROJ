"""
2. Задание на закрепление знаний по модулю json. Есть файл orders
в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий
его заполнение данными.

Для этого:
Создать функцию write_order_to_json(), в которую передается
5 параметров — товар (item), количество (quantity), цена (price),
покупатель (buyer), дата (date). Функция должна предусматривать запись
данных в виде словаря в файл orders.json. При записи данных указать
величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json()
с передачей в нее значений каждого параметра.

ПРОШУ ВАС НЕ УДАЛЯТЬ ИСХОДНЫЙ JSON-ФАЙЛ
ПРИМЕР ТОГО, ЧТО ДОЛЖНО ПОЛУЧИТЬСЯ

{
    "orders": []
}

вам нужно подгрузить JSON-объект
и достучаться до списка, который и нужно пополнять
а потом сохранять все в файл
"""
import os
import json

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


def write_order_to_json(item, quantity, price, buyer, date):
    filename = os.path.join(CURRENT_DIR, 'orders.json')

    #newfilename = os.path.join(CURRENT_DIR, 'neworders.json') #Фантазировал как открыть один файл, и сохранять в другой
    #при многократном вызове функции. Не допёр.

    with open(filename, encoding="utf-8") as fl:
        data = json.loads(fl.read())
        data['orders'].append({'item': item, 'quantity': quantity, 'price': price, 'buyer': buyer, 'date': date})

        with open(filename, "w", encoding="utf-8") as lof:
            json.dump(data, lof, indent=4, separators=(',', ': '), ensure_ascii=False)

        print(f'Данные добавлены в {filename}')

if __name__ == '__main__':
    write_order_to_json('Гордон Рамси - трёхзвездочный шеф', '11', '3500', 'Щербаков', '13.01.2020')
    write_order_to_json('Гордон Рамси - Ultimate home cooking ', '4', '2700', 'Сидоров', '27.03.2021')

