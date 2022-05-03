from unittest import TestCase, main, mock


def check_pin():
    correct_pin = "1234"
    entered_pin = input("Please enter your PIN:")
    return correct_pin == entered_pin


class TestCheckPin(TestCase):
    def test_correct_pin_returns_true(self):
        with mock.patch('builtins.input', return_value='1234'):
            result = check_pin()
            self.assertTrue(result)

    def test_correct_pin_returns_false(self):
        with mock.patch('builtins.input', return_value='9999'):
            result = check_pin()
            self.assertFalse(result)

    # side effect allows us to mock user typing in multiple values
    # ma
    def test_correct_pin_returns_false_side(self):
        with mock.patch('builtins.input', side_effect=['9999', '1234']):
            result = check_pin()
            self.assertFalse(result)


# either is good for a sequence use side effect, for one value use return value
# use git examples for testing syntax
