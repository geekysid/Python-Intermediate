import requests, json, time



def get_currentLocation():
    """
        Function that using ipStack api to fetch current location of user and returns zipcode of the user.
    """

    url = 'http://api.ipstack.com/check'

    params = {'access_key': 'deac9233d193f907ea2a810700f73c7a', 'fields': 'zip'}

    r_obj = requests.get(url, params=params)

    return r_obj.json()['zip']


def fahrenheit_to_celcius(temp_in_F):
    return (temp_in_F - 180)*5/9

def kelvin_to_celcius(temp_in_K):
    return temp_in_K - 273.15


print(" Welcome to WEATHER APP")
print("="*24)
print()

location = input("Please click 1 to know weather at your location: ")

if location == '1':

    city = input("Please enter the City: ")

    url= 'https://api.openweathermap.org/data/2.5/weather'

    params = {'q': city, 'APPID': '52ad267bc518ddfdcedddb881ebc37d9'}

    r_obj = requests.get(url, params=params)

    r_dict = r_obj.json()
    
    # print(json.dumps(r_dict, indent=4))

    print()
    # print(type(r_dict['sys']['sunrise']))
    temprature_actual = kelvin_to_celcius(r_dict['main']['temp'])
    temprature_feels = kelvin_to_celcius(r_dict['main']['feels_like'])
    temprature_max = kelvin_to_celcius(r_dict['main']['temp_max'])
    temprature_min = kelvin_to_celcius(r_dict['main']['temp_min'])
    wind = r_dict['wind']['speed']
    humidity = r_dict['main']['humidity']
    location = r_dict['name'].upper() + ", " + r_dict['sys']['country']
    sunrise = time.ctime(r_dict['sys']['sunrise'])
    sunset = time.ctime(r_dict['sys']['sunset'])

    print("Weather details for location: {}".format(location))
    print(f"Current Temprature is {temprature_actual:.2f} deg C but feels like {temprature_feels:.2f} deg C")
    print(f"Today's Max Temprature: {temprature_max:.2f} deg C")
    print(f"Today's Min Temprature: {temprature_min:.2f} deg C")
    print(f"Wind: {wind}km/h; Humidity: {humidity}%")
    print(f"Sunrise Time: {sunrise}")
    print(f"Sunset Time: {sunset}")
    print()