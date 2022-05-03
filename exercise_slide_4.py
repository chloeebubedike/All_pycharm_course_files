#Tuple of fashion brands
fashion_brands_tuple = ('PLT', 'Misguided', 'AYM', 'House of CB', 'Oh Polly')
#Slice the item between the second (inclusive) and fourth (excluded) position
print(fashion_brands_tuple[2:4])
#Print the item 4 items away from the end of the tuple
print(fashion_brands_tuple[-4])
#Turn tuple into a list
fashion_brands_list = list(fashion_brands_tuple)
#Print all items after the first (inclusive) position
print(fashion_brands_list[1:])
#Prints all items before the second (excluded) position
print(fashion_brands_list[:2])

#Using del to remove list elements after the first (inclusive) and third (excluded) position
music = ['Beyonce', 'Britney', 'JLo', 'Kesha']
del music [1:3]
print(music)