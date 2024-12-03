class Bank_account:
    def __init__(self, owner) -> None:
        self.owner = owner
        self.balance = 0
    def deposit(self, money):
        self.balance = self.balance + money
    def withdraw(self, money):
        if money <= self.balance:
            self.balance = self.balance - money
        else:
            print("Insufficient funds")
    def get_balance(self):
        return self.balance
