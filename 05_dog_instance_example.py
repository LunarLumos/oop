class Dog:
    def __init__(self,name,color):
        self.name = name 
        self.color = color
    
    def update_color(self, color):
        self.color = color

    def poke(self):
        print(self.color, self.name, "is smiling!")
    
    def view(self):
        print(self.name ,"Is",self.color,"color")

#=====================End of class=====================

d1 = Dog("Rover","Brown")
d2 = Dog ("Tony","Orenge")

d2.poke()

d1.view()

print(" ")
print("Let change the color of", d1.name)
d1.update_color("Ginger")
d1.poke()

print(" ")
print("Print the valo of all attribute value of Dog 1.")
print(d1.__dict__)


"""
We create a class Dog as a blueprint where every dog has a name and color. 
We can also update the color with update_color(), make the dog “smile” with poke(), and show its details with view(). 
When we make two dogs (d1 as Rover/Brown and d2 as Tony/Orange),
 each keeps its own data. We then call their methods to see their colors and names, 
 change Rover’s color to Ginger, and finally use dict` to print all of Rover’s attributes. 
This shows us how instance variables are unique for each object and can be updated individually.
"""