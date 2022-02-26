import socket

SERVER_HOST = 'zamidi.kedah.my'
SERVER_PORT = 54323

# create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((SERVER_HOST, SERVER_PORT))

print('Welcome to TCP Chat Client')
name = input('Enter your name: ')
print('Connected to: ', sock.getpeername()[0])

sname = sock.recv(1024)   # receive server name
sname = sname.decode('utf-8')
print('Connected to user name: ', sname)
sock.send(name.encode('utf-8'))     # send name to server

while True:
    sendmsg = input('Me -> ')

    # if message to send is bye, then close connection
    if sendmsg == 'bye':
        print('Bye from client')
        sock.send(sendmsg.encode('utf-8'))
        sock.close()
        print('Connection closed')
        break

    sock.send(sendmsg.encode('utf-8'))  # send message to server

    # receive message from server and print
    msg = sock.recv(1024).decode('utf-8')
    print(sname, "->", msg)

    # close connection when receive 'bye' from server
    if msg == 'bye':
        print('Received bye from server : ', sock.getpeername()[0])
        sock.close()
        print('Connection closed')
        break
