import requests
import pprint

pokemon_id_list = [1, 2, 3, 4, 5, 6]
pokemon_name_list = []

for id in pokemon_id_list:
  # generate request url
  request_url = 'https://pokeapi.co/api/v2/pokemon/{}'.format(str(id))
  request = requests.get(request_url)
  # convert into json
  response = request.json()
  # save names in a list
  pokemon_name_list.append(response['name'])

print(pokemon_name_list)

with open('pokemon.txt', 'w') as pokemon_file:
  for name in pokemon_name_list:
    pokemon_file.write(name +"\n")

