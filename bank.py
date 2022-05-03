def enter_pin():
    # prompt user for pin code
    user_pin = 1234
    entered_pin = input('What is your pin number? ')
    assert len(str(entered_pin)) == 4

    if user_pin == int(entered_pin):
        return True

    pin_attempts = 1
    # if pin is not correct ask for pin again x3 and then exit
    while pin_attempts < 3:
        entered_pin = int(input('Incorrect number detected. What is your pin number? '))
        if user_pin == entered_pin:
            return True
        pin_attempts += 1

    print('You have run out of pin attempts')
    return False


# if pin is correct proceed
def withdraw_money():
    # set account balance to 100
    account_balance = 100
    # allow the user to specify the amount of money they want to withdraw
    withdraw_amount = int(input('How much would you like to withdraw? '))
    # submit withdraw amount from balance and display the remaining balance
    remaining_balance = account_balance - withdraw_amount
    # If user asks to withdraw more money that they have in their account, it should raise an error
    if withdraw_amount <= account_balance:
        print("Your remaining balance is: £{}".format(remaining_balance))
    else:
        raise ValueError("Sorry, you have insufficient funds")


def run_bank():
    if enter_pin():
        try:
            withdraw_money()
            # caught Value Error from withdraw money function
        except ValueError as error:
            print(error)


run_bank()