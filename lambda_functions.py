# normal function
def plus_two(num):
    return num + 2


print("First iteration:", plus_two(100))


# function on one line
def plus_two(num): return num + 2


print("Second iteration:", plus_two(100))

# add in lambda
# remove function name
# no brackets around parameters
# no return statement needed
print("Final step:",(lambda num: num + 2)(100))


# can give the lambda function a name
plus_two = lambda num: num + 2

print(plus_two(10))


my_func = lambda num: num * 5

print(my_func(5))


# a = 3
b = 10

my_func = lambda a, b: a / b

print(my_func(20, 9))

operations = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
    '**': lambda a, b: a ** b,
    '//': lambda a, b: a // b,
    '%': lambda a, b: a % b,
}
a = int(input("Enter a whole number: "))
b = int(input("Enter another whole number: "))
op = input("What operation would you like use? ")
# access the operations dictionary and pass in a chosen operation which passes in the chosen lambda
print("result:", operations[op](a, b))
