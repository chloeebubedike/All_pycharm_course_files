import requests
import pprint

api_key = '3533bc0ff509bb8fce611fa0198b7680'

url = 'https://api.openweathermap.org/data/2.5/weather?lat={-51.4696}&lon={-117.1384}&appid={api_key}'
# Send out request
request = requests.get(url)

# Convert data into json
converted_data = request.json()

# Print using pprint module class
pprint.pp(converted_data)

