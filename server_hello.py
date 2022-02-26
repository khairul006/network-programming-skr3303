import socket
import os

#SERVER_HOST = '192.168.160.140'
#SERVER_HOST = 'zamidi.kedah.my'
#SERVER_HOST = '127.0.0.1'

SERVER_HOST = ''    # Case 1
SERVER_PORT = 54321
BACKLOG = 5

print('Server: PID', os.getpid())

serv_sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
serv_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #to reuse addr
serv_sock.bind((SERVER_HOST, SERVER_PORT))
serv_sock.listen(BACKLOG)
print('Server waiting for a connection request ...')

while True:
    cli_sock, cli_addr = serv_sock.accept()
    try:
        print('\nConnected by', cli_addr)
        msg = cli_sock.recv(1024)   #receive greeting messages
        print('Received:', msg.decode('utf-8'))
        if msg:
            welcome = 'Hi client, Welcome to the Hello Server. Bye!!!'
            welcome = welcome.encode('utf-8')
            cli_sock.send(welcome)
            print('Sent welcome message to client', cli_addr[0])
        else:
            print('No data from', cli_addr[0])
            continue
    finally:
        cli_sock.close()
