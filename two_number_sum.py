# write a function that accepts an array of numbers and an integer representing a target sum
# if any two numbers from the accepted number sum up to the target sum then your function should return them in an array
# in that order
# if no two numbers sum up to the target sum the function should return an empty array
from unittest import TestCase


def two_number_sum(list_of_numbers, sum_number):
    # create empty list
    result = []
    # while list of numbers is true (i.e. populated)
    while list_of_numbers:
        # take off last number from list
        number = list_of_numbers.pop()
        # minus specific number from aim number to get the other number
        other_number = sum_number - number
        # see if the other number is in the list
        if other_number in list_of_numbers:
            # if other number is in the list add it to the result list
            result.append((other_number, number))
    # return the result
    return result


print(two_number_sum([1, 2, 9], 10))


class TestTwoNumberNum(TestCase):
    def test_valid_returns_true(self):
        result = two_number_sum([1, 2, 9], 3)
        self.assertTrue(result)

    def test_invalid_returns_false(self):
        result = two_number_sum([1, 5, 6], 100)
        self.assertFalse(result)