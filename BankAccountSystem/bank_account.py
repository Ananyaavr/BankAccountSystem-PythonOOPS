class BalanceException(Exception):
    pass

class BankAccount:
    # Constructor for the bank account details
    def __init__(self, initialAmount, accName):
        self.initialAmount = initialAmount
        self.accName = accName
        print("The Account is created successfully.")
        print(f"Account Name : '{self.accName}' Balance : {self.initialAmount}")

    def getbalance(self):
        print(f"\nAccount : {self.accName}\nBank account Balance report : ${self.initialAmount:.2f}")

    def deposit(self, amount):
        self.initialAmount = self.initialAmount + amount
        print("\nDeposited Successfully.")
        print(f"Balance of {self.accName}'s account: ${self.initialAmount:.2f}")

    def valid_transaction(self, amount):
        if self.initialAmount >= amount:
            return
        else:
            raise BalanceException(
                f"Sorry! Account {self.accName} only has a balance of ${self.initialAmount:.2f}"
            )

    def withdraw(self, amount):
        try:
            self.valid_transaction(amount)
            self.initialAmount = self.initialAmount - amount
            print("\n Withdraw complete.")
            self.getbalance()
        except BalanceException as error:
            print(f"Withdraw interrupted : {error}")

    def transfer(self, amount, account):
        try:
            print("******* Transaction starts ******* ")
            self.valid_transaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print(" Transaction is successfully made!!!")
        except BalanceException as error:
            print(f"Transaction interrupted : {error}")








