# parse XML from Google Driving API

import requests
import json
def write_json(data) :
    with open("directions.json", 'w') as file :
        json.dump(data, file, indent=2)




url = "http://maps.googleapis.com/maps/api/directions/json?"

params = dict(origin='Central+Park',
            destination='Times+Square',
            sensor='false',
            mode='walking')

page = requests.get(url=url, params=params)
output = page.json()
write_json(output)

for route in output['routes']:
    for leg in route['legs']:
        for step in leg['steps']:
            print(step['html_instructions'])