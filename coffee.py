from order import Order

class Coffee:
    
    all = []

    def __init__(self, name):
        if not isinstance(name, str):
            raise ValueError("Name has to be a string!")
        if len(name) < 3:
            raise ValueError("Name has to be more than 3 characters long!")
        self._name = name
        Coffee.all.append(self)

    @property
    def name(self):
        return self._name
    
    def num_orders(self):
        return len([order for order in Order.all if order.coffee == self])
    
    def average_price(self):
        orders = [order for order in Order.all if order.coffee == self]
        if not orders:
            return 0
        sum_price = sum(order.price for order in orders)
        total_orders = len(orders)
        return sum_price / total_orders
