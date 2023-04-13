"""2)Реализовать метакласс, позволяющий создавать всегда один и тот же объект класса."""


class valeriimeta(type):
    _myattr = {}

    def call(mycl, *args, **kwargs):
        if mycl not in mycl._myattr:
            mycl._myattr[mycl] = super().call(*args, **kwargs)
        return mycl._myattr[mycl]

class newclass(metaclass=valeriimeta):
    def func1(self):
        print('Seems legit')
        pass

    def func2(self):
        print('Bad news, bro')
        pass


obj_1 = newclass()
obj_2 = newclass()
print('Сравним объекты obj_1 и obj_2 и вернём результат: ')
print(obj_1 is obj_2)