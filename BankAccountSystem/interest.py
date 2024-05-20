from bank_account import *

class InterestRewards(BankAccount):
    def deposit(self, amount):
        self.initialAmount = self.initialAmount + (amount * 2)
        print("Deposit complete!!")
        self.getbalance()
