
chocolates = {'white': 1.50, 'milk': 1.20, 'dark': 1.80, 'vegan': 2.00}


def get_chocolate_price():
    chocolate_choice = input('Which chocolate do you want? ').lower()
    print(chocolates.get(chocolate_choice))


get_chocolate_price()
