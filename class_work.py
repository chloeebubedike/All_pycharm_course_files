#Function takes in 3 names and say hello to them
tup = 'Chloe', 'Uzma', 'Jane'
def say_hello(name1, name2, name3):
    print("Hello", name1, ",hello", name2, "and hello ", name3)

say_hello(*tup)