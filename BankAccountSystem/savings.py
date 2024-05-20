from interest import *

class SavingsAccount(InterestRewards):
    def __init__(self, initialAmount, accName):
        super().__init__(initialAmount, accName)
        self.fee=10

    def withdraw(self, amount):
        try:
            self.valid_transaction(amount + self.fee)
            self.initialAmount = self.initialAmount - (amount + self.fee)
            print("Withdraw completed in Savings Account")
            self.getbalance()
        except BalanceException as error:
            print(f"Withdraw Interrupted : {error}")