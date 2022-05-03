from Person import Person


class Customer(Person):
    def __init__(self, name, gender, age, shop, food, colour):
        super().__init__(name, gender, food, colour)
        self._age = age
        self._shop = shop
        self._favourite_food = food
        self._colour = colour

    # get customer shop
    @property
    def shop(self):
        return self._shop

    # set customer shop
    # @shop.setter(self, shop): - property declaration not working
    def get_shop(self, shop):
        self._shop = shop


c1 = Customer('Jo', 'Female', '23', 'New Look', 'Pizza', 'grey')

print(c1._shop)
