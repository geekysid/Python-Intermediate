
<p align="center">
    <img src="https://user-images.githubusercontent.com/59141234/71911924-9dc6d680-319a-11ea-9b06-554ea5cb4eb1.png" height="100px" />
</p>
<h3 align="center">
    Working with Text Files
</h3>
<p align="center" >
    Understanding and Working with Text Files
    <br />
        <a href="https://github.com/siddhantshah1986/Python-Intermediate/tree/master/Working%20with%20Text%20Files">
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
> * [Opening and Reading Text File](#Opening-and-Reading-Text-File)
>   * [read()](#read--Reading-entire-data-from-the-file)
>   * [readline()](#readline---reading-one-line-at-a-time-from-the-file)
>   * [readlines()](#readlines---reading-all-lines-at-once-from-the-file)
> * [Creating and Writing Text File](#Creating-and-Writing-to-Text-File)
>   * [write()](#write---Writing-data-to-Text-File)
> * [Other Useful Functions](#Other-Useful-Functions)
>   * [tell()](#tell---Returns-the-position-of-cursor)
>   * [seek()](#seek---positions-cursor-to-given-location)
> * [Coding Language](#Coding-Language)
> * [Tools](#Tools)
> * [Contributing / Reporting issues](#contributing--reporting-issues) 
> * [Show Your Support](#Show-Your-Support)
> * [About Coder](#about-me)


<!-- Synopsis -->
## Synopsis
<p align="justify">
    When working in python, we need to work with existing text files or need to create new text files. Even though it looks like a tedious task, python makes it very easy by proving a number of built-in functions to assist us in completing the task.
<p>

<!-- Working on JSON File -->
## Opening and Reading Text File
<p align="justify">
In order to read the file, 1st we need to open the file. To open the file we use the function open(). This function takes 2 parameters. 1st parameter takes the path of the file and 2nd parameter (option) indicates the operation that we need to do once the file is opened. We can perform three operations, read (r), write(w) or append (a). When we open the file, it is very important to close the file failing which may cause corrupt data inside the file. To overcome this problem, we use the keyword 'with'. Using this keyword, whenever code goes out of the with block, the file is automatically closed. We can use the property ' to test it.
</p>

```python
with open('filePath', 'r') as read_file
```

<!-- read() -->
#### read()- Reading entire data from the file
<p align="justify">
This method returns all the data inside the file at once. We can limit the number of characters that this method returns but passing an integer value as the parameter of this function.
</p>

```python
data = read_file.read()   # returns entire data for the file
data = read_file.read(50)   # returns 1st 50 characters inside the file
data = read_file.read(50)   # returns next 50 characters inside the file
```

[Checkout](https://github.com/siddhantshah1986/Python-Intermediate/tree/master/Working%20with%20Text%20Files/open_read.py "open_read.py") our coding file for opening and reading text file.

<!-- readline() -->
#### readline() - reading one line at a time from the file
<p align="justify">
This method returns one line of the file at a time. Once the line is returned, the cursor is placed at the starting of the second line. If this function is called again, then the second line is returned and the cursor is placed at the starting of the 3rd line and so on. At any point, we can change the position of the cursor using the function seek(0) which we will learn in some time.
</p>

```python
data = read_file.readline()
```

[Checkout](https://github.com/siddhantshah1986/Python-Intermediate/tree/master/Working%20with%20Text%20Files/open_readline.py "open_readline.py") our coding file for opening and reading text file.

<!-- readline() -->
#### readlines() - reading all lines at once from the file
<p align="justify">
This method returns entire data inside the file in the form of a list with each element consisting of each line inside the file. We can loop through this list to fetch each of the lines.
</p>

```python
data = read_file.readlines()
```

[Checkout](https://github.com/siddhantshah1986/Python-Intermediate/tree/master/Working%20with%20Text%20Files/open_readlines.py "open_readlines.py") our coding file for opening and reading text file.

<!-- Working with JSON data -->
## Creating and Writing to Text File
<p align="justify">

</p>

<!-- write() -->
#### write() - Writing data to Text File
<p align="justify">

</p>

[Checkout](https://github.com/siddhantshah1986/Python-Intermediate/tree/master/Working%20with%20Jsons/loads_json.py "loads_json.py") our coding file for the creating and writing to text file.

## Other Useful Functions
<!-- tell() -->
### tell() - Returns the position of cursor
<p align="justify">

</p>

[Checkout](https://github.com/siddhantshah1986/Python-Intermediate/tree/master/Working%20with%20Jsons/dumps_json.py "dumps_json.py") our coding file for the same.

<!-- seek() -->
### seek() - positions cursor to given location
<p align="justify">

</p>

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