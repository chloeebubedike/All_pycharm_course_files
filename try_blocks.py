def enter_pin():
    # prompt user for pin code
    user_pin = 1234
    entered_pin = int(input('What is your 4-digit pin number? '))
    assert len(str(entered_pin)) == 4
    if user_pin == entered_pin:
        return True


enter_pin()

