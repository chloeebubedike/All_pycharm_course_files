a = 7
b = 3
print(a, b)
a, b = b, a
print(a, b)

x, y, z = 10, 20 , 30
print(x, y, z)
#Look up ways to experiment with range. Increment, starting and stopping number
x, y, z = range(3)
print(x, y, z)

#Operator overload
first_three = 'Amba', 'Uzma', 'CJ'
print(type(first_three))
print(first_three * 3)
print(first_three[0:2])
#Used to create copy
print(first_three[:])

#Extennded iterable unpacking.
x, y, z = first_three
print(x)
print(y)
print(z)

#* shows which values you want to scoop together
names = ['Chloe', 'Busra', 'Salima','Maryam', 'Jevante', 'CJ']
#first, *middle, last = names
#print(first)
#print(middle)
#print(last)

#call the sort method
#names.sort()
print(names)

# call the sorted function
names_sorted = sorted(names)
print(names)
print(names_sorted)

# call the sorted function
names_sorted = sorted(names, key=len)
print(names)
print(names_sorted)