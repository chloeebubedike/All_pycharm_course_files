#Import account class from account file
from account import Account
# Create bank account object for lisa

homer_account = Account(50)
# Instantiating an object of the class type Account
lisa_account = Account(500.00)

# Save Lisa account balance in variable
lisa_balance = lisa_account.getbalance()

# Print lisa balance
print("Lisa's balance is", lisa_balance)

# Create bart bank account
bart_account = Account(100.00)

# Save bart account balance in a variable
bart_balance= bart_account.getbalance()

# Print Bart balance
print("Bart's balance is", bart_balance)

lisa_account.deposit(250)

# Self means 50 is automatically withdrawn from Bart bank account
bart_account.withdraw(50)

print("Lisa's new account balance is ", lisa_account.getbalance(), ". Bart's new account balance is ", bart_account.getbalance())

print(homer_account)

total_balance = bart_balance + lisa_balance
print(total_balance)

#setter
homer_account.set_holder_name("Homer Simpson")

# getter

name = homer_account.get_holder_name()
print(name)

# property
desc = homer_account.__description = "Bad customer"
print(desc)
