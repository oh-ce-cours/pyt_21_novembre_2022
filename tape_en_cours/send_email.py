import smtplib, ssl
import pathlib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


port = 587  # For starttls
smtp_server = "smtp.gmail.com"


sender = "admin@example.com"
receiver = "info@example.com"

msg = MIMEMultipart()
msg["Subject"] = "Test mail with attachment"
msg["From"] = "admin@example.com"
msg["To"] = "info@example.com"

filename = "words.txt"
with open(filename, "r") as f:
    part = MIMEApplication(f.read(), Name=basename(filename))


context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
