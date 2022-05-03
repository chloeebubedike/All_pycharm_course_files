from bankaccount import BankAccount
# Create new class


class InsufficientFundsException(Exception):
    # pass in amount withdrawn
    # sep attribute to tell user how much they wouldve gone overdrawn
    def __init__(self, initial, amt):
        super().__init__(initial)
        self._amt = amt

    def raise_exception(self, amt):

        try:
            # Should class object be instantiated in try?
            self.withdraw(amt)

        # can we make our own except error names i.e. NameError
        except:
            print('Your account has insuffient funds')

        else:
            print('Your withdrawal has been approved')

        # Will always be executed
        finally:
            print('Thank you for using our bank services today')

suzy_bank_account = BankAccount(75)
print(suzy_bank_account.withdraw(100))