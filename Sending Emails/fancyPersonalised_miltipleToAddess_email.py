import smtplib, csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender_add = "sender@gmail.com" # address to which mail is being sent.

smtp_add = "smtp.gmail.com"     # address of gmail's smtp server
port = 465      # port number of gmail smtp server

username = "username"     # username used to log into smtp server.
password = "pasword"       # password used to log into smtp server
context = ssl.create_default_context()

# connecting to smtp server in secured way from begining
with smtplib.SMTP_SSL(smtp_add, port, context=context) as smtp:
    smtp.login(username, password)      # logging into smtp server

    with open('emailList.csv', 'r') as email_csv:   # reading csv file data
        csv_reader = csv.reader(email_csv, delimiter="|")

        next(csv_reader)    # skipping 1st row as it is header

        # looping through rows in csv file using reader object
        for recipient_name, recipient_add in csv_reader:

            message = MIMEMultipart()
            message['From'] = "from@gmail.com"   # display as 'From' in email
            message['Reply-To'] = "siddhant.shah.1986@example.com"     # display as 'reply-to' in email
            message['Subject'] = "Personalise Mail for " + recipient_name    # display as 'Subject' in email
            message['To'] = recipient_add       # display as 'To' in email

            # creating body of mail using name of user in current row
            body = MIMEText(
                "Hello <b>{0}</b>, <p />You are receiveing this fancy personalised mail in a multi recipient mode from <a href="">python script</a>.".format(recipient_name), 'html'
                )
            message.attach(body)    # attaching body to the mesage object

            # sending email to the user in current row,
            smtp.sendmail(sender_add, recipient_add, message.as_string())
