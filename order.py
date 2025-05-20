class Order:

    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        if not isinstance(price, float):
            try:
                price = float(price)
            except ValueError:
                raise ValueError("The price has to be a float or a float-convertible number.")
        if not (1.0 <= price <= 10.0):
            raise ValueError("Price has to be between 1.00 and 10.00")
        self._price = price
        Order.all.append(self)
        
    @property
    def price(self):
        return self._price