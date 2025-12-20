
# Welcome To The Binary Beat In Motion Python Program Example

# Created by Joseph C. Richardson, GitHub.com

from time import sleep as delay
import os;os.system('title Binary Beat')
import atexit

red = '\033[38;2;255;0;0m'
green = '\033[38;2;0;255;0m'
yellow = '\033[38;2;255;255;0m'
white = '\033[38;2;255;255;255m'

anti_flick = '\033[H'+'\033[?25l'
show_cursor = '\033[?25h\033[0m'

z = 0

end_prog = '\n'+' '*2+red+'Press Enter to exit and close the program:'

def restore_terminal():
    print(show_cursor,flush = True)

atexit.register(restore_terminal)

while z <= 255:
    print(anti_flick+white+'\n'+' '*6+'welcome to the binary beat in motion python program example'.title()
          +yellow+'\n\n'+' '*6+'1     1    1    1    1   1   1   1 = eight bits or one byte'
          +'\n\n'+' '*6+'128 + 64 + 32 + 16 + 8 + 4 + 2 + 1 = decimal number: 255''\n\n'+' '*2
          +'binary base: 2, octal base: 8, hexadecimal base: 16, decimal base: 10'.title()
          +'\n\n'+' '*3+yellow,len(f'{z:b}'),green+'binary digits: '.title()
          +yellow+f'{z:08b} '+red+'=\n\n'+' '*3+yellow,len(f'{z:o}'),green+'octal digits: '.title()
          +yellow+f'{z:o} '+red+'=\n\n'+green+' '*3+yellow,len(f'{z:x}'),green+'hexadecimal digits: '.title()
          +yellow+f'{z:X} '+red+'= '+green+'\n\n'+' '*3+yellow,len(f'{z:d}'),green+'decimal digits: '.title()
          +red+'= '+yellow+f'{z:d}')
    delay(1)
    z += 1

input(end_prog)
