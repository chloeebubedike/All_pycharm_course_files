import requests
import pprint

request = requests.get('http://api.open-notify.org/astros.json')

# Convert data into json dictionary
response = request.json()

pprint.pp(response)
print("We currently have {} astronauts in space!".format(response['number']))

# print every name of every astronaut on space rn
for people in response['people']:
    print(f"{people['name']} is in {people['craft']} right now")