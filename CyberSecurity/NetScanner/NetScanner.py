import optparse
import scapy.all as scapy


def GetUserInput():
    parseObject = optparse.OptionParser()
    parseObject.add_option("-i","--ipadress", dest="ipAdress", help="Enter IP adress")
    (userInput, arguments) = parseObject.parse_args()

    if not userInput.ipAdress:
        print("Enter IP adress")

    return userInput

def ScanMyNetwork(ip):
    arpRequestPacket = scapy.ARP(pdst=ip)
    #scapy.ls(scapy.ARP())
    broadcastPacket = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    #scapy.ls(scapy.Ether())
    combinedPacket = broadcastPacket/arpRequestPacket
    (answeredList, unansweredList) = scapy.srp(combinedPacket,timeout=1)
    answeredList.summary()

userIpAdress = GetUserInput()
ScanMyNetwork(userIpAdress.ipAdress)


#python3 file name -i x.x.x.x can use this method