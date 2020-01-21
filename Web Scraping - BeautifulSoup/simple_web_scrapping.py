import requests, csv
from bs4 import BeautifulSoup

url = 'http://www.pyclass.com/example.html'
headers = {'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'}

resp = requests.get(url, headers=headers)   # fetching data from web using request library

if resp.status_code == 200:     # executing only if response code is 200
    with open ('simple_web_scrapping.csv', 'w') as csv_file:    # opening a csv file to write data
        
        csv_write = csv.writer(csv_file)    
        csv_write.writerow(['city', 'description'])     # adding header inside the csv file

        soup = BeautifulSoup(resp.text, 'html.parser')
        divs = soup.find_all('div', class_='cities')    # fetching all divs with class as cities

        for div in divs:    # looping through all the divs
            city = div.find('h2').text  # fetching city name which is inside h2 tag
            desc = div.find('p').text   # fetching description of city which is inside P tag

            csv_write.writerow([city, desc])    # writing data to the csv file.

