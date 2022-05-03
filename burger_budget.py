# Input the price of a burger using input
price_of_burger = float(input("What is the price of an honest burger?"))

# Check if restaurant has a veggie option
vegetarian_option_available = input('Is there any veggie options on the menu? y/n? ')

has_veggie_option = vegetarian_option_available == 'y'

# Check whether the price is less than or equal to 10.00
is_under_ten_pounds = (price_of_burger <= 10.00)


# # Print the result
# print(f"Burger is within budget: {is_under_ten_pounds}")
#
# meets_criteria = is_under_ten_pounds and has_veggie_option
# print(f"We should go to this restaurant: {meets_criteria}")

if is_under_ten_pounds and has_veggie_option:
    print("This restaurant is a great choice!")
else:
    print("Probably not a good idea!")
