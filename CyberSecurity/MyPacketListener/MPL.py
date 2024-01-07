import scapy.all as scapy
from scapy.layers import http

def ListenPackets(iface):
    scapy.sniff(iface=iface, store=False, prn=AnalyzePackets)

def AnalyzePackets(packet):
    if http.HTTPRequest in packet:
        if packet.haslayer(scapy.Raw):
            try:
                print(str(packet[scapy.Raw].load, 'utf-8'))
            except UnicodeDecodeError:
                print("Cannot decode the packet.")
ListenPackets("eth0")