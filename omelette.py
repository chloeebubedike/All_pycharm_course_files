# How many omelettes ca I make
# A box contains 6 eggs and 4 eggs are needed for an omelette
# total eggs = number of boxes * number of eggs
# total omelettes = total eggs / 4
number_of_egg_boxes = 10

number_of_eggs_per_box = 6

eggs_per_omelette = 4

total_eggs = number_of_egg_boxes * number_of_eggs_per_box

total_omelettes = total_eggs / eggs_per_omelette

print('You can make {} omelettes with {} boxes of eggs'.format(total_omelettes, number_of_egg_boxes))

