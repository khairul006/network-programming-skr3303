import dns.resolver

name = input('Enter the domain name to resolve: ')
records = ['A', 'AAAA', 'NS', 'MX']

for x in records:
    try:
        results = dns.resolver.resolve(name, x)
    except dns.exception.DNSException:
        print('No information for', x, 'RECORD')
        continue
    for y in results:
        print(x, "Record: ", y)
