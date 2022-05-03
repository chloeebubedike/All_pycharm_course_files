import re

my_string = "she sells sea shells on the sea shore"

if re.search('ee', my_string):
    print("Found!")
else:
    print("Not found :(")

# how to regex an email

my_string = "emily@gmail.com"

if re.match('[\w\.-]+@[\w\.-]+\.\w{2,4}', my_string):
    print("Matches!")
else:
    print("Doesn't match :(")
