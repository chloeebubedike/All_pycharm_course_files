from unittest import TestCase, main


# built-in len function
def contains_duplicate_letter(word):
    return len(word) > len(set(word))


print(contains_duplicate_letter("pasta"))


# built in string methods
def contains_duplicate_letter(word):
    for char in word:
        # find position of the first time a word appears
        # rfind - find position of the last time a word appears
        if word.find(char) != word.rfind(char):
            return True
    return False


print(contains_duplicate_letter("pasta"))


# unit tests
class TestContainsDuplicate(TestCase):
    def test_valid_word_contains_duplicate_returns_true(self):
        result = contains_duplicate_letter("banana")
        self.assertTrue(result)

    def test_invalid_word_contains_duplicate_returns_false(self):
        result = contains_duplicate_letter("project")
        self.assertFalse(result)
