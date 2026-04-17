class Walker:
    def walk(self):
        return "Walking"

class Swimmer:
    def swim(self):
        return "Swimming"

class Duck(Walker, Swimmer):
    pass

d = Duck()
print(d.walk())
print(d.swim())
