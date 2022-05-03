# User chooses the desired operation

# Two numbers are taken and if statement used to execute a particular section

print("Please select operation -\n "
"1. Add\n "
"2. Subtract\n"
"3. Multiply\n"
"4. Divide\n")

# Take input from the user
select = int(input("Select operations form 1, 2, 3, 4 :"))
number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))


def add(num1, num2):
    return num1 + num2


def minus(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2


def calculate():
    if select == 1:
        final_number = add(number_1, number_2)
        print(final_number)
    elif select == 2:
        final_number = minus(number_1, number_2)
        print(final_number)
    elif select == 3:
        final_number = multiply(number_1, number_2)
        print(final_number)
    elif select == 4:
        final_number = divide(number_1, number_2)
        print(final_number)
    else:
        print("Please enter an operation number from 1 - 4")


calculate()

