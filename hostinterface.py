import socket
import netifaces

hname = socket.gethostname()
fqdn = socket.getfqdn(hname)
ips = socket.gethostbyname_ex(fqdn)

print('Hostname:', hname)
print('FQDN: ', fqdn)
print('IP address:')
for i in ips[2]:
    print('\t', i)

# this is from netinterface.py
print("Default gateway:", netifaces.gateways().get('default')[netifaces.AF_INET][0])

ifaces = netifaces.interfaces()
for ifa in ifaces:
    print("Network Interfaces: ", ifa)
    addrs = netifaces.ifaddresses(ifa)

    if ifa == 'lo':
        del addrs[netifaces.AF_LINK]

    for family, addresses in addrs.items():
        for current_addr in addresses:
            if family == netifaces.AF_LINK:
                print("  MAC address: ", current_addr.get('addr'))
            else:
                print("  IP address", current_addr.get('addr'))

            if ifa == 'lo':
                print("\t Peer:", current_addr.get('peer'))
            else:
                print("\t Broadcast address:", current_addr.get('broadcast'))

            print("\t Subnet mask:", current_addr.get('netmask'))
