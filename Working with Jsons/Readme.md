
<p align="center">
    <img src="https://user-images.githubusercontent.com/59141234/71911924-9dc6d680-319a-11ea-9b06-554ea5cb4eb1.png" height="100px" />
</p>
<h3 align="center">
    Python Codes (JSONs)
</h3>
<p align="center" >
    Working with JSONs
    <br />
        <a href="https://github.com/siddhantshah1986/Python-Useful-Codes/tree/master/Working%20with%20Jsons">
            View Project
        </a>
        &nbsp;&nbsp;·&nbsp;&nbsp;
        <a href="https://github.com/siddhantshah1986/Python-Useful-Codes/issues">
            Report Bug
        </a>
        &nbsp;&nbsp;·&nbsp;&nbsp;
        <a href="https://github.com/siddhantshah1986/Python-Useful-Codes/issues">
            Request Feature
        </a>
</p>

<!-- Table of Content -->
## Table of contents

> * [Synopsis](#synopsis)
> * [Library](#Library)
> * [Working with JSON file](#Working-with-JSON-file)
> * [Working with JSON data](#Working-with-JSON-data) 
> * [load() vs dump() vs loads() vs dumps()](#Summary)
> * [Coding Language](#Coding-Language)
> * [Tools](#Tools)
> * [Contributing / Reporting issues](#contributing--reporting-issues) 
> * [Show Your Support](#Show-Your-Support)
> * [About Coder](#about-me)
> * [Disclaimer](#Disclaimer)


<!-- Synopsis -->
## Synopsis
<p align="justify">
    When working in python, we need to work with JSON data. Whenever we make an API request,most of the time we get data in the form of JSON objects. So understanding how we can worth on JSON in python is very important.
<p>

<!-- Library -->
## Library
* *json*

<!-- Working on JSON File -->
## Working with JSON file
<p align="justify">
Python provides a way to fetch the data from the JSON file as well as to dump the data into a JSON file. When the data is pulled from the JSON file, or pushed into the JSON file, the data types of the data get converted to the required data type depending on data is fetched or dumped. Below is the table of conversion of the datatype.
</p>

JSON | Python
- | -
object | dict
array | list
string | str
number (int) | int
number (real) | float
true | True
false | False
string | str
null | None

<!-- load() -->
### json.load - Reading data from JSON File
<p align="justify">
In order to fetch the data from the JSON file, we need to use the load function from the JSON library which takes the JSON object and returns it in the form of a dictionary.
</p>

[Checkout](https://github.com/siddhantshah1986/Python-Useful-Codes/tree/master/Working%20with%20Jsons/load_json.py "load_json.py") our coding file for the same.

<!-- dump() -->
### json.dump - Fetching data into JSON File
<p align="justify">
Just like we can read data from the .json file, we can even push data into the .json file. For this purpose, we use the dump function of the JSON library. This function takes 2 arguments. 1st argument is the dictionary that we need to push into .json file and 2nd parameter is the file into which data needs to be pushed.
</p>

[Checkout](https://github.com/siddhantshah1986/Python-Useful-Codes/tree/master/Working%20with%20Jsons/dump_json.py "dump_json.py") our coding file for the same.

<!-- Working with JSON data -->
## Working with JSON data
<p align="justify">
Just like working on files, we can even work with JSON data. When we sent an API request, we generally get a response in the form of JSON and similarly when we get a request, we also need to send the data in JSON format. In such cases, we would need to convert the fetched JSON data into data that python understand to convert our data into JSON format respectively. For this purpose, JSON library has a couple of functions.
</p>

<!-- loads() -->
### json.loads - Reading data from JSON File
<p align="justify">
This function should be read as 'load string' because 's' in loads represents JSON string. This function takes in JSON string (or we can say string representation of any JSON object) and returns a Python object (dictionary).
</p>

[Checkout](https://github.com/siddhantshah1986/Python-Useful-Codes/tree/master/Working%20with%20Jsons/loads_json.py "loads_json.py") our coding file for the same.

<!-- dumps() -->
### json.dumps - Fetching data into JSON File
<p align="justify">
Just like in loads function, 's' in dumps also represents JSON string. This function takes a python object (dictionary) and returns JSON string.
</p>

[Checkout](https://github.com/siddhantshah1986/Python-Useful-Codes/tree/master/Working%20with%20Jsons/dumps_json.py "dumps_json.py") our coding file for the same.

<!-- Summary -->
## Summary
load() | dump() | loads() | dumps()
- | - | - | -
Reads data from .json file and returns python dictionary object. | Writes a python dictionary object data into .json file. | Takes JSON string and returns python objects (dictionary). | Takes python objects (dictionary) and return JSON object.

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

Please feel free to check [issue page](https://github.com/siddhantshah1986/Python-Useful-Codes/issues)

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