t1 = 'cat', 'dog', 'python', 'camel'
t2 = 'kelp', 'crab', 'lobster', 'fish'
#use break point and debugger to watch process
for a, *b, c in t1, t2:
    print(a, b, c)