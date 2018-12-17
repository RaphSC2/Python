import socket
import os
from colorama import init,Fore,init,Style
init()
os.system('cls')
print """

$$\   $$\ $$\      $$\  $$$$$$\  $$$$$$$\  
$$$\  $$ |$$$\    $$$ |$$  __$$\ $$  __$$\ 
$$$$\ $$ |$$$$\  $$$$ |$$ /  $$ |$$ |  $$ |
$$ $$\$$ |$$\$$\$$ $$ |$$$$$$$$ |$$$$$$$  |
$$ \$$$$ |$$ \$$$  $$ |$$  __$$ |$$  ____/ 
$$ |\$$$ |$$ |\$  /$$ |$$ |  $$ |$$ |      
$$ | \$$ |$$ | \_/ $$ |$$ |  $$ |$$ |      
\__|  \__|\__|     \__|\__|  \__|\__|      
                                            
                                                                                 

"""
                                    
def main():
    hote = raw_input("Entrer l'IP cible : ")
    port = int(raw_input("port min : "))
    cpt = int(raw_input("port max : "))
    while port <= cpt :
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        rest = s.connect_ex((hote, port))
        if rest == 0:          
            print Fore.GREEN + "Connection on " + str(port)
            print (Style.RESET_ALL)
        else:
            print Fore.RED + "Connection close on " + str(port)
            print (Style.RESET_ALL)
        port += 1
        s.close()  

main()
























