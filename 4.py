class Person:
    count = 0
    
    def __init__(self, name):
        self.name = name
        Person.count += 1
    
    @classmethod
    def get_count(cls):
        return cls.count

aadil = Person("Aadil")
miwo = Person("Miwo")
print(Person.get_count())
