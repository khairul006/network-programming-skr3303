import email.message

# email message
msg = email.message.EmailMessage()

# set header
msg.add_header('From', 'naiisu006@gmail.com')
msg.add_header('To', 'naiisu006@yahoo.com')
msg.add_header('Cc', 'dridawatyahmad@yahoo.com')
msg.add_header('Subject', 'Testing email-message')




# set contents
body = '''
Salam, hi,
Apa khabar, semoga baik sentiasa.
Regards,
Khairul 
'''
msg.set_content(body)

# display message as a string
msg_string = msg.as_string()
print("\n============ Message as String =============")
print(msg_string)

print("\n============  Message Content  =============")
print(msg.get_content())

# display message as bytes string
msg_bytes = msg.as_bytes()
print("\n============ Message as Bytes =============")
print(msg_bytes)

# add attachment
fp = open('smiley.png', mode='rb')
# fp = open('/home/kai/Downloads/smiley.png', mode='rb')
img_content = fp.read()
msg.add_attachment(img_content,maintype="image", subtype="png", filename="smiley.png")

print("\n============ Content Type Details =============")
print('Content Type             :', msg.get_content_type())
