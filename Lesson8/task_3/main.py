"""
3. Задание на закрепление знаний по модулю yaml.
 Написать скрипт, автоматизирующий сохранение данных
 в файле YAML-формата.
Для этого:

Подготовить данные для записи в виде словаря, в котором
первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа —
это целое число с юникод-символом, отсутствующим в кодировке
ASCII(например, €);

Реализовать сохранение данных в файл формата YAML — например,
в файл file.yaml. При этом обеспечить стилизацию файла с помощью
параметра default_flow_style, а также установить возможность работы
с юникодом: allow_unicode = True;

Реализовать считывание данных из созданного файла и проверить,
совпадают ли они с исходными.
"""
import os
import yaml

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(CURRENT_DIR, 'file.yaml')
data = {
    'list': ['Potato', 'Beef', 'Onion', 'Carrot'],
    'int': 16,
    'dict_price': {'Potato': '60P-100P', 'Beef': '500P-750P', 'Onion': '30P-60p', 'Carrot': '17P-50P'}
}

with open(filename, 'w', encoding="utf-8") as textio:
    yaml.dump(data, textio, default_flow_style=False, allow_unicode=True)

with open(filename) as textio:
    print(textio.read())