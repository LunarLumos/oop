class Person:
    def __init__(self, name):
        self.name = name
    
    def say_hello(self):
        print(f"{self.name} says Hello!")

aadil = Person("Aadil")
aadil.say_hello()
