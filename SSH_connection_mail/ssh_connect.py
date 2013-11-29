#!/usr/bin/env python

# ------------------------------------------------------------
# This script sends a mail at each new SSH connection
# ------------------------------------------------------------
# Arguments:
#   $1 = user connected
#   $2 = Hostname
#   $3 = Client IP
#
# ------------------------------------------------------------

import datetime
import smtplib
import sys
from email.mime.text import MIMEText

# Params
smtp_server = 'yoursmtp.com'
smtp_port = 25
smtp_account = 'you@server.com'
smtp_password = 'YourSuperPassword'

mail_from = "from@server.com"
mail_to = ["to@server.com"]
mail_subject = '%s is now connected with SSH on %s' % (sys.argv[1], sys.argv[2])
mail_message = 'SSH connection alert\n\n\
The user %s is now connected with SSH on the server %s, since %s.\n\n\
Client IP: %s' % (sys.argv[1], sys.argv[2],datetime.datetime.now(), sys.argv[3])

server = smtplib.SMTP(smtp_server, smtp_port)
server.login(smtp_account, smtp_password)

# Send the mail
msg = MIMEText(mail_message)
msg['From'] = mail_from
msg['To'] = ', '.join(mail_to)
msg['Subject'] = mail_subject

server.sendmail(mail_from, mail_to, msg.as_string())

exit(0)
