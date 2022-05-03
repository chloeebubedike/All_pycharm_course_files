# method 1 - lists and sets
# sort it in order
# convert to set to remove duplicates
# compare if sorted version of list is equal to the sorted version of the set
def contains_duplicate(num_list):
    return sorted(num_list) == sorted(list(set(num_list)))


print(contains_duplicate([1, 2, 3]))


# Method 2 - lists and sets
def contains_duplicate(num_list):
    return len(num_list) > len(set(num_list))


# Method 3 - for loop and builtin list methods
def contains_duplicate(num_list):
    for num in num_list:
        if num_list.count(num) > 1:
            return True
    return False


# Method 4 - list comprehension and builtin list methods
def contains_duplicate(num_list):
    non_duplicated_numbers = [num for num in num_list if num_list.count(num) == 1]
    return len(non_duplicated_numbers) < len(num_list)