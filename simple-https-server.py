#simple-https-server
import socket, sys, ssl

SERVER_HOST = ''
TLS_HTTPSERVER_PORT = 54422     # HTTPS port

#servercontext = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
servercontext = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
servercontext.load_cert_chain(certfile='/home/kai/local-ca/ca.crt',
                              keyfile='/home/kai/local-ca/ca.key')

serv_sock = socket.create_server((SERVER_HOST,TLS_HTTPSERVER_PORT),
                                 family=socket.AF_INET,
                                 backlog=5, reuse_port=True)

print('Simple HTTPS Server: ', serv_sock.getsockname())

try:
    while True:
        print('\nServer waiting for a connection request ...')
        cli_sock, cli_addr = serv_sock.accept()
        sslsock = servercontext.wrap_socket(cli_sock,server_side=True)
        print('HTTP request received from: ', cli_addr)

        request = sslsock.recv(1024).decode()
        if request:
            print(request)

            response = 'HTTP/1.0 200 OK\n\nNetwork Programming Course\n\n'
            sslsock.sendall(response.encode('utf-8'))
            welcome = 'Welcome client: ' + cli_addr[0]
            print(welcome)
            sslsock.sendall(bytes(welcome, 'utf-8'))
        else:
            print('No data from', cli_addr[0])
            continue
        sslsock.close()
except KeyboardInterrupt:
    serv_sock.close()
    print('You pressed <Ctrl> C to exit')
    sys.exit()
