class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance
    
    def show_balance(self):
        return self.__balance

acc = BankAccount("Aadil", 5000)
print(acc.show_balance())
# print(acc.__balance)  # Error
