Code smells are indicators of potential issues in a program's design. They aren't necessarily bugs but can make code harder to maintain, read, or extend. Below are some common code smells with corresponding Python examples:

---

### 1. Long Function

**Smell:** A function that does too much and becomes hard to understand.

```python
def process_order(order):
    print(f"Processing order {order.id}")
    subtotal = 0
    for item in order.items:
        subtotal += item.price * item.quantity
    tax = subtotal * 0.08
    discount = subtotal * 0.1 if order.customer.is_loyal else 0
    total = subtotal + tax - discount
    print(f"Subtotal: {subtotal}, Tax: {tax}, Discount: {discount}, Total: {total}")
    order.status = "Processed"
    order.customer.update_order_history(order)
    send_email(order.customer.email, "Your order has been processed.")
```

**Solution:** Break it into smaller functions.


### 2. Duplicated Code

**Smell:** The same or similar code appears in multiple places.

```python
def calculate_discounted_price(price, customer):
    discount = 0.1 if customer.is_loyal else 0
    return price - (price * discount)

def calculate_total(order):
    total = 0
    for item in order.items:
        discount = 0.1 if order.customer.is_loyal else 0
        total += item.price * (1 - discount)
    return total
```

**Solution:** Extract common logic into one function.


### 3. Large Class (God Object)

**Smell:** A class does too much and handles multiple responsibilities.

```python
class OrderManager:
    def __init__(self, orders):
        self.orders = orders

    def process_order(self, order):
        # Processes an order
        pass

    def save_order(self, order):
        # Saves order to database
        pass

    def generate_invoice(self, order):
        # Generates an invoice for the order
        pass

    def send_email(self, email, message):
        # Sends an email notification
        pass
```

**Solution:** Apply **Single Responsibility Principle (SRP)**; split responsibilities into multiple classes.


### 4. Primitive Obsession

**Smell:** Using basic data types instead of objects.

```python
class Customer:
    def __init__(self, name, email, address_street, address_city, address_zip):
        self.name = name
        self.email = email
        self.address_street = address_street
        self.address_city = address_city
        self.address_zip = address_zip
```

**Solution:** Replace primitives with objects.

```python
class Address:
    def __init__(self, street, city, zip_code):
        self.street = street
        self.city = city
        self.zip_code = zip_code

class Customer:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address
```


### 5. Feature Envy

**Smell:** A method excessively interacts with another class.

```python
class Order:
    def __init__(self, customer):
        self.customer = customer

    def apply_discount(self):
        if self.customer.is_loyal:
            return 0.1
        if self.customer.signup_date < "2020-01-01":
            return 0.05
        return 0
```

**Solution:** Move logic into the appropriate class.

```python
class Customer:
    def get_discount(self):
        if self.is_loyal:
            return 0.1
        if self.signup_date < "2020-01-01":
            return 0.05
        return 0

class Order:
    def __init__(self, customer):
        self.customer = customer
    
    def apply_discount(self):
        return self.customer.get_discount()
```


### 6. Switch Statements (Replace with Polymorphism)

**Smell:** Using a long conditional to determine behavior.

```python
class Animal:
    def make_sound(self, type):
        if type == "dog":
            return "Woof!"
        elif type == "cat":
            return "Meow!"
        elif type == "cow":
            return "Moo!"
```

**Solution:** Use polymorphism.

```python
class Animal:
    def make_sound(self):
        raise NotImplementedError

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class Cow(Animal):
    def make_sound(self):
        return "Moo!"
```


### 7. Data Clumps

**Smell:** Related data is always passed around together.

```python
def send_email(name, email, street, city, zip_code, message):
    print(f"Sending email to {name} at {email} residing at {street}, {city}, {zip_code} with message: {message}")
```

**Solution:** Group related data into a class.

```python
class Address:
    def __init__(self, street, city, zip_code):
        self.street = street
        self.city = city
        self.zip_code = zip_code

class Customer:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address

def send_email(customer, message):
    print(f"Sending email to {customer.name} at {customer.email} residing at {customer.address.street}, "
          f"{customer.address.city}, {customer.address.zip_code} with message: {message}")
```


### 8. Shotgun Surgery

**Smell:** A small change requires modifications in multiple places.

```
# If adding a field to Customer, changes must be made in:
# - Database model
# - Multiple functions handling orders
# - Email templates using customer data
```

**Solution:** Encapsulate related logic in a single place.


### 9. Inappropriate Intimacy

**Smell:** Two classes are too dependent on each other's internals.

```python
class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Order:
    def __init__(self, customer):
        self.customer = customer

    def get_customer_email(self):
        return self.customer.email   # Directly exposing internals
```

**Solution:** Provide an abstraction.

```python
class Customer:
    def __init__(self, name, email):
        self.name = name
        self._email = email  # Mark as private

    def get_email(self):
        return self._email
```


### 10. Lazy Class

**Smell:** A class that does too little and is unnecessary.

```python
class DiscountCalculator:
    def calculate_discount(self, order):
        return 0.1 if order.customer.is_loyal else 0
```

**Solution:** Inline this logic directly if it has no real benefit.

```python
discount = 0.1 if order.customer.is_loyal else 0
```

