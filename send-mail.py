
import smtplib, getpass, ssl, os
import email
# from email.message import EmailMessage

SMTP_SERVER = 'smtp.gmail.com'
SMTP_STARTTLS_PORT = 587

print('Welcome to SendEmail: PID', os.getpid())
smtpcontext = ssl.create_default_context()
smtp = smtplib.SMTP(SMTP_SERVER, SMTP_STARTTLS_PORT)
smtp.starttls(context=smtpcontext)

username = input('Enter your Gmail username: ')
paswd = getpass.getpass(prompt='Enter your Gmail password: ')
smtp.login(username, paswd)

# prepare the email message
msg = email.message.EmailMessage()

# set header
msg.add_header('From','sender@gmail.com')
msg.add_header('To','receiver1@.com')
#msg.add_header('Cc','receiver2@yahoo.com')
msg.add_header('Subject','Khairul-Email from send-mail.py')


# set contents
body = '''
Salam, hi
Kindly check the attachments. Wkwkwkwkwk
Regards,
Github
'''
msg.set_content(body)

fp = open("sample.pdf", mode="rb")
pdf_content = fp.read()
msg.add_attachment(pdf_content, maintype="application", subtype="pdf", filename="smaple.pdf")

with open("peach-color.jpg", mode="rb") as fp:
    img_content = fp.read()
    msg.add_attachment(img_content, maintype="image", subtype="jpg", filename="peach-color.jpg")

with open("smiley.png", mode="rb") as fp:
    img_content = fp.read()
    msg.add_attachment(img_content, maintype="image", subtype="png", filename="smiley.png")

with open("example.zip", mode="rb") as fp:
    zip_content = fp.read()
    msg.add_attachment(zip_content, maintype="application", subtype="zip", filename="example.zip")

# send message
print('Ready to send mail....')
try:
    response = smtp.send_message(msg=msg)
    print('Emails sent')
except smtplib.SMTPException:
    print('Error unable to send email')

smtp.quit()
print('Logout and Connection closed')
