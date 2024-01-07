import scapy.all as scapy

arpResponse = scapy.ARP(op=2,pdst="", hwdst="", psrc="")
scapy.send(arpResponse)
#scapy.ls(scapy.ARP())

