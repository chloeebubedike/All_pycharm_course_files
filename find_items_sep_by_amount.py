# Find items that are seperated by a certain amount
# For example in find_sep_by_amount([1, 2, 4, 10], 6) == [4, 10]

def find_sep_by_amount(list_of_num, amount):
    result = []
    # while list of numbers is true
    while list_of_num:
        num = list_of_num.pop()
        diff = num - amount
        if diff in list_of_num:
            result.append((diff, num))
    return result


print(find_sep_by_amount([1, 2, 4, 10], 6))


# solution
def two_number_difference(numbers, amount):
    # for every index in the length of our list
    for index_1 in range(len(numbers) - 1):
        # for every index in
        for index_2 in range(index_1 + 1, len(numbers)):
            x = numbers[index_1]
            y = numbers[index_2]
            difference = abs(x - y)
            if difference == amount:
                return [x, y]
    return []

