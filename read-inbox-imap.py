
import imaplib, getpass, email, ssl, os
IMAP_SERVER = 'imap.gmail.com'
IMAP_TLS_PORT = 993

print('Welcome to ReadEmail: PID', os.getpid())
imapcontext = ssl.create_default_context()

# connect to port 993 using TLS
imap = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_TLS_PORT, ssl_context=imapcontext)

# login to the server
username = input('Enter your Gmail username: ')
paswd = getpass.getpass(prompt='Enter your Gmail password:')
status, response = imap.login(username, paswd)
print('LOGIN status: ', status)
# print('Response is : ', response)

# choose the INBOX folder, modifications to the mailbox are not allowed
status, mailcount = imap.select(mailbox='INBOX',readonly=True)
print('SELECT status: ', status)
print('Number of mails: ', mailcount)

# search for all mails without any filter (ALL)
status, mails = imap.search(None, 'ALL')
# status, mails = imap.search(None, 'SUBJECT', '"security"')
print('SEARCH status: ', status)
print('Mail IDs: ',mails[0].decode().split())

# retrieve all emails, converts to email message type
for mid in mails[0].decode().split():
    print('\n== Start of Mail:',mid)
    status, mdata = imap.fetch(mid, '(RFC822)')
    print('FETCH status', status)
    msg = email.message_from_bytes(mdata[0][1])
    # display header information
    print('From     :',msg.get('From'))
    print('To       :',msg.get('To'))
    print('Cc       :',msg.get('Cc'))
    print('Date     :',msg.get('Date'))
    print('Subject  :',msg.get('Subject'))
    # display only the first 10 lines of email content
    print('Body : ')
    for part in msg.walk():
        if part.get_content_type() == 'text/plain':
            body_lines = part.as_string().split('\n')
            print('\n'.join(body_lines[:10]))
    for attachment in msg.walk():
        content_type = attachment.get_content_type()
        if not (content_type.startswith('text') or content_type.startswith('multi')):
            print('\n\t== Attachments ==')
            print('\n\tAttachment Type', attachment.get_content_disposition())
            print('\tContent Type',attachment.get_content_type())
    print('\n== End of Mail:',mid)
print('\nClose selected mailbox and logout')
imap.close()
imap.logout()
