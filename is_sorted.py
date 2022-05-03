# check if a word is sorted in alphabetical order
# built in function sorted
def is_sorted(word):
    return list(word) == list(sorted(word))


print(is_sorted('ably'))


# for loop
def is_sorted_2(word):
    for index in range(len(word[:-1])):
        if word[index] > word[index + 1]:
            return False
    return True

print(is_sorted_2("able"))

from unittest import TestCase, main


class TestIsSorted(TestCase):
    def test_valid_word_is_sorted_returns_true(self):
        result = is_sorted("ably")
        self.assertTrue(result)

    def test_invalid_word_is_sorted_returns_false(self):
        result = is_sorted("able")
        self.assertFalse(result)
