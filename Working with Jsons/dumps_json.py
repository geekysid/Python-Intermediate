import json

# python dictionary
python_dict = {
                "firstName": "John",
                "lastName": "Smith",
                "isAlive": True,
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
                "spouse": None
            }
# converting python dict into json string

json_str = json.dumps(python_dict, indent=4)

print(type(json_str))
print(json_str)

