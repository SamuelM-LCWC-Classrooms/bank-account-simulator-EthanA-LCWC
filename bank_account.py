class Bank_account:
    def __init__(self, owner, balance = 0) -> None:
        self.__owner = owner
        self.__balance = balance
    def deposit(self, money):
        self.__balance = self.__balance + money
    def withdraw(self, money):
        if money <= self.__balance:
            self.__balance = self.__balance - money
        else:
            print("Insufficient funds")
    def get_owner(self):
        return self.__owner
    def set_owner(self, new_name):
        self.__owner = new_name
    def get_balance(self):
        return self.__balance
