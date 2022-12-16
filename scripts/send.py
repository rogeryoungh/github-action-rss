import smtplib as SMTP
import os
from email.mime.text import MIMEText
from email.header import Header

receivers = os.environ['receivers']
mail_user = os.environ['mail_user']

mail_pass = os.environ['mail_pass']
mail_host = os.environ['mail_host']

mail_msg = ''

with open('./build/index.html') as f:
    mail_msg = f.read()

message = MIMEText(mail_msg, 'html', 'utf-8')
message['From'] = Header(mail_user, 'utf-8')
message['To'] = Header(receivers, 'utf-8')

subject = 'GitHub Action RSS'
message['Subject'] = Header(subject, 'utf-8')


try:
    conn = SMTP.SMTP()
    conn.set_debuglevel(1)
    conn.connect(mail_host)
    conn.login(mail_user, mail_pass)
    conn.sendmail(mail_user, receivers, message.as_string())
    print('send success!!')
except SMTP.SMTPException:
    print('send error!!')

