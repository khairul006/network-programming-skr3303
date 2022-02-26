import socket

MULTICAST_GROUP = ('226.1.2.3', 54323)

print('UDP Hello Multicast Sender')
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Set the TTL = 1 for local network segment
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 1)
sock.settimeout(0.5)

try:
    # send greetings
    greetings = 'Hi UDP Multicast Receiver!! Bye !'
    sock.sendto(greetings.encode('utf-8'), MULTICAST_GROUP)
    print('Sent to:', MULTICAST_GROUP)
    # receive welcome message from all recipients
    while True:
        try:
            msg, remote_addr = sock.recvfrom(1024)
        except socket.timeout:
            print('Time out, no more response')
            break
        else:
            print('\nReceived:', msg.decode('utf-8'))
            print('From:', remote_addr)
finally:
    print('Closed socket')
    sock.close()
