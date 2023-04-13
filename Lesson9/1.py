"""1) реализовать дескрипторы для любых двух классов"""
class DescPrinter(object):
    _val = 666

    def __get__(self, obj, objtype=None):
        print('Получаем...')
        return self._val

    def __set__(self, obj, val):
        print('Устанавливаем...')
        self._val = val

    def __delete__(self, obj):
        print('Удаляем ...')
        del self._val


class mycutefunction():
    x = DescPrinter()

i = mycutefunction()
i.x #Получаем 666

i.x = 100 #Устанавливаем 100
i.x #Получаем 100
del i.x #Удаляем 100

i.x #олучаем 666
print(i.x)