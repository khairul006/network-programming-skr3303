import ipaddress as ip
CLASS_C_ADDR = '192.0.2.0'  # class  C private network address

if __name__ == '__main__':
    not_exit = True
    while not_exit:
        # Get input of prefix length and store in prefix
        prefix = input('Enter the prefix length (24-30): ')

        # Convert prefix to integer
        prefix = int(prefix)

        # Check whether the input in prefix is within C class range
        if prefix not in range(24, 31):
            raise Exception('Prefix length must be between 24 and 30')

        # Store the network address
        net_addr = CLASS_C_ADDR + '/' + str(prefix)
        print('Using network address: ', net_addr)

        net4 = ip.ip_network(net_addr)

        # Display the number of available IP addresses within the given network
        print('This prefix will give', net4.num_addresses, 'IP addresses')

        # Display the network addresses, subnet mask and broadcast address of the network
        print('The network configuration will be')
        print('\tNetwork addresses: ', (net4.network_address))
        print('\tSubnet mask: ', (net4.netmask))
        print('\tBroadcast addresses: ', (net4.broadcast_address))

        # Display the first available address and the last available address in net4 network
        first_ip, last_ip = list(net4.hosts())[0], list(net4.hosts())[-1]
        print('\tHost ip address from ', first_ip, ' to ', last_ip)

        # Display the largest subnet in net4
        # Need to raise exception if subnet prefix 31, 32 - no subnet
        if prefix < 30:
            all_subnets = list(net4.subnets())
            print('\tLargest subnet information: ')
            for s in all_subnets:
                print('\t\t', s)

        # Prompt an input of 'y' or 'n' from user and store in k
        ok = input('Enter y to exit, or any key to continue [y/n] ')

        # Convert the input to lower case
        ok = ok.lower()

        # If input is  'y', exit frm the while loop and gracefullyexit
        if ok.strip() == 'y':
            not_exit = False
