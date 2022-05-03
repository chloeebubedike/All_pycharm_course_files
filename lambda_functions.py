#List of numbers
lucky_num = [7, 444, 22, 1]

#Mutate lucky number, store in a list and run map
lucky_num_mutated = list(map(lambda x: x + 1, lucky_num))
print(lucky_num_mutated)