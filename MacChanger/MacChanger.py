import subprocess
import optparse
import re


def GetUserInput():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i", "--interface", dest="interface", help="interface to change!")
    parse_object.add_option("-m", "--mac", dest="mac_address", help="new mac address")
    return parse_object.parse_args()


def ChangeMacAddress(user_interface, user_mac_address):
    subprocess.call(["ifconfig", user_interface, "down"])
    subprocess.call(["ifconfig", user_interface, "hw", "ether", user_mac_address])
    subprocess.call(["ifconfig", user_interface, "up"])


def GetNewMac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface]).decode('utf-8')
    mac_address_search_result = re.search(r"(\w\w:\w\w:\w\w:\w\w:\w\w:\w\w)", ifconfig_result)

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        return None


print("MacChanger is started!")

(user_input, arguments) = GetUserInput()
ChangeMacAddress(user_input.interface, user_input.mac_address)
finalized_mac = GetNewMac(user_input.interface)

if finalized_mac == user_input.mac_address:
    print("Success! MAC address changed to", finalized_mac)
else:
    print("Error! Failed to change MAC address.")