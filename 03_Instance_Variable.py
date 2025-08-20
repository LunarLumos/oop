class House:
    def __init__(self):
        self.windows = 4    # Instance Variable
        self.door = 2       # Instance Variable

    def view(self):
        print("[+]",self.windows,"Windows", self.door, "Doors")

House1 = House()
House2 = House()

House1.view()
House2.view()

print("[-] Update the default door of House 2.")
House2.door = 3

House2.view()

""" 
We create a class House as a blueprint, where every house starts with 4 windows and 2 doors.
 We then make two houses (House1 and House2), and both begin with the same features. 
 When we change the doors of House2 to 3, only that house changes while House1 still has 2 doors. 
 This shows us that in OOP, each object made from a class has its own separate data.
 """