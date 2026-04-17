class Person:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if len(value) < 2:
            raise ValueError("Name too short")
        self._name = value

aadil = Person("Aadil")
print(aadil.name)
aadil.name = "Aadil Ahmed"
print(aadil.name)
