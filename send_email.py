import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

email_address = os.getenv('EMAIL_ADDRESS')
email_password = os.getenv('EMAIL_PASSWORD')
to = os.getenv('EMAIL_ADDRESS')
subject = "TheBluesMood"
message = input()


def send_email(to, subject, message): 
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = email_address
    msg['To'] = to
    msg.set_content(message)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_address, email_password)
        smtp.send_message(msg)

send_email(to, subject, message)