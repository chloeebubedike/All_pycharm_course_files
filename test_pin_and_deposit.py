from unittest import TestCase, mock, main
from pin_and_deposit import enter_pin, withdraw_money


class TestBank(TestCase):
    def test_enter_pin_with_correct_pin_first_try(self):
        with mock.patch('builtins.input', return_value='1234'):
            result = enter_pin()
            self.assertTrue(result)

    def test_enter_pin_with_correct_pin_second_try(self):
        with mock.patch('builtins.input', side_effect=['4321', '1234']):
            result = enter_pin()
            self.assertTrue(result)

    def test_enter_pin_with_correct_pin_third_try(self):
        with mock.patch('builtins.input', side_effect=['4321', '4321', '1234']):
            result = enter_pin()
            self.assertTrue(result)

    def test_enter_pin_with_incorrect_pin(self):
        with mock.patch('builtins.input', side_effect=['4321', '4321', '4321']):
            result = enter_pin()
            self.assertFalse(result)

    def test_enter_pin_with_too_long_pin(self):
        with mock.patch('builtins.input', side_effect=['12345']):
            with self.assertRaises(AssertionError):
                enter_pin()


if __name__ == "__main__":
    main(argv=[''], exit=False)
