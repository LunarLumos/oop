class Person:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    @name.deleter
    def name(self):
        print("Deleting name")
        del self._name

aadil = Person("Aadil")
del aadil.name
