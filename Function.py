#!/usr/bin/env	python3
import ipaddress

def	get_mask(ip_block):
	return ipaddress.IPv4Network(ip_block).netmask

def	get_broadcast(ip_block):
	return ipaddress.IPv4Network(ip_block).broadcast_address

def get_network(ip_block):
	return ipaddress.IPv4Network(ip_block).network_address
	
def	get_range(ip_block):
	network = get_network(ip_block)
	broadcast = get_broadcast(ip_block)
	return network + 1, broadcast - 1

