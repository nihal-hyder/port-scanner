import socket



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.settimeout(1)
try : 
    s.connect(('192.168.54.101', 21))
    print('[+] connection establish...')
except:
    print('[-] connection denied...')


s.close()