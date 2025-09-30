# Know Your Polygons game Python program example:

# See what happens when you type and execute/run this guessing game program
# example below. Note: you must execute/run the program from the OS output screen,
# via double-clicking the Python program file itself.

# Save the Python file as 'Know Your Polygons.py'

import os

text_col = (
  '\x1b[31m',  # index 0 = red
  '\x1b[32m',  # index 1 = green
  '\x1b[33m',  # index 2 = yellow
  '\x1b[34m',  # index 3 = blue
  '\x1b[35m',  # index 4 = purple
  '\x1b[36m',  # index 5 = cyan
  '\x1b[37m',  # index 6 = white
  'cls')  # index 7 = clear screen

question_prompts = (
  f'{text_col[2]}How many sides does a Triangle have?\n\n{text_col[1]}(a) {text_col[2]}four sides\
\n{text_col[1]}(b) {text_col[2]}three sides\n{text_col[1]}(c) {text_col[2]}two sides',

  f'{text_col[2]}How many sides does a Square have?\n\n{text_col[1]}(a) {text_col[2]}Two sides\
\n{text_col[1]}(b) {text_col[2]}Three sides\n{text_col[1]}(c) {text_col[2]}Four sides',

  f'{text_col[2]}How many sides does a Pentagon have?\n\n{text_col[1]}(a) {text_col[2]}four sides\
\n{text_col[1]}(b) {text_col[2]}five sides\n{text_col[1]}(c) {text_col[2]}Three sides',

  f'{text_col[2]}How many sides does a Hexagon have?\n\n{text_col[1]}(a) {text_col[2]}six sides\
\n{text_col[1]}(b) {text_col[2]}five sides\n{text_col[1]}(c) {text_col[2]}two sides',

  f'{text_col[2]}How many sides does a Octagon have?\n\n{text_col[1]}(a) {text_col[2]}four sides\
\n{text_col[1]}(b) {text_col[2]}six sides\n{text_col[1]}(c) {text_col[2]}eight sides',

  f'{text_col[2]}How many sides does a Dodecagon have?\n\n{text_col[1]}(a) {text_col[2]}eight\
sides\n{text_col[1]}(b) {text_col[2]}three sides\n{text_col[1]}(c) {text_col[2]}twelve sides',

  f'{text_col[2]}How many sides does a Hexadecagon have?\n\n{text_col[1]}(a) {text_col[2]}sixteen\
sides\n{text_col[1]}(b) {text_col[2]}eight sides\n{text_col[1]}(c) {text_col[2]}six sides')

prompt = ('b','c','b','a','c','c','a')

score = 0
loop = 0

while loop <= 6:

  os.system(text_col[7])
  button = input((text_col[1])+'\nKnow Your Polygons!\n\n'+(text_col[2])+'Know Your Polygons\n\n'+\
  question_prompts[loop]+'\n\n'+(text_col[0])+'READY: '+(text_col[1])).strip()

  if button == (prompt[loop]):
      score += 1

  loop += 1

  os.system(text_col[7])

print(f'\n{text_col[2]}Know Your Polygons\n\n{text_col[2]}You got \
{score}/{len(question_prompts)} questions correct.\nCongratulations! Your total \
Prize Winnings: {text_col[1]}${score*100*score:,}.00 {text_col[2]}Dollars.')

input(f'\n{text_col[5]}Press Enter to exit:')
