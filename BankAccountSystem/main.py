from bank_account import *
from interest import *
from savings import *

customer_1=BankAccount(1000, "Ananyaa")
customer_2=BankAccount(2000, "Ram")

customer_1.getbalance()
customer_2.getbalance()

customer_1.deposit(1000)
customer_1.getbalance()

customer_1.withdraw(500)

customer_1.transfer(500,customer_2)

customer_3 = InterestRewards(3000,"Hema")

customer_3.getbalance()
customer_3.deposit(500)
customer_3.transfer(500,customer_1)

customer_4 = SavingsAccount(5000,"Latha")
customer_4.getbalance()
customer_4.withdraw(500) # reduces additional fee of savings account
customer_4.transfer(100,customer_2)
