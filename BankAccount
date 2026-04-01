"""
Crete a class to represent a bank account. Include attribute like account number , balance and methods like deposit , withdraw and check balance
"""


class BankAccount :
    def _init_(self, account_number , balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self , amount) :
        if amount > 0 :
            self.balance += amount
            print(f"Deposited rs{amount}")
        else :
            print("Invalid deposit amount")

    def withdraw(self, amount) :
        if amount > 0 and amount <= self.balance :
            self.balance -= amount
            print(f"Withdrawn rs{amount}")
        else :
            print("Insufficient balance or Invalid amount")

    def check_balance(self) :
        print(f"------------WC------------" f"\nCurrent Balance:{self.balance}" f"\n----------Ty----------")

account = BankAccount(101,5000)
account.deposit(30000)
account.withdraw(150)
account.check_balance()
