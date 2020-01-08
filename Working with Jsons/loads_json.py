import json

# json object string
json_str = '''
            {
                "firstName": "John",
                "lastName": "Smith",
                "isAlive": true,
                "age": 27,
                "address": {
                    "streetAddress": "21 2nd Street",
                    "city": "New York",
                    "state": "NY",
                    "postalCode": "10021-3100"
                },
                "phoneNumbers": [
                    {
                        "type": "home",
                        "number": "212 555-1234"
                    },
                    {
                        "type": "office",
                        "number": "646 555-4567"
                    },
                    {
                        "type": "mobile",
                        "number": "123 456-7890"
                    }
                ],
                "children": [],
                "spouse": null
            }
            '''

# json object array
json_array_str = '''[{ "type": "home", "number": "212 555-1234" }, { "type": "office", "number": "646 555-4567"}, "number"]'''

# converting json string into python objects using loads function
python_dict = json.loads(json_str)
python_list = json.loads(json_array_str)

# looping through the python dict
print("On converting string representation of json object to python dictionary:")
print("Type of Returned Data: {0}".format(type(python_dict)))
for data in python_dict:
    print(type(data), data)

print()

# looping through the python list
print("On converting string representation of json array to python list:")
print("Type of Returned Data: {0}".format(type(python_list)))
for data in python_list:
    print(type(data), data)