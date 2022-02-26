import socket
import ssl
import sys
import pprint

SERVER_HOST = 'www.example.com'
SERVER_PORT = 443

# security context
clientcontext = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)

# server certificate
clientcontext.load_verify_locations('/etc/ssl/certs/ca-certificates.crt')

print('Welcome to Simple HTTPS Client')
sock = socket.create_connection((SERVER_HOST, SERVER_PORT))
sslsock = clientcontext.wrap_socket(sock, server_hostname=SERVER_HOST)
print('Simple HTTPS Client:', sslsock.getsockname())
print('Connected to: ', sslsock.getpeername())
print('\nThe cipher suite used at the remote host: ', sslsock.cipher())
print('\nThe certificate used at the remote host: ')
pprint.pprint(sslsock.getpeercert())

print('Requesting to the web content:')
request = 'GET / HTTP/1.1\r\nHost:%s\n\n' % SERVER_HOST
# request = 'HEAD / HTTP/1.1\r\nHost:%s\n\n' % SERVER_HOST
sslsock.sendall(request.encode('utf-8'))

# receives a response from the web server
while True:
    try:
        response = sslsock.recv(4096).decode('utf-8')
        print(response)
    except KeyboardInterrupt:
        print('You pressed Ctrl+C, Exit')
        sslsock.close()
        sock.close()
        sys.exit()
