import os
import smtplib
import imghdr
from email.message import EmailMessage

from_address = "sias.recreation@krea.ac.in"
from_password = "ardmpcijejdgadiy"

contacts = ['', 'sandeepchezhian_a.sias20@krea.ac.in']

msg = EmailMessage()
msg['Subject'] = 'Check out Bronx as a puppy!'
msg['From'] = from_address
msg['To'] = 'sandeepchezhian_a.sias20@krea.ac.in'
msg.set_content("This is a plain text email")


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(from_address, from_password)
    smtp.send_message(msg)
    