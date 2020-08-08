from email import message
import os
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

FROM = os.environ.get('EMAIL_USER')
PASS = os.environ.get('EMAIL_PASS')
TO = 'testyoyo222@gmail.com'

server = smtplib.SMTP('smtp.gmail.com', port=587)

server.starttls()

server.login(FROM, PASS)

msg = MIMEMultipart()
msg['From'] = FROM
msg['To'] = TO

msg['Subject'] = "Testing"

with open('msg.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

filename = "D:\smrnj\Pictures\Saved Pictures\w4h8ko7v76x41.png"
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')

p.set_payload(attachment.read())

encoders.encode_base64(p)

p.add_header('Content-Disposition', f'attachment; filename={filename}')

msg.attach(p)

txt = msg.as_string()

server.sendmail(FROM, TO, txt)
