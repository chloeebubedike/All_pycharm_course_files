from bankaccount import BankAccount


class SavingsAccount(BankAccount):
    INTEREST_RATE = 0.5

    def __init__(self, initial, monthly_payments):
        super().__init__(initial)
        self._monthly_payments = monthly_payments
        self._yearly_interest = int(self._monthly_payments * (self.INTEREST_RATE * 12))

    def workout_yearly_interest_payment(self):
        self._yearly_interest = int(self._monthly_payments * (self.INTEREST_RATE * 12))

    def get_yearly_interest_payment(self):
        return self._yearly_interest



sukaina_savings_account = SavingsAccount(100, 30)
sukaina_savings_account.withdraw(80)
print('Sukaina has a balance of £{}'.format(sukaina_savings_account._balance))
print('Sukaina will have a yearly interest yield of {} on her monthly payments of £{}'.format(sukaina_savings_account._yearly_interest, sukaina_savings_account._monthly_payments))


# print(sukaina.workout_interest())