def calculator():
    operator = input('My super calculator. Please type in one of the math operators you would like to use:'
                       '+ for addition,'
                       '- for subtraction,'
                       '* for multiplication,'
                       '/ for division.')
    number_1 = int(input('Enter the first number: '))
    number_2 = int(input('Enter the second number: '))

    if operator == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)
    elif operator == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)
    elif operator == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)
    elif operator == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)
    else:
        print('Your input is invalid. Try again.')


print(calculator())