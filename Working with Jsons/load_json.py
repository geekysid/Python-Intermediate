# A python coder can consider JSON file basically as a file which has data in the form of dictionary, 
# i.e. key value pairs.

import json     # Import json library to work with json file

with open('customer.json', 'r') as json_file:       # opening json file by using 'with' operator  
    data = json.load(json_file)     # using load function to fetch data of json file in the form of dictionary

print("Type of Returned Data: {0}".format(type(data)))
print()
for item in data:
    print(item, data[item])