# JSON Parsing 2

import json

# decodes the json file
output = json.load(open('cars.json'))

# display output to screen
print (output["CARS"][0]["MODEL"])