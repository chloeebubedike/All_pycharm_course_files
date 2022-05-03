names = ["Gabby", "CJ", "Salima"]
names_string = ""
for item in names:
    names_string = names_string + item + " "

print(names_string)

name = "Teddy"
if 'ed' in name:
    print('Ed is in Teddy')

text = 'hello world'
print(text.count('o'))

if text.startswith('hell'):
    print('Hell is here')

# Does not print because of spaces
if text.isalpha():
    print('string is all alpha')

#The string is entirely whitespace
text = ' \t\r\n'
if text.isspace():
    print('string is whitespace')