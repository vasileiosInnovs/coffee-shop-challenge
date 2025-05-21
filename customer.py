from order import Order

class Customer:
    
    all = []

    def __init__(self, name):
        self.name = name
        Customer.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError ("The name has to be a string!")
        if len(value) not in range(1, 16):
            raise ValueError ("Name has to be 15 letters long!")
        self._name = value

    def create_order(self, coffee, price):
        Order(self, coffee, price)

    def orders(self):
        return [order for order in Order.all if order.customer == self]

    @classmethod
    def most_aficionado(cls, coffee):
        from collections import defaultdict

        spending = defaultdict(float)

        for order in Order.all:
            if order.coffee == coffee:
                spending[order.customer] += order.price

        if not spending:
            return None

        return max(spending, key=spending.get)