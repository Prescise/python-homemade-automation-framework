from BalanceException import *

class Account:
    def __init__(self, initialAmount, clientName):
        self.balance = initialAmount
        self.name = clientName

    def getBalance(self):
        return self.balance
    
    def checkBalance(self, amount):
        try:
            self.balance >= amount
            return True
        except:
            raise BalanceException(
                f"retrait impossible solde insuffisant: '{self.balance}'$ "
            )
    
    def depositMoney(self, amount):
        self.balance += amount
    
    def withDraw(self, amount):
        try:
            self.checkBalance(amount)
            self.balance -= amount
        except BalanceException as error:
            raise BalanceException(
                f"operation  impossible solde insuffisant: {self.balance}$"
            )

    def payment(self, amount, account):
        try:
            self.checkBalance(amount)
            self.withDraw(amount)
            account.depositMoney(amount)
        except BalanceException as error:
            raise BalanceException(
                f"virement de {amount}$ impossible solde du compte de '{self.name}': {self.balance} $"
            )