#!/usr/bin/env	python3.5

import Function as f
import math

ip_address = input("Insert the IP Address: ")
ip_mask = input("Insert the IP Mask: ")

num_subnet = input("Insert the number of subnets: ")
print("Insert the number of address for each subnet\n")

subnet = []
for i in range(0, int(num_subnet)):
	subnet.append(input("subnet" + str(i) + ": "))

host_id = []
for i in range(0, int(num_subnet)):
	host_id.append(int(32 - math.log(int(subnet[i]), 2)))
print(host_id)

'''
ip_block = []
for i in range(0, int(num_subnet)):
	ip_block.append(ip_address + "/" + str(host_id[i]))
print(ip_block)
'''

#network 0
ip_block = ip_address + "/" + str(host_id[0])
print("Network 0: ")
print("- Network address: " + str(f.get_network(ip_block)) + "/" + str(host_id[0]))
print("- Broadcast:       " + str(f.get_broadcast(ip_block)))
print("- Subnet mask:     " + str(f.get_mask(ip_block)))
first_host, last_host = f.get_range(ip_block)
print("- Range host:      " + str(first_host) + " -> " + str(last_host))
print()

ip_address = f.get_broadcast(ip_block) + 1

for i in range(1, int(num_subnet)):
	ip_block = str(ip_address) + "/" + str(host_id[i])
	print("Network " + str(i) + ": ")
	print("- Network address: " + str(f.get_network(ip_block)) + "/" + str(host_id[i]))
	print("- Broadcast:       " + str(f.get_broadcast(ip_block)))
	print("- Subnet mask:     " + str(f.get_mask(ip_block)))
	first_host, last_host = f.get_range(ip_block)
	print("- Range host:      " + str(first_host) + " -> " + str(last_host))
	print()
	ip_address = f.get_broadcast(ip_block) + 1
