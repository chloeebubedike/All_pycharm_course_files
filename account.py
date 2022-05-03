# Create class called Account
class Account:
    # Create variable to hold the number of bank accounts created
    numCreated = 0

    def __init__(self, initial):
        self._balance = initial
        Account.numCreated += 1
        self.__description = "n/a"
        self.__holder_name = "Unknown"

    def deposit(self, amt):
        self._balance += amt
        return

    def withdraw(self, amt):
        self._balance -= amt
        return

    def get_holder_name(self):
        return self.__holder_name

    # setter - write
    # could include validation logic
    def set_holder_name(self,name):
        self.__holder_name = name

    # Property for description
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.description = description

    def getbalance(self):
        return self._balance

    def __str__(self):
        return "Bank account is " + str(self._balance)

    def __add__(self, other):
        return self.getbalance() + other.getbalance()