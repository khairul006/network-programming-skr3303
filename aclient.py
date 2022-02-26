import socket
import sys
import time


print('Welcome to TCP Chat Client')
time.sleep(1)
SERVER_HOST = '192.168.160.140'
SERVER_PORT = 54323
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
time.sleep(1)
#get information to connect with the server
#print(SERVER_HOST, '({})')

name = input('Enter Client\'s name: ')
print('Trying to connect to the server: {}, ({})'.format(SERVER_HOST, SERVER_PORT))

sock.connect((SERVER_HOST, SERVER_PORT))
print("Connected...\n")
sock.send(name.encode())
server_name = sock.recv(1024)
server_name = server_name.decode()
print('{} has joined...'.format(server_name))
print('Enter bye to exit.')

try:
    while True:
        message = input(str("Me > "))


        if message == "bye":
            print('client left')
            #message = 'Client left'
            sock.send(message.encode())
            print("Connection closed")
            sock.close()
            break

        sock.send(message.encode())
        message = sock.recv(1024)
        message = message.decode()
        print(server_name, '>', message)

        if message == 'bye':
            print("Bye from server")
            #sock.send(bytes(message, 'utf-8'))
            sock.close()
            print('Connection closed')
            break

        #sock.send(message.encode())
        #message = sock.recv(1024)
        #message = message.decode()
        #print(server_name, '>', message)

except KeyboardInterrupt:
    sock.close()
    print('You pressed <Ctrl> C to exit')
    sys.exit()
