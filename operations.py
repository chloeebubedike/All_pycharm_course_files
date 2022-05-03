var = input("Please enter a value: ")
make_var_lowercase = var.lower()
print(make_var_lowercase)

num = make_var_lowercase.isnumeric()
print(num)

num = make_var_lowercase.isdecimal()
print(num)