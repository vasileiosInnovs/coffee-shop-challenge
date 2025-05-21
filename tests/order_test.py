import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from customer import Customer
from coffee import Coffee
from order import Order

alice = Customer("Alice")
bob = Customer("Bob")

latte = Coffee("Latte")
espresso = Coffee("Espresso")

o1 = Order(alice, latte, 4.5)
o2 = Order(alice, espresso, 3.0)
o3 = Order(bob, latte, 5.0)

print("Order.customer:", o1.customer.name)
print("Order.coffee:", o1.coffee.name)
print("Order.customer:", o2.customer.name)
print("Order.coffee:", o2.coffee.name)
