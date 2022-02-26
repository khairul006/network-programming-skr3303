import socket
hostname = input('Enter the hostname:')

#convert a hostname to IP address and display
ipinfo = socket.getaddrinfo(hostname, 'http')
for ip in ipinfo:
  if ip[0] == socket.AF_INET:
    print('IPV4 address:', ip[-1][0])

for ip in ipinfo:
  if ip[0] == socket.AF_INET6:
    print('IPv6 address:', ip[-1][0])

