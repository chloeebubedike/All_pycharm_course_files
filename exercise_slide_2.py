#Swapping references after assigning values to variables
a = 1
b = 2
a, b = b, a
print(a)
print(b)

#Set values from a numeric range
pink, purple, blue = range(3)
print(pink)
print(purple)
print(blue)

#Repeat values
mytuple = 'item 1', 'item 2', 'item 3'
another = mytuple * 4
print(another)

#Trailing comma creates a tuple
string = 'Hello'
print(type(string))

tuple = 'Hello',
print(type(tuple))