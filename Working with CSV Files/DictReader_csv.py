import csv

with open("oscar_combined.csv", "r") as csv_file:
    csv_dictreader = csv.DictReader(csv_file, delimiter="|")
    for row in csv_dictreader:
        print(row)
        
        
# MAKING USE OF DICTIONARY IN BEST WAY
with open("oscar_combined.csv", "r") as csv_file:
    csv_dictreader = csv.DictReader(csv_file, delimiter="|")

    for row in csv_dictreader:
        if int(row['Year']) > 2000 and row['Gender'] == 'Female':
            print(f"In year {row['Year']}, {row['Age']} years old actress known by the name of {row['Name']} won oscars for {row['Movie']} film")


