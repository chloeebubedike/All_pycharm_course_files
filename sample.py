from dice import roll_dice
from unittest import mock

def guess_number(num):
    mock_roll_dice = mock.Mock(name="roll dice mock", return_value=3)
    roll_dice = mock_roll_dice
    result = roll_dice()
    if result == num:
        return "You won!"
    else:
        return "You lost!"