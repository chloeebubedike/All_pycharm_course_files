def withdraw(amount):
    balance = 100
    if amount > balance:
        raise ValueError("You can't withdraw more than you have in your account")
    new_balance = balance - amount
    return new_balance

try:
    amount = int(input("How much would you like to withdraw? "))
    new_balance = withdraw(amount)
except ValueError as error:
    print(error)
else:
    print(f"Withdrawal successful, new balance: {new_balance}")
finally:
    print("Thank you for using Emily's bank.")