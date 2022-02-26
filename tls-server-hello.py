#tls-server-hello
import os
import socket, sys, ssl

SERVER_HOST = ''
TLS_HELLOSERVER_PORT = 54221
BACKLOG = 5

servercontext = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)

servercontext.load_cert_chain(certfile='/home/kai/local-ca/ca.crt',
                              keyfile='/home/kai/local-ca/ca.key')

print('Server: PID', os.getpid())
serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serv_sock.bind((SERVER_HOST, TLS_HELLOSERVER_PORT))

serv_sock.listen(BACKLOG)
print('Server waiting for a connection request ...')

while True:
    cli_sock, cli_addr = serv_sock.accept()
    sslsock = servercontext.wrap_socket(cli_sock, server_side=True)
    try:
        print('Connected by', cli_addr)
        msg = sslsock.recv(1024)    #receive greetings message
        print('Received:', msg.decode('utf-8'))
        if msg:
            welcome = 'Hi client, Welcome to Hello Server, Bye!!'
            welcome = welcome.encode('utf-8')
            sslsock.send(welcome)
            print('Sent welcome message to client', cli_addr[0])
        else:
            print('No data from', cli_addr[0])
            continue
    finally:
        sslsock.close()
