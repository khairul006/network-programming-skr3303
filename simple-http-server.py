import socket
import sys

SERVER_HOST = ''
# SERVER_HOST = '192.168.91.140'
#SERVER_HOST = 'zamidi.kedah.my'
SERVER_PORT = 54322

serv_sock = socket.create_server((SERVER_HOST, SERVER_PORT),
                                 family=socket.AF_INET,
                                 backlog=5, reuse_port=True)
print('Simple HTTP server: ', serv_sock.getsockname())

try:
    while True:
        print('\nServer waiting for a connection request ...')
        cli_sock, cli_addr = serv_sock.accept()
        print('HTTP request received from: ', cli_addr)

        # Get the client request
        request = cli_sock.recv(1024).decode()
        if request:
            print(request)

            # Send response to client
            response = 'HTTP/1.0 200 OK\n\nNetwork Programming Course\n\n'
            cli_sock.sendall(response.encode('utf-8'))
            welcome = 'Welcome client: ' + cli_addr[0]
            print(welcome)
            cli_sock.sendall(bytes(welcome,'utf-8'))
        else:
            print('No data from', cli_addr[0])
            continue
        cli_sock.close()
except KeyboardInterrupt:
    serv_sock.close()
    print('You pressed <Ctrl> C to exit')
    sys.exit()
