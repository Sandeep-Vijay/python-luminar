#bank

class Bank:
    bankName='SBI'
    def __init__(self,accno):
        self.accno=accno
        self.balance=0
    def deposit(self,amt):
        self.amt=amt
        self.balance=self.balance+self.amt
        print('your',Bank.bankName,'account has been credited with an amount of',self.amt)
        print('the available balance amount is',self.balance)
    def withdraw(self,amount):
        self.amount=amount
        if self.amount>self.balance:
            print('insufficient balance')
        else:
            self.balance=self.balance-self.amount
            print('your account has been debited with an amount of',self.amount)
            print('the available balance amount is',self.balance)
A1=Bank(12345)
A1.withdraw(90)
A1.deposit(1500)
A1.withdraw(500)
A1.deposit(1000000000)