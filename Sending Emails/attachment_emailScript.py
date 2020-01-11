import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.base import MIMEBase

# creating object of MIMEMultipart which holds different information of the mail.
message = MIMEMultipart()

message['To'] = "recipient@example.com"   # display as 'To' in email
message['From'] = "sender@gmail.com"    # display as 'From' in email
message['Cc'] = "cc@example.com"          # display as 'Cc' in email
message['Bcc'] = "bcc@example.com"     # display as 'Bcc' in email
message['Subject'] = "Fancy Mail Email Script With Attachment"   # display as 'Subject' in email

# making baody of mail using MIMEText
body = MIMEText(
        "<h4>Fancy Mail<h4>You have received this fancy mail with attachement from <a href="">python script</a>", 'html'
        )
message.attach(body)    # attaching body tp the message

# Open PDF file in binary mode
with open('emailList.csv', "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email    
encoders.encode_base64(part)

# Add header as key/value pair to attachment part
part.add_header(
    "Content-Disposition",
    f"attachment; filename= emailList.csv",
)

# Add attachment to message and convert message to string
message.attach(part)

username = "username"     # username used to log into smtp server.
password = "pasword"       # password used to log into smtp server

smtp_add = "smtp.gmail.com"     # address of gmail's smtp server
port = 465      # port number of gmail smtp server

sender_add = "sender@gmail.com" # address to which mail is being sent.
recipient_add = "recipient@example.com"   # address from which the mail will be sent.
context = ssl.create_default_context()

# establishing secure SMTP connection
with smtplib.SMTP_SSL(smtp_add, port, context=context) as smtp:
    smtp.login(username, password)      # logging into the smtp server
    smtp.sendmail(sender_add, recipient_add, message.as_string())   # sending mail
