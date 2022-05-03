import unittest
from dice import roll_dice
from sample import guess_number

class MyTestCase(unittest.TestCase):
    def test_guess_number(self):
        assert guess_number(3) == "You won"


if __name__ == '__main__':
    unittest.main()
