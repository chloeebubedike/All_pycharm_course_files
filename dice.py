import random
from unittest import mock


def roll_dice():
    print("rolling...")
    return random.randint(1, 6)

print(roll_dice())


# create mock object by creating a mock class object defined from the Mock library
# inside mock you can define a name for debugging purposes
# if you want to specify a return value, we have told the mock to return 3 everytime the mock roll_dice function is ran
mock_roll_dice = mock.Mock(name="roll dice mock", return_value=3)

# mock roll dice is a mock object
print(mock_roll_dice)


print(mock_roll_dice())

# we can force roll dice to have the mock_roll dice returned value by doing this:
roll_dice = mock_roll_dice
# also returns 3
print(roll_dice())

mock_roll_dice.assert_called()



