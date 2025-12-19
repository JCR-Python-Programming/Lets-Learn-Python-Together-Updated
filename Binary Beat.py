
from time import sleep as delay
import os;os.system('title Binary Beat')
import atexit

# Created by Joseph C. Richardson, GitHub.com

red = '\033[38;2;255;0;0m'
green = '\033[38;2;0;255;0m'
yellow = '\033[38;2;255;255;0m'
white = '\033[38;2;255;255;255m'
n = 0

def restore_terminal():
    print('\033[?25h\033[0m',flush = True) # Show the cursor and reset colors

atexit.register(restore_terminal)

while True:
    print('\033[H','\033[?25l'+white+'\n'+' '*6+'welcome to the binary beat in motion python program example'.title()
          +yellow+'\n\n'+' '*6+'1     1    1    1    1   1   1   1 = eight bits or one byte'
          +'\n\n'+' '*6+'128 + 64 + 32 + 16 + 8 + 4 + 2 + 1 = decimal number: 255''\n\n'+' '*2
          +'binary base: 2, octal base: 8, hexadecimal base: 16, decimal base: 10'.title()
          +'\n\n'+' '*3+yellow,len(f'{n:b}'),green+'binary digits: '.title()
          +yellow+f'{n:040b} '+red+'=\n\n'+' '*3+yellow,len(f'{n:o}'),green+'octal digits: '.title()
          +yellow+f'{n:o} '+red+'=\n\n'+green+' '*3+yellow,len(f'{n:x}'),green+'hexadecimal digits: '.title()
          +yellow+f'{n:X} '+red+'= '+green+'\n\n'+' '*3+yellow,len(f'{n:d}'),green+'decimal digits: '.title()
          +red+'= '+yellow+f'{n:d}');delay(1);n+=1
