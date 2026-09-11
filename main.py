import socket

def scan(ip, port_count):
    # Convert port_count to int and add 1 to include the final port number
    for p in range(1, int(port_count) + 1):
        port_scan(ip, p)

def port_scan(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)  
    try:
        s.connect((ip, port))  
        print(f'[+] {port} port open')
    except (socket.timeout, ConnectionRefusedError, OSError):
        print(f'[-] {port} port closed')
    finally:
        s.close()  

ips = input('Enter IP address(es) (separated by commas): ')
port = input('Enter how many ports to scan: ')

if ',' in ips:
    print('[*] Scanning multiple IPs...')
    for ip_address in ips.split(','):
        scan(ip_address.strip(), port) 
else:
    print('[*] Scanning single IP...')
    scan(ips.strip(), port)