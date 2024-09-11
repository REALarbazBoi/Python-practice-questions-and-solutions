class MinimumBalanceError(Exception):
    pass

class Account:

    Acc_no = 1001

    def __init__(self, name, balance = 1000):
        if balance < 1000:
            raise MinimumBalanceError("Account cannot be created")
        self.name = name
        self.account_number = Account.Acc_no
        self.balance = balance
        Account.Acc_no += 1

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount < 1000:
            raise MinimumBalanceError("Amount can't be withdrawn")
        self.balance -= amount

    def show_details(self):
        print("Name: ", self.name)
        print("Account number: ", self.account_number)
        print("Balance: ", self.balance)


c1 = Account("Arbaz",2000)
c1.deposit(1000)
c1.withdraw(2000)
c1.show_details()
c2 = Account("Vikesh",3000)
c2.show_details()