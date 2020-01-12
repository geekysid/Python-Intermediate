
<p align="center">
    <img src="https://user-images.githubusercontent.com/59141234/71911924-9dc6d680-319a-11ea-9b06-554ea5cb4eb1.png" height="100px" />
</p>
<h3 align="center">
    Sending Emails with Python
</h3>
<p align="center" >
    Understanding how to sent simple and HTML based emails to multiple client
    <br />
        <a href="https://github.com/siddhantshah1986/Python-Intermediate/tree/master/Sending%20Email">
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
> * [Simple Mail](#Simple-Mail)
>   * [Simple Mail to Single Recipient](#Simple-Mail-to-Single-Recipient)
>   * [Simple Mail to Multiple Recipient](#Simple-Mail-to-Multiple-Recipient)
>   * [Simple Personalised Mail to Multiple Recipient](#Simple-Personalised-Mail-to-Multiple-Recipient)
> * [Fancy Mail](#Fancy-Mail)
>   * [Fancy Mail to Single Recipient](#Fancy-Mail-to-Single-Recipient)
>   * [Fancy Personalised Mail to Multiple Recipient](#Fancy-Personalised-Mail-to-Multiple-Recipient)
> * [Mail with Attachment](#Mail-with-Attachment)
> * [Coding Language](#Coding-Language)
> * [Tools](#Tools)
> * [Contributing / Reporting issues](#contributing--reporting-issues) 
> * [Show Your Support](#Show-Your-Support)
> * [About Coder](#about-me)


<!-- Synopsis -->

## Synopsis
<p align="justify">
Sending emails across the network is one of the most common tasks that almost every single app performs. they can be regarding new services/products, or regarding promotions, or simply to communicate with clients. so it is of utmost importance that a coder knows how to send mail. Just like other stuff, Python has various libraries for sending emails as well to make life easy for developers.
</p>

<!-- Working on JSON File -->

## Simple Mail
In this section, we will look at how to send simple email with plain text. For sending mails in python, we will need to import 2 types of libraries, <i>smtplib</i> and <i>ssl</i>

```python
import smtplib, ssl
```


#### Simple Mail to Single Recipient
<p align="justify">
Sending a simple plain text mail to a single may be the easiest task in hand. For this, we simply need to get connected with the smtp server of our mailing account and then use a couple of methods from <i>smtplib</i> library to sent the mail.
</p>

```python
    with smtplib.SMTP_SSL(smtp_address, port) as smtp:  # Opening secured SMTP connection
        smtp.login(username, password)      # logging into SMTP server using login function of class smtblib
        smtp.sendmail(sender_email, recipient_email, 'This s a message')    # sending mail using sendmail function of class smtblib
```
<p align="justify">
It is important to note that for simple mail, we need our message to be in a particular format to display the subject in the mail. If we fail to provide text in the required format then the subject of mail will be blank.
</p>

```python
    message = """Subject: 'Place your subject'
    \n
    \n
    'This will have body of your mail'
    """
    
```

[Checkout](https://github.com/siddhantshah1986/Python-Intermediate/blob/master/Sending%20Emails/simple_emailScript.py "simple_emailScript.py") our coding file for the same.


#### Simple Mail to Multiple Recipient
<p align="justify">
This feature is required to sent bulk mail like pormotional mails or important information about the coampny to set of people. We can do this by passing receipient emails in the form of list to the sendmail function of the class <i>smtplib</i>
</p>

```python
    # passing recipients email addreses in the form of list
    smtp.sendmail(sender_email, ['email1', 'emal2', 'email3'], 'This s a message')
```

[Checkout](https://github.com/siddhantshah1986/Python-Intermediate/blob/master/Sending%20Emails/Simple_multipleToAddess_email.py "simple_multipleToAddess_email.py") our coding file for the same.

#### Simple Personalised Mail to Multiple Recipient
<p align="justify">
Here we send a personalized email to different users in a go. In my example, I have simply read a CSV file that has the name and email address of the recipients. I read both the values using a DictReader function of <i>csv</i> library and sent personalized mail to them. To lear more about reading CSV file please look into <a hf="https://github.com/siddhantshah1986/Python-Intermediate/tree/master/Working%20with%20CSV%20Files">this</a>.
</p>

[Checkout](https://github.com/siddhantshah1986/Python-Intermediate/blob/master/Sending%20Emails/SimplePersonalised_miltipleToAddess_email.py "simplePersonalised_miltipleToAddess_email.py") our coding file for the same.


## Fancy Mail
<p align="justify">
Almost every time we will be using fancy mails to communicate with our clients. These mails allow us to the body of the email in HTML format but also break down email properties like 'To', 'From', 'reply-To', 'Subject' and many more. For these type of maile we will need to import 2 types of classes, <i>MIMEMultipart</i> and <i>MIMEText</i> along with <i>smtplib</i> and <i>ssl</i>.
</p>

```python
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
```


#### Fancy Mail to Single Recipient
<p align="justify">
To make a fancy mail, we use an object of MIMEMultipart which basically breaks downs email body  in a chunk of pieces and makes it easy to control them. It conatils details of header of mail in the form of Key-Value pair like: 
</p>

```python
    # Creating a multipart object and setting headers
    msg_obj = MIMEMultipart()

    msg_obj['To'] = "recipient@example.com"   # display as 'To' in email
    msg_obj['From'] = "sender@gmail.com"    # display as 'From' in email
    msg_obj['Cc'] = "cc@example.com"          # display as 'Cc' in email
    msg_obj['Bcc'] = "bcc@example.com"     # display as 'Bcc' in email
    msg_obj['Subject'] = "Fancy Mail Script"   # display as 'Subject' in email
```

<p slign="justify">
In order to add body to the mail, we create an object of another class, <i>MIMEText</i> which takes 2 parameters, the first parameter has the string and the second parameter will be the type in which the first parameter is to be rendered. If the second parameter is 'html' then the first parameter will be rendered as HTML and if its 'plain' then it will be rendered as a simple plain text.
</p>

```python
    # making baody of mail using MIMEText
    body = MIMEText(
        "<h4>Fancy Mail<h4>You have received this famcy mail from python <a href="">script</a>", 'html'
        )
    msg_obj.attach(body)    # attaching body multipart object
```

In order to pass the MIMEMultipart object (msg_obj) to the sendfunction of class <i>smtplib</i>, we need to convert it into string which can be done easily by using anther method of class MIMEMultipart, as_string()

```python
    smtp.sendmail(sender_add, recipient_add, msg_obj.as_string())   # using as_string() function to display MIMEMultipart object as a string
```

[Checkout](https://github.com/siddhantshah1986/Python-Intermediate/blob/master/Sending%20Emails/fancy_emailScript.py "fancy_emailScript.py") our coding file for the same..


#### Fancy Personalised Mail to Multiple Recipient
<p align="justify">
Now that we have learned how to code fancy email and how to code personalized email for multiple recipients, its no brainer how to work on a fancy personalized mail for multiple recipients. The only thing we need to take care of is that we need to create different instance of MIMEMultipart and MIMEText for each user. I have done the same by creating an object of before said libraries when I am reading individual rows from the CSV file.
</p>

[Checkout](https://github.com/siddhantshah1986/Python-Intermediate/blob/master/Sending%20Emails/fancyPersonalised_miltipleToAddess_email.py "fancyPersonalised_miltipleToAddess_email.py") our coding file for the same.


## Mail with Attachment
<p align="justify">
In order to provide an attachement to the email, we need to import two extra libraries, <i>encoder</i> and <i>MIMEBase</i>. 
</p>

```python
    from email import encoders
    from email.mime.base import MIMEBase
```

```python
    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
```

[Checkout](https://github.com/siddhantshah1986/Python-Intermediate/blob/master/Sending%20Emails/attachment_emailScript.py "attachment_emailScript.py") our coding file for the same..



## Coding Language
Coding language in which the solution are provided here is:

- **Python**


## Tools
- **Visual Studio Code**


## Contributing / Reporting issues
Contributions, issues and feature request are welcome

Please feel free to check [issue page](https://github.com/siddhantshah1986/Python-Intermediate/issues)


## Show Your Support
Please give this project a :star: if you liked this project.


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