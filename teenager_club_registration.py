def check_name(name):
    assert len(name) <= 40


def check_age(user_age):
    try:
        user_age = int(user_age)
    except ValueError:
        print("Wrong age format")
        exit()
    if age < 18 or age > 25:
        raise ValueError("Age outside the allowed parameters")


def check_email(email):
    if "@" not in email or email.count("@") > 1 or "." not in email:
        raise ValueError("Wrong email format")


# write a registration record into a new file
name = input('What is your name? ')
age = int(input('How old are you? '))
email = input('What is your email address? ')

check_age(age)
check_email(email)
check_name(name)


with open("registration_record.txt", "a+") as registration_file:
    registration_file.write(','.join([name, str(age), email]))

import re
email = "youri@sent.ie"
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

assert re.match(regex, email)