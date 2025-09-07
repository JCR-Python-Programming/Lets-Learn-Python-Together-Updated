# Subroutine Python Program Example:

# Created by Joseph C. Richardson, GitHub.com

# This is the Python program on how to create subroutines with
# define functions. If you want to use wave sounds within your
# Python program, you must import the winsound module. You
# can also create variables to store all your text string values to
# make your Python code neat and compact. Variables are also
# great for data manipulation with their stored values. You can
# create variables with an array of stored values, and them call
# them, along with their index number values, starting from zero
# and onward. Python programming is largely based around
# define functions, known as def functions for short. Def functions
# can store blocks of Python code inside them, that can execute
# run the Python code from within when called upon. You can
# call def functions as many times as you like. Def functions and
# conditional while loops are what make subroutines in Python
# possible, hence there are no line numbers in Python, like there
# were in older programming languages, such as BASIC: (Beginners,
# All-purpose Symbolic Instruction Code). Type and execute/run
# this Python program example below. Just remember that learning
# also means doing. In order to learn anything, you have to do it
# as well. Now, let's get into it shall we!

import winsound

wave_sounds = (
  'Subroutine Fun',
  'Subroutine 1',
  'Subroutine 2',
  'Subroutine 3',
  'Pick a Subroutine',
  'Pick a sub2',
  'Sorry',
  'quit subroutine',
  'Close Program Example')

paragraph = (
  '''How can we create subroutines in Python,when there
are no line numbers at all to create subroutines?
Because Python has no  line numbers. How can we
create subroutines in Python?

The answer is simple! We create define functions
that execute Python code from within them when
they are called upon through conditional while
loops. Let's use my wave sound voice to make
this Python program much more fun! as well as
much more easy to understand what's happening
throughout the Python program execution/run.
Each one of my wave sound voice files will be
executed while you, the user presses the number
keys to tell the Python program which subroutine
to execute/run. ''')

text = (
  '\nThis is subroutine number one, using a define function.',
  '\nThis is subroutine number two, using another define function.',
  '\nThis is subroutine number three, using another define function.',
  '\nPick a subroutine 1, 2 or 3 or press Q to close the program.',
  '\nPick a subroutine: ',
  '\nI will now exit and close this Python program example.',
  '''\nSorry! No subroutine for that.
You can press the letter Q to quit and exit this program example at any time.'''
  )

one,two,three,quit_prog = '1','2','3','q'

def subroutine_one():
  print(text[0])
  winsound.PlaySound(wave_sounds[1],winsound.SND_ALIAS)
  winsound.PlaySound(wave_sounds[5],winsound.SND_ASYNC)

def subroutine_two():
  print(text[1])
  winsound.PlaySound(wave_sounds[2],winsound.SND_ALIAS)
  winsound.PlaySound(wave_sounds[5],winsound.SND_ASYNC)

def subroutine_three():
  print(text[2])
  winsound.PlaySound(wave_sounds[3],winsound.SND_ALIAS)
  winsound.PlaySound(wave_sounds[5],winsound.SND_ASYNC)

print(paragraph)

winsound.PlaySound(wave_sounds[0],winsound.SND_ALIAS)
print(text[3])
winsound.PlaySound(wave_sounds[4],winsound.SND_ALIAS)
winsound.PlaySound(wave_sounds[5],winsound.SND_ASYNC)

while True:
  user_input = input(text[4]).lower().strip()
  if user_input == one:
    subroutine_one()
  elif user_input == two:
    subroutine_two()
  elif user_input == three:
    subroutine_three()
  elif user_input == quit_prog:
    print(text[5])
    winsound.PlaySound(wave_sounds[8],winsound.SND_ALIAS)
    break
  else:
    print(text[6])
    winsound.PlaySound(wave_sounds[6],winsound.SND_ALIAS)
    winsound.PlaySound(wave_sounds[7],winsound.SND_ALIAS)
    winsound.PlaySound(wave_sounds[5],winsound.SND_ASYNC)

# I am almost a complete Walking Human Computer Science Research
# Laboratory Machine on Two Legs... 😁
