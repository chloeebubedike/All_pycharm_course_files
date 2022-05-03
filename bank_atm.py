# drop in qs : how should atm program be structured? A number of functions with try block inside?

# where can I learn about how to structure unit tests? should I use ones from exceptions lesson?
# what does mock.patch() do?
# if unit test is a class why does it not start with a constructor method

# what makes you decide to use an assert over raising a specific exception

# notes to self:
# import mock and main from the module unittest
# import the functions you are testing
# use raise and assert in atm functions
# use multiple functions to represent multiple unit tests within the TestBank class
# class TestClass(TestCase)
#   def name_of_test(self):
# UNSURE WHAT THIS LINE MEANS
#       with mock.patch('builtins.input', return_value ='test value'):
#           name_of_program_testing()