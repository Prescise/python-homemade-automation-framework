from bank_account import *

Dave = BankAccount(1000, "Dave")
Sarah = BankAccount(2000, "Sarah")

#Dave.getBalance()
##Sarah.getBalance()

#Dave.depositMoney(500)

Dave.transfer(50, Sarah)
