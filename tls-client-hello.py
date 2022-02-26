#tls-client-hello
import socket, ssl, pprint

SERVER_HOST = 'zamidi.kedah.my'
TLS_HELLOSERVER_PORT = 54221

# security context
clientcontext = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
#clientcontext = ssl.create_default_context()
# server certificate
#clientcontext.load_verify_locations('/home/kai/local-ca/ca.crt')
clientcontext.load_default_certs()      # already store this cert in trust store

# create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((SERVER_HOST, TLS_HELLOSERVER_PORT))

# secure socket
sslsock = clientcontext.wrap_socket(sock, server_hostname=SERVER_HOST)

print('Client:', sslsock.getsockname())
print('Connected to:', sslsock.getpeername())
print('\nCipher suite used:', sslsock.cipher())
print('\nView Hello Server certificate:')
pprint.pprint(sslsock.getpeercert())

greetings = 'Hi Server !!!'
sslsock.send(greetings.encode('utf-8'))
print('Sent greetings to server:', sslsock.getpeername())

msg = sslsock.recv(1024)
print('Received:', msg.decode('utf-8'))

sslsock.close()
