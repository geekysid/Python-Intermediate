import csv

male_list = [
    {'Year': 1977, 'Age': 60, 'Name': 'Peter Finch', 'Movie': 'Network', 'Gender': "Male"},
    {'Year': 1978, 'Age': 30, 'Name': 'Richard Dreyfuss', 'Movie': 'The Goodbye Girl', 'Gender': "Male"}
]

female_list =[
    [1995, 45, 'Jessica Lange', 'Blue Sky', "Female"],
    [1996, 49, 'Susan Sarandon', 'Dead Man Walking', "Female"],
    [1997, 39, 'Frances McDormand', 'Fargo', "Female"],
    [1998, 34, 'Helen Hunt', 'As Good as It Gets', "Female"],
    [1999, 26, 'Gwyneth Paltrow', 'Shakespeare in Love', "Female"]
]

with open("writer_csv_test_Dict.csv", "w") as csv_file:
    # returns the object of class _csv.DictWriter and is ready to write into csv file with default delimiter as comma

    fieldnames = ['Year', 'Age', 'Name', 'Movie', 'Gender']

    csv_dictwriter = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter="|")

    csv_dictwriter.writeheader()

    for row in male_list:

        # writing into the file. It is importantto note that the row needs to be in dictiorary 
        # format with keys simillar to that in fieldnames else we will get an error 
        csv_dictwriter.writerow(row)
