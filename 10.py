class Parent:
    def show(self):
        return "Parent"

class Child(Parent):
    def show(self):
        return "Child"

c = Child()
print(c.show())
