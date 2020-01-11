import smtplib, csv

recipient_add_list = []

# fetching email address from a csv file and appending it to email list
with open('emailList.csv', 'r') as email_file:
    csv_DictReader = csv.DictReader(email_file, delimiter="|")
    for row in csv_DictReader:
        recipient_add_list.append(row['Email'])

username = "username"     # username used to log into smtp server.
password = "pasword"       # password used to log into smtp server

sender_add = "sender@gmail.com" # address to which mail is being sent.

message = "Subject: Mail sent to Multiple Address\n\nHello,You have received Simple mail in multi recipient mode from <a href="">python script</a>."  # Personalising message for current user in dict

smtp_add = "smtp.gmail.com"     # address of gmail's smtp server
port = 465      # port number of gmail smtp server

context = ssl.create_default_context()

# creating smtp instance with server details mentioned in smtp_add and port.
with smtplib.SMTP_SSL(smtp_add, port, context=context) as smtp:
    smtp.login(username, password)      # login into smtp server
    smtp.sendmail(sender_add, recipient_add_list, message)    # sending mail