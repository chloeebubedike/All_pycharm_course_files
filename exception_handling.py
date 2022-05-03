def return_item(l, i):
    # assert ((l and i >= 0) or (not l and i < 0))
    if type(l) is not list:
        raise TypeError('Param is not a list')
    if not l:
        raise ValueError('Empty list')
    if i < 0 or i >= len(l):
        raise IndexError('Index out of bounds')
    return l[i]

# Put code want to execute in the try block
try:
    print(return_item(["23"], 0))
# Except will state do not error the code if we get an Index Error, instead print our chosen message
except IndexError:
    print("Index out of bounds")
except TypeError:
    print("We got a type error")
# Else will only run if the code runs fine with no error
else:
    print("The code ran fine")
# Finally will print no matter what, whether there was or was not an index error
finally:
    print("I'm always going to print")