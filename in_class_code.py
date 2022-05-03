#Define the function
def make_list():
    result = range(6)
    return result

def make_list_2(value, times):
    result = str(value) * times
    return result

def print_list(value, times):
    print(str(value) * times)

#Call or Invoke the function
list_a = make_list()
print(type(list_a))
print(list_a)


list_b = make_list_2('chips ', 4)
print(list_b)
print(make_list_2('Chloe ', 7))

#Call function that does not return our value
print_list('spam', 5)