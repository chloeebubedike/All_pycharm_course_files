tv_shows_list =['AOT','Stranger things', 'The Apprentice', 'Peaky Blinder', 'RuPauls Drag Race']
#Use sort method to sort a list in place based on the length of the string
tv_shows_list.sort(key=len)
print(tv_shows_list)
#Use sorted function to return a sorted list. CHECK WHAT THIS WAS SORTED BY
numbers = ['22', '4444', '77', '66']
newstr = sorted(numbers)
print(newstr)
#Returns new sorted list by ascending integer
newnum = sorted(numbers, key=int)
print(newnum)