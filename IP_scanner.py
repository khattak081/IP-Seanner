import socket
from IPy import IP

print(''' 
  _    _           _   _        _     
 | |  | |         | | | |      | |    
 | | _| |__   __ _| |_| |_ __ _| | __ 
 | |/ / '_ \ / _` | __| __/ _` | |/ / 
 |   <| | | | (_| | |_| || (_| |   <  
 |_|\_\_| |_|\__,_|\__|\__\__,_|_|\_\  \n\n\n''')



targets = input("[+] Enter Target/s To Scan (split Muliple targits with ,) : ")

start_port = int(input("[+] Enter the Starting Port -> "))

ending_port= int(input("[+} Enter The  Ending Port -> "))

### Getting user input
def scan(target):
    converted_ip= check_Ip(target)  ## calling  target ip address for chcking (weather it is domain name or simple ip)
    print('\n'+ '[-_0 Scaning target] ' + str(target))



    for port in range(start_port,ending_port+1):
        scan_port(converted_ip,port)

# def get_banner(k):
#     return k.recv(1024)   ##we wil revive 1024 byte banner site details

## checking the IP and Converting Domain name into ip address 

def check_Ip(ip):
    try: 
       IP(ip)   ## Using IPy function to check the Ip is real Or Domain name 
       return ip
    except ValueError:
        return socket.gethostbyname(ip)     ### converting domain name into ip address
                             
## connecting to ip address

def scan_port(ipaddress,port):

    try:
        khattak= socket.socket()
        khattak.settimeout(1)     ### control the time for scaning one port( more the time more result will be their )
        khattak.connect((ipaddress,port))
        try: 
            banner =khattak.recv(1024)
            '''
                If we want to check version or type of banner port is using we will try to get tese banners 
            '''
            # for removing exta tags and banner tag  we use decode and strip
            print(f"[+]  Open Port " +str(port) + ' : ' + str(banner.decode().strip('\n')))  
        except:
            print(f"[+] Port " + str(port) + " Is Open. ")
    



    except:
        # print(f"[-]Port " + str(port)+ " Is close. ")
        pass


if ',' in targets:
    for ip_add in targets.split(','):
        scan(ip_add.strip(' '))
else :
    scan(targets)