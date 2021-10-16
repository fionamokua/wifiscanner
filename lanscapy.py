x#import scapy 
import scapy.all as scapy
#creation of regular expressions to ensure that the input is correctly formatted
import re
#regular expression pattern to recognize the ipv4 address

ip_add_range_pattern=re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")
#get the address range to arp
while True:
    ip_add_range_entered=input("/n Please enter the ip address and the range that you want to (ex 192.168.1.0/24):")
    if ip_add_range_pattern.search(ip_add_range_entered):
        print(f"{ip_add_range_entered} is a valid ip address range")
        break
#try arping the ip address range supplied by the user
#THe arping() methop in scan py creates an arp message  and sends it to th broad cast mac address
# if a valid ip address range is supplied the program will return the list of all results  
arp_result=scapy.arping(ip_add_range_entered )