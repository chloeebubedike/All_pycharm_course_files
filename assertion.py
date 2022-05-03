def return_item(my_list, i):
    assert i >- 0 and i < len(my_list)
    return my_list[i]


print(return_item ([1,2,3], 1))


def my_assert(expr):
    if not expr:
        raise IndexError

my_assert(0)