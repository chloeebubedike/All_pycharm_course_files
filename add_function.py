from unittest import TestCase, mock, main


def add(num1, num2):
    return num1 + num2

print(add(10, 1))

# unit test


class TestAdd(TestCase):
    def test_add(self):
        result = add(1, 2)
        self.assertEqual(result, 3)