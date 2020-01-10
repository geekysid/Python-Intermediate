import csv

male_list = [
    [1977, 60, 'Peter Finch', 'Network', "Male"],
    [1978, 30, 'Richard Dreyfuss', 'The Goodbye Girl', "Male"]
]
female_list =[
    [1995, 45, 'Jessica Lange', 'Blue Sky', "Female"],
    [1996, 49, 'Susan Sarandon', 'Dead Man Walking', "Female"],
    [1997, 39, 'Frances McDormand', 'Fargo', "Female"],
    [1998, 34, 'Helen Hunt', 'As Good as It Gets', "Female"],
    [1999, 26, 'Gwyneth Paltrow', 'Shakespeare in Love', "Female"]
]

with open("writer_csv_test.csv", "w") as csv_file:
        
    csv_writer = csv.writer(csv_file)   

    for item in male_list:
        csv_writer.writerow(item)   # writerow allows us to write data into the csv file.

# appending to the already created csv file
with open("writer_csv_test.csv", "a+") as csv_file:     # opening file in append mode.
    # returns the object of class _csv.writer and is ready to write into csv file with delimiter as Pipe (|)
    csv_writer = csv.writer(csv_file)

    for item in female_list:
        csv_writer.writerow(item)   # writerow allows us to write data into the csv file.


# WORKING WITH GIVEN DELIMITER
with open("writer_csv_delimiter_test.csv", "w") as csv_file:
    # returns the object of class _csv.writer and is ready to write into csv file with default delimiter as comma
    csv_writer = csv.writer(csv_file, delimiter="|")   

    for item in male_list:
        csv_writer.writerow(item)   # writerow allows us to write data into the csv file.

# appending to the already created csv file but with different delimiter
with open("writer_csv_delimiter_test.csv", "a+") as csv_file:     # opening file in append mode.
    # returns the object of class _csv.writer and is ready to write into csv file with delimiter as tab
    csv_writer = csv.writer(csv_file, delimiter="\t")

    for item in female_list:
        csv_writer.writerow(item)   # writerow allows us to write data into the csv file.

