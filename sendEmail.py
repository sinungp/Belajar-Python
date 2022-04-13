import smtplib
import ssl

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "datauntukkerja@gmail.com"
receiver_email = "programmer.nyasar@gmail.com"
password = input("Type your password and press enter:")
message = """\
Subject: HOLA

tes kodingan python sinung."""

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
