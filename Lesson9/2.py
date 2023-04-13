"""1) реализовать дескрипторы для любых двух классов"""
class NonNegative:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Не может быть отрицательным')
        instance.__dict__[self.name] = value
    def __set_name__(self, owner, name):
        self.name = name
class Order:
    price = NonNegative()
    quantity = NonNegative()
    def __init__(self, name, price, quantity):
        self._name = name
        self.price = price
        self.quantity = quantity
    def total(self):
        return self.price * self.quantity


apple_order = Order('Яблоко', 1, 666)
apple_order.total() # 666
apple_order.price = 666  # ValueError: не может быть отрицательным
apple_order.quantity = 666   # ValueError: не может быть отрицательным