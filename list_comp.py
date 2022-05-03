# print every other item in my list
my_list = [1, 2, 3, 4, 5, 6, 7, 8]


# for every index in my list
for index in range(len(my_list)):
    # if the item index is odd
    if index % 2 != 0:
        print(my_list[index])


print([index for index in range(len(my_list)) if index % 2 != 0])
