#!/usr/bin/python
# Example Python script
# importing system
import sys

count_of_arguments = len(sys.argv)

if count_of_arguments > 1:
    print('There is more than one argument')
    print('The zeroth arg is ' + sys.argv[0])
    print('The first arg is ' + sys.argv[1])
    print('The second arg is ' + sys.argv[2])
    print('The third arg is ' + sys.argv[3])
else:
    where = 'World'
    print("Hello", where)

print('Goodbye from ' +
      sys.argv[0])