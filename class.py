names =['Tom', 'Harry', 'Jane', 'Mary']
suffix = ['st', 'nd', 'rd', 'th']
n = 1
s = f"{str(n+5) + suffix[n]} of {len(names)} is {names[n]}"
print(s)