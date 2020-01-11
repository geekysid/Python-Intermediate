import ssl, smtplib, csv

username = "username"     # username used to log into smtp server.
password = "pasword"       # password used to log into smtp server

sender_add = "sender@gmail.com" # address to which mail is being sent.

smtp_add = "smtp.gmail.com"     # address of gmail's smtp server
port = 465      # port number of gmail smtp server

context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_add, port, context=context) as smtp:
    smtp.login(username, password)

    # reading email and name of each user from a csv file to fetch a dictionary od 'Name': 'Email' format
    with open('emailList.csv', 'r') as email_list:
        csv_DictReader = csv.DictReader(email_list, delimiter="|")

        # looping through each row of csv using a dictReader object and fetch name and email as key value pair repectively
        for row in csv_DictReader:
            smtp.sendmail(sender_add, row['Email'], 
                "Subject: Mail for {}\n\nHello {}, You have received Simple Personalised mail from <a href="">python script</a>.".format(row['Name']))
