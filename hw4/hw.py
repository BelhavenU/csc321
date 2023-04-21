#By Donovan Givens
#DNS Hw4 file

#This is section of the code is used to extract the domain for each sit within the file 'domains.tsv'
#part 1
print("domain from each site extraction:")
import csv

with open("domains.tsv", "r") as file:
     
     domains = [".".join(row.split("\t")[0].split(".")[-2:]) for row in file]
     print(domains)



#This is section of the code is used to conduct a forward DNS lookup for each site within the file 'domains.tsv'
# part 2
print("Forward DNS look up")
import socket

with open('domains.tsv', 'r') as file:
    domains = [line.split('\t')[1].strip() for line in file]

results = {}
for domain in domains:
    try:
        ip = socket.gethostbyname(domain)
        results[domain] = ip
    except socket.gaierror:
        results[domain] = 'Error: Unable to resolve'

for domain, ip in results.items():
    print(f'{domain}: {ip}')



#this section of the code Does a Reverse DNS lookup for all IP addresses associated with these domains
# part 3
import socket

with open('domains.tsv', 'r') as file:
    for line in file:
        domain = line.split('\t')[1].strip()
        try:
            ip_addresses = socket.getaddrinfo(domain, None)
            for ip_address in ip_addresses:
                try:
                    reverse_dns = socket.gethostbyaddr(ip_address[4][0])
                    print(f'{ip_address[4][0]}: {reverse_dns[0]}')
                except socket.herror:
                    print(f"Error: No reverse DNS record found for {ip_address[4][0]}")
        except socket.gaierror:
            print(f'Error: Unable to resolve {domain}')



#this section of the code Creates a graph that associates the original domains from the list with domains garnered from the Reverse DNS lookups
# prob 4
print("graph creation:")
import networkx as nx
import matplotlib.pyplot as plt

Graph1 = nx.DiGraph()


with open('domains.tsv', 'r') as file:
    for line in file:
        domain = line.split('\t')[1].strip()

        try:
            ip_addresses = socket.getaddrinfo(domain, None)

            for ip_address in ip_addresses:
                try:
                    reverse_dns = socket.gethostbyaddr(ip_address[4][0])

                    Graph1.add_edge(domain, reverse_dns[0])
                except socket.herror:
                    pass
        except socket.gaierror:
            pass

pos = nx.kamada_kawai_layout(Graph1)
nx.draw(Graph1, pos, with_labels=True)

plt.show()
#Cannot find my graph



