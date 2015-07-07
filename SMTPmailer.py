#! /usr/bin/env python
# Mail from Python script using a third party SMTP server

import smtplib
import time

localtime = time.asctime(time.localtime(time.time()))
username = 'someuser@gmail.com'  
password = 'password' 

receivers = ['receiver@somemail.com','receiver@somemail.net']
sender = 'someuser@gmail.com'
message = """From: No-reply <someuser@gmail.com>
To: all recepients
Subject: SMTP e-mail test

This is a test e-mail message at %s
""" % localtime

server = smtplib.SMTP('smtp.gmail.com:587')  
server.starttls()  
server.login(username,password)  
server.sendmail(sender, receivers, message)  
server.quit()
