import os, sys
import socket
port = 7000

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
serversocket.bind((host, port))
serversocket.listen(1)

if platform.system() == 'windows' or platform.system() == 'Windows':
    clear = 'cls'
else:
    clear = 'clear'

os.system(clear)
clientsocket, addr = serversocket.accept()
print("Connection from: " + str(addr))
while True:
    msg = input()
    if msg == "help":
        os.system(clear))
        print("-+-+-+-+-+HELP+-+-+-+-+-")
        print("Test Connection: 'test'")
        input("\nPress ENTER to continue")
        os.system(clear)
    else:
        msg = msg.encode("UTF-8")
        clientsocket.send(msg)
        #msg = clientsocket.recv(4096)
        #print(msg.decode("UTF-8"))
