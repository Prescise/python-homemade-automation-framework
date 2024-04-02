from pytest import *
from  Account import *

class TestAccount:

    def test_get_balance(self):
        bank_acc = Account(1000, "Patrick")
        assert  bank_acc.getBalance() == 1000

    def test_deposit_money(self):
        bank_acc = Account(1000, "Patrick")
        bank_acc.depositMoney(50)
        assert  bank_acc.getBalance() == 1050

    def test_withdraw_succeed(self):
        bank_acc = Account(1000, "Patrick")
        bank_acc.withDraw(100) 
        assert bank_acc.getBalance() == 900

    def test_withdraw_fail(self):
        bank_acc = Account(1000, "Patrick")
        with raises(BalanceException):
            bank_acc.withDraw(1001)

    def test_check_balance_fail(self):
        bank_acc = Account(1000, "Patrick")
        with raises(BalanceException):
            bank_acc.checkBalance(1001)

    def test_check_balance_succeed(self):
        bank_acc = Account(1000, "Patrick")
        assert bank_acc.checkBalance(100) == True

    def test_transfer_fail(self):
        bank_acc = Account(0, "Patrick")
        sarah = Account(1000, "Sarah")
        with raises(BalanceException):
            bank_acc.payment(100, sarah)

    def test_transfer_succedd(self):
        bank_acc = Account(1500, "Patrick")
        sarah = Account(1000, "Sarah")
        bank_acc.payment(100, sarah)
        assert bank_acc.getBalance() == 1400
        assert sarah.getBalance() == 1100

