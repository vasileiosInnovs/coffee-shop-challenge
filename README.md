# coffee-shop-challenge

---

# ☕ Coffee Ordering System (Python OOP Project)

This is a simple object-oriented Python project that simulates a coffee ordering system. It models the relationships between **customers**, **coffees**, and **orders**, while demonstrating class design, encapsulation, and object relationships — including a many-to-many association.

---

## 📦 Project Overview

* A **Customer** can place multiple orders.
* A **Coffee** can be ordered many times.
* An **Order** links a Customer to a Coffee at a specific price.

➡️ This means **Customer ↔ Coffee** is a **many-to-many** relationship, implemented through the `Order` class.

---

## 🧠 Core Design Principles

* ✅ **Single source of truth**: `Order.all` is the only place where all order data is stored.
* ✅ **Data integrity**: Validations are enforced (e.g., price range, name length).
* ✅ **Encapsulation**: Uses Python's `@property` and private attributes.

---

## 🧱 Class Breakdown

### 👤 Customer

```python
Customer(name: str)
```

* Name must be a string with **1 to 15 characters**
* Stored as a property with a getter/setter

#### 🔹 Methods

| Method                             | Description                                                                    |
| ---------------------------------- | ------------------------------------------------------------------------------ |
| `create_order(coffee, price)`      | Creates a new `Order` for the given coffee and price                           |
| `Customer.most_aficionado(coffee)` | Class method that returns the customer who spent the most on a specific coffee |

---

### ☕ Coffee

```python
Coffee(name: str)
```

* Name must be a string with **at least 3 characters**
* Name is **read-only** after initialization

#### 🔹 Methods

| Method            | Description                                             |
| ----------------- | ------------------------------------------------------- |
| `num_orders()`    | Returns the number of orders for this coffee            |
| `average_price()` | Returns the average price of all orders for this coffee |

---

### 🧾 Order

```python
Order(customer: Customer, coffee: Coffee, price: float)
```

* Links a `Customer` and a `Coffee`
* Price must be a float between **1.00 and 10.00**
* All instances stored in `Order.all`

#### 🔹 Properties

| Property | Description           |
| -------- | --------------------- |
| `price`  | Read-only float value |

---

## 🔁 Relationships Summary

| Entity            | Relationship                           |
| ----------------- | -------------------------------------- |
| Customer          | has many Orders                        |
| Coffee            | has many Orders                        |
| Order             | belongs to one Customer and one Coffee |
| Customer ↔ Coffee | Many-to-many (via Order)               |

---

## 📊 Example Usage

```python
# Create customers and coffee
alice = Customer("Alice")
bob = Customer("Bob")
latte = Coffee("Latte")

# Create orders
alice.create_order(latte, 4.5)
bob.create_order(latte, 5.0)
bob.create_order(latte, 4.0)

# Queries
print(latte.num_orders())                # Output: 3
print(latte.average_price())            # Output: 4.5
print(Customer.most_aficionado(latte))  # Output: <Customer Bob>
```

---

## 🗂 Suggested File Structure

```
coffee-shop-challenge/
├── customer.py
├── Pipfile 
├── debug.py 
├── coffee.py
├── order.py   
├── README.md
└── tests/       # for manual testing
    ├── customer_test.py 
    ├── coffee_test.py 
    └── order_test.py
```

---

## 🚀 Learning Goals

* Practice **OOP fundamentals**: classes, methods, classmethods, and properties
* Understand **many-to-many relationships** in code
* Learn how to manage **clean, validated object design**
* Reinforce single-source-of-truth architecture using shared class lists

---

## 🧪 Optional Enhancements

Want to go further?

* Add filtering methods like `Customer.orders()` or `Coffee.customers()`
* Create CLI or GUI to place and view orders
* Write unit tests using `unittest` or `pytest`

---

Let me know if you'd like this turned into an actual codebase structure or GitHub repo format!
