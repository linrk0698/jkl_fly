# -*- coding: utf-8 -*-
"""
Created on Tue May 30 13:52:58 2017

@author: Kevin Lin
"""

# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
textfile = '../data/budgetArchive/201706.csv'

with open(textfile) as fp:
    # Create a text/plain message
    body = fp.read()

user = 'linrk0698@gmail.com'
pwd  = '01955117'
recipient = 'kevin.rk.lin@gmail.com'
subject = 'The contents of %s' % textfile


gmail_user = user
gmail_pwd = pwd
FROM = user
TO = recipient if type(recipient) is list else [recipient]
SUBJECT = subject
TEXT = body

# Prepare actual message
message = """From: %s\nTo: %s\nSubject: %s\n\n%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

server = smtplib.SMTP("smtp.gmail.com", 587)
server.ehlo()
server.starttls()
server.login(gmail_user, gmail_pwd)
server.sendmail(FROM, TO, message)
server.close()
print('successfully sent the mail')

