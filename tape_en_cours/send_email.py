import smtplib, ssl

port = 587  # For starttls
smtp_server = "localhost:1025"
sender_email = "my@gmail.com"
receiver_email = "your@gmail.com"
message = """\
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.sendmail(sender_email, receiver_email, message)
