import os, time
from scapy.all import *


def printPostCallback(packet):
    if packet[TCP].payload:
        if packet[IP].dport == 80:
            src  = packet[IP].src
            dst  = packet[IP].dst
            pl   = str(bytes(packet[TCP].payload))
            if pl[:4] == 'POST':
                print  "\n" * 2
                print "#" * 35
                print "%s SENT TO %s" % (src, dst)
                print "#" * 35
                print  "\n%s\n" % pl
                print  "-" * 80
                return
            else:
                return

def loading():
    i = 0
    os.system('cls')
    while i <= 5:
        print "[|] Start HTTP POST scanning "
        time.sleep(0.1)
        os.system('cls')
        print "[/] Start HTTP POST scanning ."
        time.sleep(0.1)
        os.system('cls')
        print "[-] Start HTTP POST scanning .."
        time.sleep(0.1)
        os.system('cls')
        print "[\] Start HTTP POST scanning ..."
        time.sleep(0.1)
        if i == 5:
            time.sleep(0.1)
            os.system('cls')
            print "[+] Scanning"
            return
        os.system('cls')
        i += 1

def main():
    loading()
    sniff(filter='tcp', prn=printPostCallback, store=0, count=0)

main()
