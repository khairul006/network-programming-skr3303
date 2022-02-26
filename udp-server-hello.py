import socket
import os

SERVER_HOST = '192.168.91.140'
SERVER_PORT = 54321

print('UDP Hello Server: PID', os.getpid())
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
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
