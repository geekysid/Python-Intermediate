import requests, csv
from bs4 import BeautifulSoup

with open ('intermediate_web_scrapping.csv', 'w') as csv_file:    # opening a csv file to write data
    
    csv_write = csv.writer(csv_file)    # creating csv writer object
    # adding heading to the csv file
    csv_write.writerow(['property_code', 'price', 'address_line1', 'address_line2', 'bed', 'area', 'full_bath', 'half_bath', 'description', 'features', 'source'])

    url = 'http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/'
    headers = {'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'}
    
    i = 0

    while True:
        # fetching data from the url
        resp = requests.get(url, headers=headers)   # fetching data from web using request library
        if resp.status_code == 200:     # executing only if response code is 200
            
            soup = BeautifulSoup(resp.text, 'html.parser')

            # finding al the div tag with a specific class to lopp over it again and again
            divs = soup.find_all('div', class_='propertyRow')

            for div in divs:
                
                # fetching property code
                property_code = div.find('div', {'class':'propertyMLS'})
                if not property_code == None:
                    property_code = property_code.text.replace('\n', '').replace(' ', '')
                
                # fetching property description
                property_desc = div.find('div', {'class':'propertyDescCollapse collapsed'})
                if not property_desc == None:
                    property_desc = property_desc.text.replace('\n', '').strip()

                # fetching price of the property
                price = div.find_all('h4', class_='propPrice')[0].text.replace("\n", "").replace(" ", "")
                
                # fetching 1st address lines
                address_line1 = div.find_all('span', {'class':'propAddressCollapse'})[0].text
                
                # fetching 2nd address line
                address_line2 = div.find_all('span', {'class':'propAddressCollapse'})[1].text
                
                # fetching bed description
                bed = div.find('span', {'class':'infoBed'})
                if not bed == None:
                    bed = bed.text

                # fetching area of the property description
                area = div.find('span', {'class': 'infoSqFt'})
                if not area == None:
                    area = area.text

                # fetching bathroon description
                full_bath = div.find('span', {'class': 'infoValueFullBath'})
                if not full_bath == None:
                    full_bath = full_bath.text

                # fetching bathroon description
                half_bath = div.find('span', {'class': 'infoValueHalfBath'})
                if not half_bath == None:
                    half_bath = half_bath.text
                
                # fetching source of the information
                source = div.find('div', {'class': 'secondaryHeader'})
                if not source == None:
                    source = source.text.strip()
                    if source[0:4] == 'List':
                        source = source[10:]
                    else:
                        source = source[12:]
                
                # fetching amenities of the porperty
                for div_columnGroup in div.find_all('div', class_='columnGroup'):
                    features = ""
                    for span_featureGroup in div_columnGroup.find_all('span', class_='featureGroup'):
                        featureNames = ""
                        for span_featureNames in div_columnGroup.find_all('span', class_='featureName'):
                            featureNames = featureNames + (span_featureNames.text)
                        features = features + span_featureGroup.text.replace(' ', '').replace(':', '') + ': '+ featureNames + '. \n'
                        # print(span_featureGroup.text.replace(' ', '').replace(':', '') + ': '+ featureNames + '.\n')

                # creating list of all the informations collected
                desc_list = [property_code, price, address_line1, address_line2, bed, area, full_bath, half_bath, property_desc, features, source]

                # adding all the information into csv file
                csv_write.writerow(desc_list)
                
            i = i + 1
            # generating url of next page
            url = 'http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s='+str(i*10)+'.html'

        else:
            break
