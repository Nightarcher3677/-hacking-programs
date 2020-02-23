import time
import sys
import os
import subprocess
from tqdm import tqdm
import psutil
import platform
import pygame
if platform.system() == 'windows' or platform.system() == 'Windows':
    clear = 'cls'
else:
    clear = 'clear'
os.system(clear)
pygame.init()
os.system(clear)

#variables
database = 'eh'

#definitions


def wait(Time):
    time.sleep(Time)

def info():
    global database
    print('\033[1;32;40m Hecate')
    print()
    print('CPU usage: ', flush = True)
    sys.stdout.flush()
    print(psutil.cpu_percent(), flush = True)
    print('')
    print('Memory usage: ')
    print(psutil.virtual_memory())
    print('')
    print('Disk IO: ')
    print(psutil.disk_io_counters())
    print('')
    print('OS: ')
    print(platform.system())
    print('\033[1;35;40m')
    #print('Press H to enter a console command')


print("\033[1;35;40m Welcome to HECATE")
wait(2)
print('LOADING...')
from tqdm import tqdm
for i in tqdm(range(100)):
    wait(0.01)
    pass
wait(0.5)
os.system('mode 140, 40')
wait(0.5)
while True:
    print('          _____')
    print('         /\\    \\')
    print('        /::\\____\\')
    print('       /:::/    /')
    print('      /:::/    /')
    print('     /:::/    /')
    print('    /:::/____/')
    print('   /::::\\    \\')
    print('  /::::::\\    \\   _____')
    print(' /:::/\\:::\\    \\ /\\    \\')
    print('/:::/  \\:::\\    /::\\____\\')
    print('\\::/    \\:::\\  /:::/    /')
    print(' \\/____/ \\:::\\/:::/    /')
    print('          \\::::::/    /')
    print('           \\::::/    /')
    print('           /:::/    /')
    print('          /:::/    /')
    print('         /:::/    /')
    print('        /:::/    /')
    print('        \\::/    /')
    print('         \\/____/')
    print('                  ')
    print('')
    print('')
    info()
    wait(1)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_h]:
        database = False
        c = input('enter your command \n\n')
        os.system(c)
        input('Press ENTER to leave')
        database = True
    if database:
        os.system(clear)
