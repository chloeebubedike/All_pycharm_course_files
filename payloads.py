import requests
import pprint
from datetime import datetime

payload = requests.get('http://api.open-notify.org/iss-now.json')
my_data = payload.json()
pprint.pp(my_data)

date = datetime.fromtimestamp(my_data['timestamp'])
position = my_data['iss_position']['latitude']
longitude = my_data['iss_position']['longitude']

with open('log.txt', 'w+') as log_file:
    log_file.write("Date: {}, Position {}, Longitude {}".format(date, position, longitude))
