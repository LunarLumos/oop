class Account:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
    
    def get_balance(self):
        return self.__balance

aadil_acc = Account("Aadil", 1000)
aadil_acc.deposit(500)
aadil_acc.withdraw(200)
print(aadil_acc.get_balance())
