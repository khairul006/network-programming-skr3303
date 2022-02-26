import socket
import os
import sys

SERVER_PORT = 54321
# SERVER_HOST = ''
SERVER_HOST = '<broadcast>'
print('UDP Hello Broadcast Receiver ...PID:', os.getpid())
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.bind((SERVER_HOST, SERVER_PORT))
    print('Binding at', sock.getsockname())

    while True:
        msg, remote_addr = sock.recvfrom(1024)  # receive hello
        print('\nReceived:', msg.decode('utf-8'))
        print('From', remote_addr)

        greetings = 'Hi sender, Welcome !!!'.encode('utf-8')
        sock.sendto(greetings, remote_addr)     # send welcome
        print('Sent greetings to: ', remote_addr)

except KeyboardInterrupt:
    print('You pressed Ctrl+C. Exit')
    sys.exit()
