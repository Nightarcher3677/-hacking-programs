import os, sys
import getpass
import sys
import time
from wifi import Cell, Scheme
from scapy.all import *

if platform.system() == 'windows' or platform.system() == 'Windows':
    clear = 'cls'
else:
    clear = 'clear'

username = input('\033[1;32;40m Username: \n')
password = print(' Password: \n')

#defiining functions

def _find_getch():
    try:
        import termios
    except ImportError:
        # Non-POSIX. Return msvcrt's (Windows') getch.
        import msvcrt
        return msvcrt.getch

    # POSIX system. Create and return a getch that manipulates the tty.
    import tty
    def _getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    return _getch


def wait(amount):
    time.sleep(amount)


getch = _find_getch()

pword = ''
ch = 'spam'
# keep looping until "enter" is hit
while ch not in '\r\n':
    ch = getch().decode()
    pword += ch

    print('*', end='')
    # we need to flush, or else the asterisks won't appear
    # until after the password is finished getting entered
    sys.stdout.flush()
# add a newline after the asterisks
print()
print(pword)
# prove that we actually got something
if username == 'mrhacker':
    print('usernamesuccess')
    if 'G@merdude56' in pword:
        print('yes')
        while True:
            os.system(clear)
            print('\033[1;35;40m Hecate\033[1;32;40m')
            os.system('arp -a')
            print()
            wait(1)
