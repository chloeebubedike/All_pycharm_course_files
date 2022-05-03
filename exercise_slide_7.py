#Use pop to extract an item from a list
tv_shows_list =['Stranger things', 'The Apprentice', 'Peaky Blinder', 'RuPauls Drag Race']
#Remove item in the first position
saved_tv_show = tv_shows_list.pop(1)
print("Saved 1:", saved_tv_show, ", Result:", tv_shows_list)
#Remove item from the last (default) position. Note 'The Apprentice' has been permanently removed from list
saved_tv_show = tv_shows_list.pop()
print("Saved 2:", saved_tv_show, ", Result:", tv_shows_list)