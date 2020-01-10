
<p align="center">
    <img src="https://user-images.githubusercontent.com/59141234/71911924-9dc6d680-319a-11ea-9b06-554ea5cb4eb1.png" height="100px" />
</p>
<h3 align="center">
    Working with CSV Files
</h3>
<p align="center" >
    Understanding and Working with CSV Files
    <br />
        <a href="https://github.com/siddhantshah1986/Python-Intermediate/tree/master/Working%20with%20CSV%20Files">
            View Project
        </a>
        &nbsp;&nbsp;·&nbsp;&nbsp;
        <a href="https://github.com/siddhantshah1986/Python-Intermediate/issues">
            Report Bug
        </a>
        &nbsp;&nbsp;·&nbsp;&nbsp;
        <a href="https://github.com/siddhantshah1986/Python-Intermediate/issues">
            Request Feature
        </a>
</p>

<!-- Table of Content -->
## Table of contents

> * [Synopsis](#synopsis)
> * [Reading CSV File](#Reading-CSV-File)
>   * [reader()](#reader---Reading-Rows-in-the-form-of-List)
>   * [DictReader()](#DictReader---Reading-Rows-in-the-form-of-Dictionary)
> * [Writing CSV File](#Writing-to-CSV-File)
>   * [writer()](#writer---Writing-list-data-to-CSV-File)
>   * [DictWriter()](#DictWriter---Writing-dictionary-data-to-CSV-File)
> * [Coding Language](#Coding-Language)
> * [Tools](#Tools)
> * [Contributing / Reporting issues](#contributing--reporting-issues) 
> * [Show Your Support](#Show-Your-Support)
> * [About Coder](#about-me)


<!-- Synopsis -->
## Synopsis
<p align="justify">
Understanding how to work with CSV files are very important for every programmer as most of the data that we deal with for share will be in the CSV format. 
</p>
<p align="justify">
To work with the CSV file, Python provides <i>csv</i> library which makes our task easy to fetch data from or write data in CSV file. These files are open in same was other file so I will not focus on it. What we will try to understand is how to read and write these files.
</p>

<!-- Working on JSON File -->
## Reading CSV File
<p align="justify">
The <i>csv</i> library provides two way in which we can read data from csv files. 
</p>

<!-- read() -->
#### reader() - Reading Rows in the form of List
<p align="justify">
<i>reader()</i> method returns the reader's objects that can iterate over each line(row) in the CSV file. Whenever we use this reader object to iterate over a row in CSV file, we get a list of strings, with each column (separated by a delimiter) of row acting as the individual string element of that list.
</p>

```python
with open("oscar_age_female.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)   # returns the object of class _csv.reader. 
    for row in csv_reader:  
        print(row['Name'])  # fetching only name column form the file
```

[Checkout](https://github.com/siddhantshah1986/Python-Intermediate/blob/master/Working%20with%20CSV%20Files/reader_csv.py "reader_csv.py") our coding file for understaing how reader() works.

<!-- readline() -->
#### DictReader() - Reading Rows in the form of Dictionary
<p align="justify">
<i>DictReader()</i> function returns the DictReader's objects which just like reader methods can iterate over each line(row) in the CSV file, but instead of list, when iterated over a row in CSV file, it maps the information in each row to a dict whose keys are given by the optional fieldnames parameter to give a key-value pair. Here the key is an element from fieldnames and value is the element from the line of CSV file which is being interated.
 </p><p align="justify">
The fieldnames parameter is a sequence. If fieldnames is omitted, the values in the first row of CSV file will be used as the fieldnames. Regardless of how the fieldnames are determined, the dictionary preserves their original ordering. fieldnames parameters are optional here.
</p><p align="justify">
This methods it easy for us to perform actions on a  given column of row as its easy to call <i>row['index']</i> then <i>row[0]</i>
</p>

```python
with open("oscar_combined.csv", "r") as csv_file:
    csv_dictreader = csv.DictReader(csv_file, delimiter="|")

    for row in csv_dictreader:
        print(row)
```

[Checkout](https://github.com/siddhantshah1986/Python-Intermediate/blob/master/Working%20with%20CSV%20Files/DictWriter_csv.py "DictWriter_csv.py") our coding file for understaing how DictReader() works.

<!-- Opening and Writing to Text File -->
## Writing to CSV File
<p align="justify">
The <i>csv</i> library provides two way in which we can write data from csv files. 
</p>

<!-- write() -->
#### writer() - Writing list data to CSV File
<p align="justify">
<i>writer()</i> methods generate the writer object that coverts the data provided by the user into a desired delimited format and then uses another method <b>writerow()</b> to write into the CSV file.
</p>

```python
with open("writer_csv_test.csv", "w") as csv_file:     # opening csv file in write mode.
    csv_writer = csv.writer(csv_file)       # csv_writer = writer object
    csv_writer.writerow([1978, 30, 'Richard Dreyfuss', 'The Goodbye Girl', "Male"])   # writerow allows us to write data into the csv file.

```

[Checkout](https://github.com/siddhantshah1986/Python-Intermediate/blob/master/Working%20with%20CSV%20Files/writer_csv.py "writer_csv.py") our coding file for understaing how writer() works.

<!-- DictWriter() -->
#### DictWriter() - Writing dictionary data to CSV File
<p align="justify">
<i>writer()</i> methods generate the DictWriter object that coverts the data which in the form of a dictionary and is provided by the user into a desired delimited format and then use another method *writerow()* to write into the CSV file. The fieldnames parameter is a sequence of keys that identify the order in which values in the dictionary passed to the <b>writerow()</b> method are written to the CSV file. We can even use fieldnames as the header of the file by using method <b>writeheader()</b>
</p>

```python
with open("writer_csv_test_Dict.csv", "w") as csv_file:
    fieldnames = ['Year', 'Age', 'Name', 'Movie', 'Gender']     # setting up fieldnames
    csv_dictwriter = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter="|")  # creating DictWriter object whcih will convert input data with proper fieldnames and delimiter

    csv_dictwriter.writeheader()    # setting header of csv file to filednames
    csv_dictwriter.writerow({'Year': 1977, 'Age': 60, 'Name': 'Peter Finch', 'Movie': 'Network', 'Gender': "Male"},)    # converting dictionary into proper format and writing into csv file
```

[Checkout](https://github.com/siddhantshah1986/Python-Intermediate/blob/master/Working%20with%20CSV%20Files/writer_csv.py "writer_csv.py") our coding file for understaing how DictWriter() works.

<!-- Details of Coding Language -->
## Coding Language
Coding language in which the solution are provided here is:
- **Python**

<!-- Details of Tools used for coding -->
## Tools
- **Visual Studio Code**

<!-- Asking for Contributions and Issues -->
## Contributing / Reporting issues
Contributions, issues and feature request are welcome

Please feel free to check [issue page](https://github.com/siddhantshah1986/Python-Intermediate/issues)

<!-- Asking for Supports -->
## Show Your Support
Please give this project a :star: if you liked this project.

<!-- Displaying message about me -->
## About Me

<img align="left" src="https://user-images.githubusercontent.com/59141234/71932585-18f1b200-31c6-11ea-9e2a-50bce063de57.png" width="125px">

<p align="justify">
    Electrical and Instrumentation Engineer by eductaion and Software Engineer by profession. I am a self-taught coder who has worked on languages like, HTML, Javascript, PHP, Asp.net, and Python. After working for years in a couple of IT companies (One of which was India's best IT Company - WIPRO), I took a break off for the IT World for 4 years to take care of Family Business. During these 4 years, I built an ERP with Billing Software for my own company from scratch on the asp.net platform. Now that I have sold my family business, looking to re-start my IT career as a Python Developer.
</p>

> **Siddhant Shah** - Software Engineer

>[GitHub](https://gist.github.com/siddhantshah1986 "Siddhant Git Hub")
&emsp;&emsp;
[Website](https://gist.github.com/siddhantshah1986 "Siddhant Website")
&emsp;&emsp;
[Mail Me](mailto:siddhant.shah.1986@gmail.com "siddhant.shah.1986@gmail.com")
&emsp;&emsp;
[My Resume](mailto:siddhant.shah.1986@gmail.com "siddhant.shah.1986@gmail.com")