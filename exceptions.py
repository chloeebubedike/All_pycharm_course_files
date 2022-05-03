import math
# BROAD REASONS WHY YOU MIGHT GET AN EXCEPTION
# (1) Trying to refer to something that doesn't exist
# (2) Using a value that is inappropriate in some way

# CORE EXAMPLES OF EXCEPTIONS IN THIS FILE
# AttributeError (1)
# KeyError (1)
# IndexError (1)
# NameError (1)
# UnboundLocalError (1)
# TypeError (2)
# ValueError (2)
# ZeroDivisionError (2)
# OverflowError (2)
# FileNotFoundError (1)
# UnicodeEncodeError (2)
# ModuleNotFoundError (1)
# ImportError (1)

# BONUS EXAMPLES YOU CAN TRY IF YOU WISH
# PermissionError (2)
# IsADirectoryError (2)


# AttributeError - EXAMPLE
def produce_attribute_error():
    print(1.234.upper())


# KeyError
def produce_key_error():
    my_dictionary = {'name': 'Chloe', 'age': 23}
    my_dictionary['address']


# IndexError
def produce_index_error():
    favourite_snacks = ['almond slices', 'nachos', 'croissant']
    favourite_snacks[3]


# NameError
def produce_name_error():
    my_variable = "This is my variable"
    print(my_function)


# UnboundLocalError
counter = 0
def produce_unbound_local_error():
    counter += 1


# TypeError
def produce_type_error():
    return 4 / "2"


# ValueError
def produce_value_error():
    return math.sqrt(-1)


# ZeroDivisionError
def produce_zero_division_error():
    return 2 / 0


# OverflowError
def produce_overflow_error():
    return 5 * 10


# FileNotFoundError
def produce_file_not_found_error():
    with open('imaginary_file.txt', 'r') as imaginary_file:
        imaginary_file.read()


# UnicodeEncodeError
def produce_unicode_encode_error():
    return "ñ".encode('ascii')


# ModuleNotFoundError
def produce_module_not_found_error():
    import NumPy
    arr = np.array([1, 2, 3])


# ImportError
def produce_import_error():
    import ChloesModule
