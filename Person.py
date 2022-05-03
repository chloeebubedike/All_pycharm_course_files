# Create class called person
class Person:
    # Create class data attribute to be shared amongst all instances
    LOCATION = 'England'

    # Constructor to set name, gender and favourite food
    def __init__(self, name, gender, food, colour):
        self._name = name
        self._gender = gender.upper()
        self._favourite_food = food
        self._colour = colour

    # Getter to get the favourite food attribute
    def get_favourite_food(self):
        return self._favourite_food

    # Setter to set the favourite food attribute
    def set_favourite_food(self, food):
        self._favourite_food = food

    # Special method to stringify the object instance/ class
    def __str__(self):
        return 'Name: ' + self._name + \
               ' Gender: '+self._gender + \
                ' Location: ' + self.LOCATION

    # getter property
    @property
    def colour(self):
        return self._colour


    @colour.setter
    def colour(self, colour):
        self._colour = colour


# Create an instance of person
chloe = Person('chloe', 'female', 'Roast dinner', 'blue')

# Use special method string
print(chloe)

# Set favourite food to mac and cheese
chloe.set_favourite_food('Mac and cheese')

# Get the favourite food
print('Favourite food is {}'.format(chloe.get_favourite_food()))

chloe.colour = 'pink'

print('Favourite colour is {}'.format(chloe.colour))