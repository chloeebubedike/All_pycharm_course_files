word = 'Apple'
word_in_list = []
length_of_word = len(word)

while len(word_in_list) < len(word):
    word_in_list += word [length_of_word - 1]
    length_of_word = length_of_word -1

reversed_word = "".join(word_in_list)
print(reversed_word)

