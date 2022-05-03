import getpass

pin = 1234
count = 1

while count < 4:
    supplied_pin = int(getpass.getpass("Enter Pin: "))
    if supplied_pin == pin:
        print("Correct Pin")
        break
    elif count < 3:
        print("Incorrect Pin, Try again - attempt", count, "of 3")
        count += 1
    else:
        print("Sorry - FAIL")