import socket
import os

# Address Testing - MP12
#SERVER_HOST = '192.168.22.140'
#SERVER_HOST = 'zamidi.kedah.my'
#SERVER_HOST = '192.168.22.255'
#SERVER_HOST = ''

#SERVER_HOST = '<broadcast>'
#SERVER_HOST = str(socket.INADDR_BROADCAST)
#SERVER_HOST = '255.255.255.255'

SERVER_PORT = 54321

print('UDP Hello Server: PID', os.getpid())
# create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
greetings = 'Hi UDP Hello Server !!!'
sock.sendto(greetings.encode('utf-8'), (SERVER_HOST, SERVER_PORT))
print('Sent greetings to server:', SERVER_HOST)

msg, remote_addr = sock.recvfrom(1024)
print('Received:', msg.decode('utf-8'))
print('From:', remote_addr[0])

sock.close()
