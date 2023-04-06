"""
Задание 1.

Создать класс TrafficLight (светофор)
и определить у него один приватный атрибут color (цвет) и публичный метод running (запуск).

В рамках метода running реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный)
составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение.
Для имитации "горения" каждого цвета испольщуйте ф-цию sleep модуля time

Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый).

Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""
import time

class TrafficLight:
    _color = None
    _colors = ['red', 'yellow', 'green']
    _timeouts = [7, 2, 4]

    def __init__(self):
        self._color = self._colors[0]
        self._timeout = self._timeouts[0]

def running():
    i = 0
    j = 0
    while i < 3:
        for el in TrafficLight._colors:
            print(el)
            i += 1
            time.sleep(TrafficLight._timeouts.__getitem__(j))
            j += 1


traffic = TrafficLight()
running()
