"""
Created on Tue Feb 3/07/2023 

@author: Donovan Givens
Network Management 
Professor Clement

This is an application that creates a Python program to implement
functions for finding interfaces, mac addresses, Ipv4, Ipv6, netmask, and 
networks using Netifaces and Ipaddress Imports.

"""
print("""" 
      This Code was created by: 
          Donovan Givens
          Network Mangement
          professor Clement
          Commited on 3/07/2023
      """)


import netifaces
import ipaddress

netiface = netifaces.interfaces()


mkeys = {}




       
#This Function returns all interfaces on this host
def get_interfaces():
    print('The interfaces are : \n')
    return netifaces.interfaces()
'''Windows IP Configuration


Wireless LAN adapter Local Area Connection* 1:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :

Wireless LAN adapter Local Area Connection* 2:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :

Wireless LAN adapter Wi-Fi:

   Connection-specific DNS Suffix  . : belhaven.edu
   Link-local IPv6 Address . . . . . : fe80::578d:93c7:ddcd:ab25%21
   IPv4 Address. . . . . . . . . . . : 192.168.186.165
   Subnet Mask . . . . . . . . . . . : 255.255.240.0
   Default Gateway . . . . . . . . . : 192.168.176.1
'''
#This function gets the systems mac address
def get_mac(interface):
    nkeys = {}
    for i in netiface:
        addrs = netifaces.ifaddresses(i)
        mac = addrs[netifaces.AF_LINK][0]['addr']
        if mac == "":
            pass
        else:    
            mkeys[i] = mac
        
    addrs = netifaces.ifaddresses(interface)
    
    print('the mac adress of' + interface + 'is: ' + mkeys[interface])
'''mac address : '''

'''Mac address : 5C-FB-3A-6F-49-AF '''
    
#This function gets the systems IPv4 & IPv6
def get_ips(interface):
    ip_dict = {}
    try:

        addrs = netifaces.ifaddresses(interface)
        ipv4 = addrs[netifaces.AF_INET]
        ipv4i = ipv4[0]['addr']
        #print(ipv4i)
        ip_dict['v4'] = ipv4i
    except:
        print('does not have ipv4')

    try: 
        addrs = netifaces.ifaddresses(interface)
        ipv6 = addrs[netifaces.AF_INET6]
        ipv6i = ipv6[0]['addr']
        ip_dict['v6'] = ipv6i
    except:
        print('does not have ipv6') 

    print("the ip addresses are: ")
    print(ip_dict)       

'''IPv4 : 192.168.186.165 and IPv6: fe80::578d:93c7:ddcd:ab25%21'''

# This function gets the netmask
def get_netmask(interface):
    netmask = {}
    addrs = netifaces.ifaddresses(interface)
    try:

        addrs = netifaces.ifaddresses(interface)
        print('does not have ipv6') 
        print("the ip addresses are: ")
    
                                                                      

        ipv4 = addrs[netifaces.AF_INET]
        ipv4i = ipv4[0]['netmask']
        netmask['v4'] = ipv4i
    except:
        print()
        
    try: 
        addrs = netifaces.ifaddresses(interface)
        ipv6 = addrs[netifaces.AF_INET6]
        ipv6i = ipv6[0]['netmask']
        netmask['v6'] = ipv6i
    except:
        print() 
    print("the netmasks are; ")
    print(netmask)
'''netmask for ipv4 and ipv6 : 255.255.240.0'''

#This function gets the system networks
def get_network(interface):
    network = {}
    addrs = netifaces.ifaddresses(interface)
    try:

        addrs = netifaces.ifaddresses(interface)
        ipv4 = addrs[netifaces.AF_INET]
        ipv4i = ipv4[0]['netmask']
        #print(ipv4i)
        network['v4'] = ipv4i
    except:
        print()

    try: 
        addrs = netifaces.ifaddresses(interface)
        ipv6 = addrs[netifaces.AF_INET6]
        ipv6i = ipv6[0]['broadcast']
        network['v6'] = ipv6i
    except:
        print() 

    print(network)



print(get_interfaces())

net = input("which one would you like to examine:")

get_mac(net)

get_ips(net)

get_netmask(net)

get_network(net)


