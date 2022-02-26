import socket

#SERVER_HOST = '192.168.160.140'     #ipv4
#SERVER_HOST = 'zamidi.kedah.my'    #fqdn
#SERVER_HOST = 'zamidi'             #hostname
#SERVER_HOST = 'midinetprogram'     #alias name
#SERVER_HOST = '127.0.0.1'          #ipv4 loopback address
#SERVER_HOST = 'localhost'
#SERVER_HOST = '::1'                #ipv6 loopback address
SERVER_HOST = 'ip6-localhost'
SERVER_PORT = 54321

# create a TCP socket
sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
sock.connect((SERVER_HOST, SERVER_PORT))
print('Client: ', sock.getsockname())
print('Connected to: ', sock.getpeername())

greetings = 'Hi Server !!!'
sock.send(greetings.encode('utf-8'))

print('Sent greetings to server: ', sock.getpeername())

# receive welcome message
msg = sock.recv(1024)
print('Received: ', msg.decode('utf-8'))
sock.close()
