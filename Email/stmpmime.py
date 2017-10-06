#imports

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import time


# smtp gmail
to = ""
user = ""
password = ""

smtpserver = smtplib.SMTP('smtp.gmail.com', 587, timeout=30)
print("Here")
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo()
smtpserver.login ( user, password)

print("Here")

msg = MIMEMultipart()

msg['To']=to
msg['From']=user
msg['Subject']='IOT'

msg.attach(MIMEText("Hello"))


#mail
fp=open('dog.png','rb')
msg.attach(MIMEImage(fp.read()))

smtpserver.sendmail ( user, to , msg.as_string())

#smtpserver.close()

print("mailed !!")

