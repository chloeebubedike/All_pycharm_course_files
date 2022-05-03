text = 'hello world'
#Counts number of 'o's
print(text.count('o'))

#Return boolean value is text starts with hel
if text.startswith('hel'):
    print("It starts with hel")

#
if text.isalpha():
    print('string is all alpha')

new_text = ' \t\r\n'
if new_text.isspace():
    print('string is whitespace')