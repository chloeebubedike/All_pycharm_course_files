import sys

if 5 > 10:
    print_statement = "5 is bigger than 10? Really?"
elif 10 > 5:
    print_statement = "This makes sense, 10 is bigger than 5"
else:
    print_statement = "So you're saying 5 and 10 are equal?"

print(print_statement)

lang = ['Pearl', 'Python', 'PHP', 'Ruby']
if 'Python' not in lang:
    print('Python is not there')
else:
    print('Python is there!')

if 1 == 1:
    print('1 is a truthy value')

number = 99
if 50 < number < 100:
    print("This number is inbetween 0 and 100")
else:
    print("This number is either below 50 or above 100")

# While loops

#1
line = None

while line != 'done':
    line = input('Type "done" to complete:')
    print('<', line, '>')

#2
myl = [23, 67, 32, 9, 77]
while myl:
    print(myl.pop()*2)

print(sys.getdefaultencoding())
print("\u20ac",20)

print("The answer is", 42, "always", sep='SPACE ', end='!', flush= 'true')
print("I think!")
print("hello\tworld")