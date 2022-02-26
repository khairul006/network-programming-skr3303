import socket
import os
import struct
import sys

MULTICAST_ADDR = '226.1.2.3'
SERVER_HOST = ''
SERVER_PORT = 54323

print("UDP Hello Multicast Receiver...PID:", os.getpid())

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((SERVER_HOST, SERVER_PORT))
    print('Binding at:', sock.getsockname())

    # Attach the multicast group to socket
    group = socket.inet_pton(socket.AF_INET, MULTICAST_ADDR)
    mreq = struct.pack('4sI', group, socket.INADDR_ANY)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    while True:
        msg, remote_addr = sock.recvfrom(1024)  # receive hello
        print('\nReceived: ', msg.decode('utf-8'))
        print('From', remote_addr)

        greetings = 'Hi sender, Welcome!'.encode('utf-8')
        sock.sendto(greetings, remote_addr)     # send welcome
        print('Sent greetings to:', remote_addr)

except KeyboardInterrupt:
    print('You pressed Ctrl+C. Exit')
    sys.exit()
