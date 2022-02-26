import socket
import sys

SERVER_HOST = '192.168.160.140'
SERVER_PORT = 54323
BACKLOG = 5

print('Welcome to TCP Chat Server')
name = input('Enter your name: ')

serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serv_sock.bind((SERVER_HOST, SERVER_PORT))
serv_sock.listen(BACKLOG)
print('Waiting for a connection request ...')

cli_sock, cli_addr = serv_sock.accept()
cli_sock.send(name.encode('utf-8'))     # send name to client
print('Connected to:', cli_addr[0])
cname = cli_sock.recv(1024)   # receive client name
cname = cname.decode('utf-8')
print(cname, "has joined the chat room")

try:
    while True:
        # get message from client
        msg = cli_sock.recv(1024).decode()

        # print message from the client
        if msg:
            print(cname, "-> ", msg)

            # close connection when receive bye
            if msg == 'bye':
                print('Received bye from client : ', cli_addr[0])
                cli_sock.close()
                print('Connection closed')
                break

            # send message to client
            sendmsg = input('Me-> ')

            if sendmsg == 'bye':
                print('Bye from server')
                cli_sock.send(bytes(sendmsg, 'utf-8'))
                cli_sock.close()
                print('Connection closed')
                break

            cli_sock.sendall(bytes(sendmsg, 'utf-8'))

except KeyboardInterrupt:
    serv_sock.close()
    print('You pressed <Ctrl> C to exit')
    sys.exit()







'''while True:
    msg = cli_sock.recv(1024)
    msg = msg.decode('utf-8')
    if msg == 'bye':
        msg = 'Received bye from client: ' + cli_addr
        cli_sock.close()
        print('Connection closed')
    print(cname, ":", msg)
    msg = input('Me : ')

    if msg == "bye":
        msg = name + " has left the chat room!"
        cli_sock.send(msg.encode('utf-8'))
        print('\n')
        cli_sock.close()
        break
    cli_sock.send(msg.encode('utf-8'))'''




