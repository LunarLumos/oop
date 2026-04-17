class PositiveNumber:
    def __set_name__(self, owner, name):
        self.name = name
    
    def __get__(self, obj, objtype=None):
        return obj.__dict__.get(self.name)
    
    def __set__(self, obj, value):
        if value <= 0:
            raise ValueError(f"{self.name} must be positive")
        obj.__dict__[self.name] = value

class Product:
    price = PositiveNumber()
    quantity = PositiveNumber()
    
    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity

p = Product(100, 5)
print(p.price)
# p.price = -10  # ValueError
