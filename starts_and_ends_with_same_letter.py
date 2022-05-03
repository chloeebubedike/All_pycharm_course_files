# using string slicing
def starts_and_ends_same(word):
    return word[0] == word[-1]


print(starts_and_ends_same('love'))


# using built in string methods
def starts_and_ends_same_2(word):
    first_letter = word[0]
    return word.endswith(first_letter)


print(starts_and_ends_same_2('donkeyed'))

from unittest import TestCase, main


class TestStartsAndEndsSame(TestCase):
    # check if it returns True when the word does start and end the same
    def test_valid_start_and_ends_same_returns_true(self):
        result = starts_and_ends_same("oreo")
        self.assertTrue(result)

    # check if it returns False when the word does not start and end the same
    def test_non_valid_start_and_ends_same_returns_false(self):
        result = starts_and_ends_same("orange")
        self.assertFalse(result)
