import socket

SERVER_HOST = '<broadcast>'
SERVER_PORT = 54321

print('UDP Hello Broadcast Sender')
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sock.settimeout(0.5)

try:
    # send greetings
    greetings = 'Hi UDP Broadcast receiver !! Bye !!'
    sock.sendto(greetings.encode('utf-8'), (SERVER_HOST, SERVER_PORT))
    print('Sent to: ', SERVER_HOST)

    # receive welcome message from all recipients
    while True:
        try:
            msg, remote_addr = sock.recvfrom(1024)
        except socket.timeout:
            print('Timed out, no more response')
            break
        else:
            print('\nReceived:', msg.decode('utf-8'))
            print('From: ', remote_addr)
finally:
    print('Closed socket')
    sock.close()
