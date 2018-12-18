from scapy.all import *
import socket
import os
from colorama import init,Fore,init,Style
init()
os.system('cls')
print """
-------------------------------------------------------
   _____                        _____                 |
  / ____|                      / ____|                |
 | (___   ___ __ _ _ __  _   _| (___   ___ __ _ _ __  |
  \___ \ / __/ _` | '_ \| | | |\___ \ / __/ _` | '_ \ |
  ____) | (_| (_| | |_) | |_| |____) | (_| (_| | | | ||
 |_____/ \___\__,_| .__/ \__, |_____/ \___\__,_|_| |_||
                  | |     __/ |                       |
                  |_|    |___/                        |
                                                      |
        @Author: Raphael D                            |
        @Git   : Raph_Sc2                             |
----------------------------------------------------- 

"""
ip = raw_input("Entrer l'IP cible : ")
closed_ports = 0
open_ports = []


def is_up(ip):
    """ Tests if host is up """
    icmp = IP(dst=ip)/ICMP()
    resp = sr1(icmp, timeout=10)
    if resp == None:
        return False
    else:
        return True


                                    
def main():
    conf.verb = 0 # Disable verbose in sr(), sr1() methods
    pmin = int(raw_input("port min : "))
    pmax = int(raw_input("port max : "))
    ports = range(pmin,pmax)
    if is_up(ip):
        start_time = time.time()
        print "Host %s is up, start scanning" % ip 
        for port in ports:
            src_port = RandShort() # Getting a random port as source port
            p = IP(dst=ip)/TCP(sport=src_port, dport=port, flags='S') # Forging SYN packet
            resp = sr1(p, timeout=1) # Sending packet

            if resp.getlayer(TCP).flags == 0x12:
                send_rst = sr(IP(dst=ip)/TCP(sport=src_port, dport=port, flags='AR'), timeout=1)
                print " Le port : " + Fore.GREEN + str(port) + Style.RESET_ALL + " is"+ Fore.GREEN + " open." + Style.RESET_ALL
            elif resp.getlayer(TCP).flags == 0x14:
                print " Le port : " + Fore.RED + str(port) + Style.RESET_ALL + " is " + Fore.RED + "closed." + Style.RESET_ALL
        
        duration = time.time()-start_time
        print "%s Scan Completed in %fs" % (ip, duration)
    else:
        print " The host is not up, please enter a valid Ip address"



main()




