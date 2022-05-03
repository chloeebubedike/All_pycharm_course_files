import random

def flip_coin():

    flip= random.randint(0,1)
    if (flip == 0 ):
       return "heads"
    else:
       return  "tails"

choice = input('heads or tails: ')
result = flip_coin()
print('The coin landed on {}'.format(result))

if (choice == result):
    print("You win")
else:
    print("You lose")