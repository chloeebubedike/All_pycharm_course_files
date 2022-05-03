import requests
import pprint

pokemon_request = requests.get('https://pokeapi.co/api/v2/pokemon/charizard')

pokemon_data = pokemon_request.json()

print('Charizard height: {}, weight {}, id {}'.format(pokemon_data['height'], pokemon_data['weight'], pokemon_data['id']))

second_pokemon_request = requests.get('https://pokeapi.co/api/v2/pokemon?limit=6&offset=?')

second_pokemon_data = second_pokemon_request.json()
print('ID: {}'.format(second_pokemon_data['id']))