import socket

#SERVER_HOST = 'www.example.com'
SERVER_HOST = input('Enter the ipaddress/domain name of the web server: ')
SERVER_PORT = input('Enter the port number of the web server: ')
#SERVER_HOST = '192.168.22.140'
#SERVER_PORT = 80
#SERVER_PORT = 54322

print('Welcome to Simple HTTP Client')
sock = socket.create_connection((SERVER_HOST, SERVER_PORT))
print('Simple HTTP Client:', sock.getsockname())
print('Connected to: ', sock.getpeername())

print('Requesting to the web content:')
request = 'GET / HTTP/1.1\r\nHost:%s\n\n' % SERVER_HOST
# request = 'HEAD / HTTP/1.1\r\nHost:%s\n\n' % SERVER_HOST
sock.sendall(request.encode('utf-8'))

# receives a response from the web server
response = sock.recv(4096).decode('utf-8')
print(response)

sock.close()
