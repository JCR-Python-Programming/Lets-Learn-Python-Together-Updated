import time
import os;os.system('title Binary Beat')
import atexit

os.system(f'title Fibonacci Natural Number Sequence')

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
