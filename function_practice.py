#Create a add function
def add(num1, num2):
    answer = num1 + num2
    return answer

result = add(5, 10)
another_result = add(6,7)

chloe = 23
elliott = 19

ages_added = add(chloe, elliott)
print(result, another_result, ages_added)

#Create a subtract function and check you can call
def sub(num1, num2):
    answer = num1 - num2
    return answer

minus_num = sub(5, 4.6)
print(minus_num)

