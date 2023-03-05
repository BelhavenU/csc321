#imports
import netifaces
import ipaddress

interface = netifaces.interfaces()

# pull IP configuration with 'ipconfig'in terminal 
# pull interfaces on personal computer 

def get_interfaces():
    print('Interfaces: \n')
    return netifaces.interfaces()
'''Windows IP Configuration

   Host Name . . . . . . . . . . . . : chonteze
   Primary Dns Suffix  . . . . . . . :
   Node Type . . . . . . . . . . . . : Hybrid
   IP Routing Enabled. . . . . . . . : No
   WINS Proxy Enabled. . . . . . . . : No

Ethernet adapter Ethernet:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . : attlocal.net
   Description . . . . . . . . . . . : Killer E2600 Gigabit Ethernet Controller
   Physical Address. . . . . . . . . : 08-8F-C3-61-48-F5
   DHCP Enabled. . . . . . . . . . . : Yes
   Autoconfiguration Enabled . . . . : Yes

Wireless LAN adapter Local Area Connection* 1:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : Microsoft Wi-Fi Direct Virtual Adapter
   Physical Address. . . . . . . . . : 54-6C-EB-7C-FC-64
   DHCP Enabled. . . . . . . . . . . : Yes
   Autoconfiguration Enabled . . . . : Yes

Wireless LAN adapter Local Area Connection* 2:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : Microsoft Wi-Fi Direct Virtual Adapter #2
   Physical Address. . . . . . . . . : 56-6C-EB-7C-FC-63
   DHCP Enabled. . . . . . . . . . . : No
   Autoconfiguration Enabled . . . . : Yes

Wireless LAN adapter Wi-Fi:

   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : Killer(R) Wi-Fi 6 AX1650i 160MHz Wireless Network Adapter (201NGW)
   Physical Address. . . . . . . . . : 54-6C-EB-7C-FC-63
   DHCP Enabled. . . . . . . . . . . : Yes
   Autoconfiguration Enabled . . . . : Yes
   Link-local IPv6 Address . . . . . : fe80::a4df:1131:d151:7a61%8(Preferred)
   IPv4 Address. . . . . . . . . . . : 10.0.0.27(Preferred)
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Lease Obtained. . . . . . . . . . : Sunday, March 5, 2023 2:36:24 PM
   Lease Expires . . . . . . . . . . : Monday, March 6, 2023 2:36:24 PM
   Default Gateway . . . . . . . . . : 10.0.0.1
   DHCP Server . . . . . . . . . . . : 10.0.0.1
   DHCPv6 IAID . . . . . . . . . . . : 89418987
   DHCPv6 Client DUID. . . . . . . . : 00-01-00-01-2A-44-08-2B-08-8F-C3-61-48-F5
   DNS Servers . . . . . . . . . . . : 10.0.0.1
   NetBIOS over Tcpip. . . . . . . . : Enabled

Ethernet adapter Bluetooth Network Connection:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : Bluetooth Device (Personal Area Network)
   Physical Address. . . . . . . . . : 54-6C-EB-7C-FC-67
   DHCP Enabled. . . . . . . . . . . : Yes
   Autoconfiguration Enabled . . . . : Yes '''
# code for finding mac address for given interface

def get_mac(interface):
    my_interface = netifaces.ifaddresses(interface)
    mac_address = my_interface[netifaces.AF_LINK][0]['addr']
    return mac_address
'''' for dorm network UV 313 : 54-6C-EB-7C-FC-63 and for BU Student '''

# code for finding ip for given interface

def get_ips(interface):
    interface = netifaces.interfaces()
    ip_dict = {}

    try: 
        ipv6 = netifaces.ifaddresses(interface)[netifaces.AF_INET6][0]['addr']
        ip_dict["ipv6"] = ipv6
    except: 
        print('no ipv6')
    try:
        ipv4 = netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['addr']
        ip_dict["ipv4"] = ipv4
    except: 
        print('no ipv4')

    return ip_dict

'''IPv4 : 10.0.0.27 and IPv6 : fe80::a4df:1131:d151:7a61%8 '''
# code for finding netmask for given interface

def get_netmask(interface):
    interface = netifaces.interfaces()
    netmask_dict = {}

    try: 
        ipv6 = netifaces.ifaddresses(interface)[netifaces.AF_INET6][0]['netmask']
        netmask_dict["ipv6"] = ipv6
    except: 
        print('no ipv6 netmask')
    try:
        ipv4 = netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['netmask']
        netmask_dict["ipv4"] = ipv4
    except: 
        print('no ipv4')

    return netmask_dict

'''IPv4:255.255.255.0 and IPv6:255.255.255.0 '''
