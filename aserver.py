import socket
import sys
import time

print('Welcome to TCP Chat Server')
time.sleep(1)

# Get the hostname, IP Address from socket and set Port

SERVER_HOST = '192.168.160.140'
SERVER_PORT = 54323

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((SERVER_HOST, SERVER_PORT))
#print('Binding at', sock.getsockname())
name = input('Enter your name: ')
sock.listen(1)  #  Try to locate using socket

print('Waiting for incoming connections...')
cli_sock, cli_addr = sock.accept()
print("Connected to: ", cli_addr[0])


#get a connection from client side
client_name = cli_sock.recv(1024).decode()
print(client_name + ' has joined.')
print('Press bye to leave the chat room')
cli_sock.send(name.encode())

try:
    while True:
        message = cli_sock.recv(1024).decode()

        if message == 'bye':
            print('Received bye from client')
            #message = 'Received bye from server: '+ SERVER_HOST
            #cli_sock.send(message.encode())
            cli_sock.close()
            print("Connection closed")
            break

        print(client_name, ">", message)
        message = input(str("Me > "))
        cli_sock.send(message.encode())

        if message == 'bye':
            print("Bye from Server")
            #cli_sock.send(message.encode())
            cli_sock.close()
            print('Connection closed')
            break




except KeyboardInterrupt:
    sock.close()
    print('You pressed <Ctrl> C to exit')
    sys.exit()
