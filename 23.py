class Person:
    __slots__ = ['name', 'age']
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

aadil = Person("Aadil", 22)
print(aadil.name)
# aadil.city = "NYC"  # Error
