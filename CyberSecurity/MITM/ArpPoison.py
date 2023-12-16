import scapy.all as scapy

arp_response = scapy.ARP()
scapy.ls(scapy.ARP())