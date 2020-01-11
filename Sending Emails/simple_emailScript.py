import smtplib, ssl

sender_add = "siddhant.shah.86@gmail.com" # address to which mail is being sent.
recipient_add = "recipient@example.com"   # address from which the mail will be sent.

# This is how msg of the email has to be written. subject followed by 'Subject:', then 2 blank lines and then the actual body message
message = "Subject: Mail from Python Script\n\nHello, You have received mail from <a href="">python script</a>."

username = "username"     # username used to log into smtp server.
password = "pasword"       # password used to log into smtp server

smtp_add = "smtp.gmail.com"     # address of gmail's smtp server
port = 465      # port number of gmail smtp server
context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_add, port, context=context) as smtp:  # Opening secured SMTP connection
    smtp.login(username, password)      # logging into SMTP server
    smtp.sendmail(sender_add, recipient_add, message)    # sending mail
