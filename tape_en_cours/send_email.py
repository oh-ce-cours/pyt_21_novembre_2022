import smtplib, ssl
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

port = 587  # For starttls
smtp_server = "smtp.gmail.com"


sender = "falce.matthieu@gmail.com"
receiver = "matthieu@falce.net"
# https://support.google.com/accounts/answer/185833?hl=fr
password = "lthumuxpgbezukem"

msg = MIMEMultipart()
msg["Subject"] = "Test mail with attachment"
msg["From"] = sender
msg["To"] = receiver


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
    server.login(sender, password)
    server.sendmail(sender, receiver, msg.as_string())
