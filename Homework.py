#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

#Get length of string and print hyphens with the same length
print("-" * len(Belgium))

#Remove commas and add in colons between elements.
belgium_colons = ":".join(Belgium.split(","))
print(belgium_colons)

#Split string into list
my_list = belgium_colons.split(":")
#Convert string 1st and 3rd items into integers calculate sum
print(int(my_list[1]) + int(my_list[3]))