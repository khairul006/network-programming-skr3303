import netifaces
import ipaddress

for iface in netifaces.interfaces():
    if iface == 'lo' or iface.startswith('eth0'):
        continue
    addrs = netifaces.ifaddresses(iface)
    if addrs.get(netifaces.AF_INET):
        ip4addr = addrs.get(netifaces.AF_INET)
        address = ip4addr[0]['addr']
        prefix = ip4addr[0]['netmask']   # A
        bcast = ip4addr[0]['broadcast']
        net_addr = address + '/' + str(prefix)  # B
        host4 = ipaddress.ip_interface(address+'/'+prefix)
        net = host4.network
        net4 = ipaddress.ip_network(net)  # C
        print('Network interface: ', iface) # D
        print("\t IP address: ", str(address))
        print('\t Broadcast address: ', bcast)  # E
        print('\t Subnet mask: ', str(prefix))  #
        print('\t Network address: ', net) # F
        print('\t Default gateway: ', netifaces.gateways().get('default')[netifaces.AF_INET][0])    # G
        print('\t MAC address: ', addrs[netifaces.AF_LINK][0]['addr'])  # H
        print('This network can allocate', net4.num_addresses , 'IP addresses')    # I

