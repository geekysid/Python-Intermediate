import json

# dictioary that we want to push to a json file
data = {"abandoned industrial site": ["Site that cannot be used for any purpose, being contaminated by pollutants."], "abandoned vehicle": ["A vehicle that has been discarded in the environment, urban or otherwise, often found wrecked, destroyed, damaged or with a major component part stolen or missing."], "abiotic factor": ["Physical, chemical and other non-living environmental factor."], "access road": ["Any street or narrow stretch of paved surface that leads to a specific destination, such as a main highway."], "access to the sea": ["The ability to bring goods to and from a port that is able to harbor sea faring vessels."]}

with open('createJSON.json', 'w') as writeJSON:     # opening file with name createJSON.json in write mode
    file = json.dump(data, writeJSON, indent=4)     # dumping data into json as json object.

# tesing if writing to json file worked.
with open('createJSON.json') as readJSON:   # opening json file created in last step in read mode  
    data = json.load(readJSON)         # fetching data from opened file using load function.

print(data)