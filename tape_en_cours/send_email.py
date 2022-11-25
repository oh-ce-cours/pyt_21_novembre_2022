import smtplib, ssl
from os.path import basename
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


port = 587  # For starttls
smtp_server = "smtp.gmail.com"


sender = "matthieu@falce"
receiver = "info@example.com"

msg = MIMEMultipart()
msg["Subject"] = "Test mail with attachment"
msg["From"] = "admin@example.com"
msg["To"] = "info@example.com"

filename = "J1.ipynb"
with open(filename, "r") as f:
    part = MIMEApplication(f.read(), Name=basename(filename))

part["Content-Disposition"] = 'attachment; filename="{}"'.format(basename(filename))
msg.attach(part)

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
