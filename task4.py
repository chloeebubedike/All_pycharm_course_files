list_of_strings = ['cat', 'horse', 'elephant', 'dog']


def find_longest_word(list_of_words):
    longest_word = ''
    for word in list_of_words:
        current_length = len(word)
        if current_length > len(longest_word):
            longest_word = word
    return longest_word


chosen_word = find_longest_word(list_of_strings)

print(chosen_word)