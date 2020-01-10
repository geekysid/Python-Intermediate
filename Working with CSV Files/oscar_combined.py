import csv

def row_cleaner(row, gender):
    """ Functions that takes a list of item and returns the list after cleaning and converting items as desired
        Args:
            row (list): list of items that needs to be cleans.
            gender (str): to specify gender of the actor
    """

    index = int(row[0].strip())
    year = int(row[1].strip())
    age = int(row[2].strip())
    name = row[3].strip().replace("\"", "")
    movie = row[4].strip().replace("\"", "")

    return [index, year, age, name, movie, gender]

with open ("oscar_age_female.csv", 'r') as csv_readFemale_file:     # opening csv that has list of osar winning Female actors (Comma Separated)
    with open ("oscar_age_male.csv", 'r') as csv_readMale_file:     # opening csv that has list of osar winning Male actors (Pipe Separated)
        with open ("oscar_combined.csv", 'w') as csv_writeCombined_file:    # opening/ctreating aa csv thatwill have combined list of osar winning Male and Female actors (Pipe Separated)

            csv_readFemale = csv.reader(csv_readFemale_file)    # creating reader object for reading data from female csv
            csv_readMale = csv.reader(csv_readMale_file, delimiter="|")    # creating reader object for reading data from male csv
            csv_writeCombine = csv.writer(csv_writeCombined_file, delimiter="|")    # creating writer object to write data in combined csv
            
            header = next(csv_readFemale)   # reading 1st row from the female reader object to fetch the header
            cleaned_header = []   # list that will hold cleaned data fetched above
            
            # looping through each element of header row and cleaning the data and appending each item to cleaned_header list
            for item in header:
                item = item.strip().replace("\"", "")
                cleaned_header.append(item)

            cleaned_header.append("Gender")     # Adding another item in header which wil hold genger of actor
            
            csv_writeCombine.writerow(cleaned_header)   # writing header to the combined csv file

            # looping through each row of the female reader object and cleaning it using row_cleaner function before writing it to the combined csv file
            for row in csv_readFemale:
                csv_writeCombine.writerow(row_cleaner(row, "Female"))

            next(csv_readMale)      # skipping 1st row of male reader object as it has the header information

            # looping through each row of the male reader object and cleaning it using row_cleaner function before writing it to the combined csv file
            for row in csv_readMale:
                csv_writeCombine.writerow(row_cleaner(row, "Male"))
       