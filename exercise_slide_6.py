skincare_items = ['moisturiser', 'toner']
#Adding items to the left of a list.
skincare_items[:0] = ['SPF', 'essence']
#Plus operator and extend method have the same effect
skincare_items.extend(['retinol', 'alpha arbutin'])
skincare_items += ['retinol', 'alpha arbutin']
#Use append to add singular item into a list
skincare_items.append('retinal')
#Use insert to add items anywhere within a list
skincare_items.insert(3, 'tretoin')
#Use slice to add items anywhere within a list
skincare_items[3:3] = ['tretoin']
print(skincare_items)
