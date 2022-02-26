# bcast-server-hello.py
import socket
import os

# Case 1 - Server use wildcard address
#SERVER_HOST = ''                          # 1(a)
#SERVER_HOST = str(socket.INADDR_ANY)      # 1(b)

# Case 2 - Server use broadcast address
#SERVER_HOST = '<broadcast>'                   # 2(a)
# SERVER_HOST = str(socket.INADDR_BROADCAST)    # 2(b)
#SERVER_HOST = '255.255.255.255'               # 2(c)
SERVER_HOST = '192.168.22.255'                # 2(d)

SERVER_PORT = 54321

print('UDP Hello Server: PID', os.getpid())
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sock.bind((SERVER_HOST, SERVER_PORT))
print('Binding at', sock.getsockname())

while True:
    msg, remote_addr = sock.recvfrom(1024)
    print('\nReceived:', msg.decode('utf-8'))
    print('From:', remote_addr)
    if msg:
        welcome = 'Hi client, Welcome to UDP Hello Server. Bye!!!'
        welcome = welcome.encode('utf-8')
        sock.sendto(welcome, remote_addr)
        print('Sending welcome message to client', remote_addr[0])
    else:
        print('No data from', remote_addr[0])
        continue
