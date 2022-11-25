import smtplib, ssl
from 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "falce.matthieu@gmail.com"
receiver_email = "matthieu@falce.net"
password = "lthumuxpgbezukem"
message = """\
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
