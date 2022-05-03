# def add_vat(vat, prices):
#     """
#     Add commission to every price item in the provided iterable.
#
#     :param vat: float, vat percentage
#     :param prices: iterable, net prices as per customers' receipt
#     :return: list of prices with added vat
#     """
#     # Assert evaluates an expression that triggers an exception if evaluates to false
#     assert (len(prices) > 0 and vat > 0)
#
#     new_prices = [(price / 100 * vat) + price for price in prices]
#
#     # new_prices = []
#     # for price in prices:
#     #     new_prices.append(price + (price / 100 * vat))
#
#     return new_prices
#
#
# class MyException(Exception):
#     pass
#
#
# def return_item(l, i):
#     # assert ((l and i >= 0) or (not l and i < 0))
#     # Create a check with specific error message
#     # if we're trying to access first or last item
#     if i == 0 or i > len(l) - 1:
#         raise MyException("Trying to access first or last item!")
#     if type(l) is not list:
#         raise TypeError('Param is not a list')
#     if not l:
#         raise ValueError('Empty list')
#     if i < 0 or i >= len(l):
#         raise IndexError('Index out of bounds')
#     return l[i]
#
#
# # Homemade assert
# def my_assert(expr):
#     if not expr:
#         raise IndexError
#
# my_var = "y"
# # print(add_vat(21, [10, 100, "3", 4.21]))
# # print(add_vat(21, [10]))
# try:
#     print(return_item([12, 13, 14], 1))
# except ValueError:
#     print("Empty list !")
# except IndexError:
#     print("Index was out of bounds")
# except TypeError:
#     print("Must be a list")
# except MyException:
#     print("My exception !")
# else:
#     print("The code ran fine")
# finally:
#     print("something after")





####
# Create program requesting persons and writing them to a file
####


def check_name(name):
    assert len(name) <= 40


def check_age(age):
    try:
        age = int(age)
    except ValueError:
        print("Wrong age format")
        exit()
    if age < 0 or age > 150:
        raise ValueError("wrong age")


def check_email(email):
    if "@" not in email or email.count("@") > 1 or "." not in email:
        raise ValueError("Wrong email format")


# User input
# name = input("What's the person's name? : ")
# # Check the age is in proper format
# age = input("What's the person's age ? : ")
# email = input("What's the person's email? : ")
#
# # Data Validation
# check_name(name)
# check_age(age)
# check_email(email)
filename = "db.txt"
try:
    with open(filename, "r") as out_file:
        print(out_file.readlines())
except:
    print("Failed to open file")
else:
    with open(filename, "a") as out_file:
        out_file.write("new line")
finally:
    print("Program terminated")




