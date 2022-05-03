import re

my_string = "she sells sea shells on the sea shore"

# if there is any word longer than 7 characters a-z
if re.search('[a-z]{7}', my_string):
    print("Found!")
else:
    print("Not found")