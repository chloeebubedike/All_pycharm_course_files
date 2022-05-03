# Need same number of elements on either side to unpack a tuple
favourite_meals = 'tomato pasta', 'tacos', 'chicken katsu', 'rice and peas'
meal1, meal2, meal3, meal4 = favourite_meals
print(meal1)
print(meal2)
print(meal3)
print(meal4)
#Unpacking to a wildcard which grabs as many values as it can
meal1, meal2, *meal3 = favourite_meals
print(meal1)
print(meal2)
print(meal3)
#Looping through and upacking two seperate tuples
colours = 'pink', 'blue', 'red', 'cyan', 'magenta'
moods = 'happy', 'sad', 'angry', 'excited'

for a, *b, c in colours, moods:
    print(a, b, c)