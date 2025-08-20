class Car:
    def __init__(self,name,model):
        self.name = name 
        self.model_year = model 
        self.wheel = 4 
    def view(self):
        print("The Model year of this ",self.name, "is ", self.model_year)
        print("It is a ",self.wheel, "Wheels car")

c1 =  Car("BMW",2016)
c2 =  Car("Audi",2018)

c1.view()
print("________________________________")
print(" ")
c2.view()

"""
We make a class Car as a blueprint where every car has a name, a model year, and 4 wheels by default. 
When we create two cars (c1 as BMW 2016 and c2 as Audi 2018), each car stores its own details. 
When we call the view() method, each car shows its own information, 
proving that objects keep their own data even though they are made from the same class.
"""
