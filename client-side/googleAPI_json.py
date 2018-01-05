# parse JSON from Google Driving API

import requests
import json


#function for writing json content to a file
def write_json(data) :
    with open("directions.json", 'w') as file :
        json.dump(data, file, indent=2)




url = "http://maps.googleapis.com/maps/api/directions/json?"

#write params in a dict
params = dict(origin='Central+Park',
            destination='Times+Square',
            sensor='false',
            mode='walking')

#retrieve the json
page = requests.get(url=url, params=params)
output = page.json()    
write_json(output)  #write json to a file
    

#loops for retrieving instructions
for route in output['routes']:
    for leg in route['legs']:
        for step in leg['steps']:
            print(step['html_instructions'])