import csv

with open("oscar_age_female.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)   # returns the object of class _csv.reader. 

    for row in csv_reader:
        print(row)

with open("oscar_age_female.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)   # returns the object of class _csv.reader. 

    # If the CSV file consists of header then the csv.reader will also convert it in the list of string and 
    # it will be 1st element of the iterator list. If we don't want to read the header then we can just use 
    # the next() function to skip the header as the 1st operation after retrieving the iterator.
    next(csv_reader)

    print("="*50)
    # Here we will loop through each list and change the type of element at index 0, 1, and 2 to int 
    for row in csv_reader:
        row[0] = int(row[0].strip())    # making sure there is no extra space befor or after the text in string
        row[1] = int(row[1].strip())    # making sure there is no extra space befor or after the text in string
        row[2] = int(row[2].strip())    # making sure there is no extra space befor or after the text in string
        row[3] = row[3].strip().replace("\"", "")    # removing extra space and " forn the values to make it clean
        row[4] = row[4].strip().replace("\"", "")    # removing extra space and " forn the values to make it clean
        print(row)


# WORKING WITH PIPE (|) Delimited CSV FILE
with open("oscar_age_male.csv", "r") as csv_file:
    # in order wor read csv file with anyother delimiter then comma, we just need to provide a named argument 
    # 'delimiter' with proper delimiter value to make reading work.
    csv_reader = csv.reader(csv_file, delimiter="|")     
    for row in csv_reader:
        print(row)