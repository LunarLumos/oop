from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

aadil = Person("Aadil", 22)
print(aadil)
