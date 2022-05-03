# using slicing
def is_palindrome(word):
    return word == word[::-1]


print(is_palindrome('ooo'))


# using the list function reversed
def is_palindrome_2(word):
    return list(word) == list(reversed(word))


print(is_palindrome_2('donkey'))

# testing

from unittest import TestCase, main


# extend testcase imported from unit test
class TestIsPalindrome(TestCase):
    # check if it returns true when the word is palindrome
    def test_valid_palindrome_returns_true(self):
        result = is_palindrome("hannah")
        # assert that the result should be true because hannah is a palindrome
        self.assertTrue(result)

    def test_valid_palindrome_2_returns_true(self):
        result = is_palindrome_2("hannah")
        self.assertTrue(result)

    # check if it returns false when the word is not a palindrome
    def test_non_palindrome_returns_false(self):
        result = is_palindrome("donkeys")
        # assert that the result should be true because hannah is a palindrome
        self.assertFalse(result)

    def test_invalid_palindrome_2_returns_false(self):
        result = is_palindrome_2("donkey")
        self.assertFalse(result)

# if all tests works this makes sure that function works as expected