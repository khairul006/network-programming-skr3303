
import smtplib, getpass, ssl, os

SMTP_SERVER = 'smtp.gmail.com'
SMTP_TLS_PORT = 465
SMTP_STARTTLS_PORT = 587

print('Welcome to SendTextEmail: PID', os.getpid())
smtpcontext = ssl.create_default_context()

# connect to port 587 # STARTTLS, port 587 is less secure
#smtp = smtplib.SMTP(SMTP_SERVER, SMTP_STARTTLS_PORT)
#smtp.starttls(context=smtpcontext)

# or connect to port 465 # IMPLICIT TLS
smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_TLS_PORT, context=smtpcontext)

# login
username = input('Enter your Gmail username: ')
paswd = getpass.getpass(prompt='Enter your Gmail password: ')
smtp.login(username, paswd)

smail = 'naiisu006@gmail.com'   # sender
rmail = 'naiisu006@gmail.com'  # receiver
#rmail = 'dridawatyahmad@yahoo.com'  # receiver

msg = '''\
Subject: Khairul-Testing SendTextMail-Port 465
This message is sent from Python'''

try:
    smtp.sendmail(smail, rmail, msg)
    print('Emails sent')
except smtplib.SMTPException:
    print('Error unable to send email')

smtp.quit()
print('Logout and Connection Closed')
