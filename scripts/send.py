import smtplib as SMTP
import os
from email.mime.text import MIMEText
from email.header import Header

receivers = os.getenv('RECEIVERS')
sender = os.getenv('SENDER')
mail_user = os.getenv('MAIL_USER')

mail_pass = os.getenv('MAIL_PASS')
mail_host = os.getenv('MAIL_HOST')

mail_msg = ''

with open('./build/index.html') as f:
    mail_msg = f.read()

message = MIMEText(mail_msg, 'html', 'utf-8')
message['From'] = Header(sender, 'utf-8')
message['To'] = Header(receivers, 'utf-8')

subject = 'GitHub Action RSS'
message['Subject'] = Header(subject, 'utf-8')


try:
    conn = SMTP.SMTP_SSL(mail_host)
    conn.set_debuglevel(1)
    conn.connect(mail_host)
    conn.login(mail_user, mail_pass)
    conn.sendmail(mail_user, receivers, message.as_string())
    print('send success!!')
except SMTP.SMTPException:
    print('send error!!')

