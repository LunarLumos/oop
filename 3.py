class Person:
    species = "Human"
    
    def __init__(self, name):
        self.name = name

aadil = Person("Aadil")
miwo = Person("Miwo")

print(aadil.species)
print(miwo.species)
print(Person.species)
