class BankAccount:

    def __init__(self, initial):
        self._balance = initial

    def deposit(self, amount):
        self._balance += amount
        return

    def withdraw(self, amount):
        if amount < self._balance:
            self._balance -= amount
        else:
            raise Exception('Insufficient Funds')
        # if statement for withdrawal. If not valid else raises an exception

    def get_balance(self):
        return self._balance

    def __str__(self):
        return 'Bank account with a balance of ' + str(self.get_balance())


mary_bank_account = BankAccount(2000)
mary_bank_account.deposit(200)
mary_bank_account.withdraw(2000)
print(mary_bank_account.get_balance())