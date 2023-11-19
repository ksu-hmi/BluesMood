from tkinter import*
import os 
from email.message import EmailMessage
import ssl
import smtplib

root = Tk()
note_entry = Text(root, height=5, width=30)
note_entry.pack(pady=10)

def email():
    email_sender = lala
    email_password =fala
    email_receiver = lafala

    subject = 'Hey, I have something to tell you!'
    note = note_entry.get("1.0", "end-1c")
    body = note_entry

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject 
    em.set_content(body)

    ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
