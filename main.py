import socket
import time

RED = '\033[91m'
GREEN = '\033[92m'
RESET = '\033[0m'

ascii_art = f"""{RED}
  ___  ___  ___ _____   ___  ___   _   _  _  _ _____ ___ 
 | _ \/ _ \| _ \_   _| / __|/ __| /_\ | \| || | | __| _ \
 |  _/ (_) |   / | |   \__ \ (__ / _ \| .` || |_| _||   /
 |_|  \___/|_|_\ |_|   |___/\___/_/ \_\_|\_| \___/___|_|_\ 
{RESET}"""

print(ascii_art)
print("Made by : Nihal Hyder")
print("My GitHub account : https://github.com/nihalhyder\n")

def get_service_name(port, protocol):
    try:
        return socket.getservbyport(port, protocol)
    except OSError:
        return 'unknown'

def grab_version_banner(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1.5)
    banner = "No version response"
    
    try:
        s.connect((ip, port))
        
        if port in [80, 8080, 8000, 443]:
            s.sendall(f"HEAD / HTTP/1.1\r\nHost: {ip}\r\n\r\n".encode())
            
        raw_data = s.recv(1024).decode('utf-8', errors='ignore').strip()
        
        if raw_data:
            for line in raw_data.split('\r\n'):
                if line.lower().startswith('server:'):
                    banner = line.split(':', 1)[1].strip()
                    break
                elif line.startswith('SSH-') or line.startswith('220'):
                    banner = line
                    break
            else:
                banner = raw_data.splitlines()[0]
    except Exception:
        pass
    finally:
        s.close()
        
    return banner

def tcp_scan(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    try:
        s.connect((ip, port))
        s.close()
        
        service = get_service_name(port, 'tcp')
        version = grab_version_banner(ip, port)
        
        print(f'{GREEN}[+] {port}/TCP OPEN | Service: {service} | Version: {version}{RESET}')
    except (socket.timeout, ConnectionRefusedError, OSError):
        pass 

def udp_scan(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(1.5)
    try:
        s.sendto(b'Ping', (ip, port))
        data, _ = s.recvfrom(1024)
        
        service = get_service_name(port, 'udp')
        print(f'{GREEN}[+] {port}/UDP OPEN | Service: {service} (Response received){RESET}')
    except socket.timeout:
        pass  
    except ConnectionRefusedError:
        pass  
    finally:
        s.close()

def scan(ip, max_port, scan_type):
    print(f'\n[*] Scanning target: {ip} ({scan_type.upper()} mode)...')
    for p in range(1, max_port + 1):
        if scan_type == 'tcp':
            tcp_scan(ip, p)
        elif scan_type == 'udp':
            udp_scan(ip, p)

start_time = time.perf_counter()

ips_input = input('Enter IP address(es) (split by comma): ')
ports_input = input('Enter max port number to scan (e.g. 100): ')
mode_input = input('Enter scan protocol (tcp/udp): ').strip().lower()

try:
    max_port_num = int(ports_input)
except ValueError:
    print('[-] Error: Port number must be an integer.')
    exit()

ip_list = [ip.strip() for ip in ips_input.split(',')]

print(f'[*] Target count: {len(ip_list)} IP address(es)')
for target_ip in ip_list:
    if target_ip:
        scan(target_ip, max_port_num, mode_input)

end_time = time.perf_counter()

total_time_taken = end_time - start_time

print(f'total time it tooks to scan the port(s) {total_time_taken} seconds')