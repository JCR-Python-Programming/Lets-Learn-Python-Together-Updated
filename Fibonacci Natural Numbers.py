# Fibonacci Natural Number Sequence Python program example.

# Created by Joseph C. Richardson, GitHub.com

# Note: you must execute/run the program from
# the OS output screen, via double-clicking the Python
# program file itself.

# HIGHLIGHT AND COPY CODE, THEN PASTE INTO YOUR PREFERABLE PYTHON APP/IDLE

import os;os.system(f'title Fibonacci Natural Number Sequence')
import time
import atexit

def restore_terminal():
  print(show_cursor,flush = True)

atexit.register(restore_terminal)

text_colours=(
  '\033[38;2;255;0;255m', # index 0 = red
  '\033[38;2;0;255;0m', # index 1 = green
  '\033[38;2;255;255;0m', # index 2 = yellow
  '\033[38;2;0;255;255m', # index 3 = cyan
    )

anti_flick = '\033[H'+'\033[?25l'

# show_cursor = '\033[?25h\033[0m'

text_words=(
  f'{text_colours[1]}Fibonacci Natural Number Sequence in Action...',

  f'\n\n{text_colours[2]}Fibonacci Natural Number Sequence example: \
[0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610...]',

  f'\n\n{text_colours[3]}Fibonacci Natural Numbers go on forever!',
  f'\n\nFibonacci Natural Numbers can only be found in \
nature, such as plants and animals...'
    )

def Fib_Num():

  for i in range(25):
    print(anti_flick+'\n',' '*i,text_words[0])
    time.sleep(.10)

  num1=0
  num2=1
  fib=[num1,num2]

  while True:
    num3=num1+num2
    fib.append(num3)
    num1=num2
    num2=num3
    clock=(time.asctime())

    print(anti_flick+'\n',' '*25,text_words[0],text_words[1],text_words[2])

    print(f'\nFibonacci Natural Number Sequence: {text_colours[2]}\
{num1} {text_colours[3]}+ {text_colours[2]}{num2}{text_colours[3]} = \
({text_colours[0]}{num1+num3}{text_colours[3]}){text_colours[3]}\n\n\
Fibonacci Natural Numbers: "{text_colours[0]}{num1+num3:,}{text_colours[3]}\
"\n\n{text_colours[0]}Date & Time:\n\n{clock}')

    time.sleep(1)

Fib_Num()
