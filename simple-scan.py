import socket
import errno
from datetime import datetime

print('Welcome to Port Scanner')
SERVER_HOST = input('Enter IP address/domain name of a host: ')
print('Enter a range of port numbers')
startport = int(input('Enter a start port: '))
endport = int(input('Enter an end port: '))


print('Scanning port(s) at: ', SERVER_HOST)
stime = datetime.now()  # capture current time

for SERVER_PORT in range(startport,endport+1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setblocking(False)
    sock.settimeout(5)
    result = sock.connect_ex((SERVER_HOST, SERVER_PORT))
    if result == 0:
        print(SERVER_PORT, '--> Open')
    else:
        print(SERVER_PORT, '--> Closed :Reason:', errno.errorcode[result])
    sock.close()

print('Port Scanning Completed in: ', datetime.now() - stime)
