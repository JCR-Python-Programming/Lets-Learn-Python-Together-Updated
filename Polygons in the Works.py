# Know Your Polygons game Python program example:

# See what happens when you type and execute/run this guessing game program
# example below.

# Note: you must execute/run the program from the OS output screen,
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

polygons = (
  'How many sides does a Triangle have?',  # index[0]
  'How many sides does a Square have?',  # index[1]
  'How many sides does a Pentagon have?',  # index[2]
  'How many sides does a Hexagon have?',  # index[3]
  'How many sides does a Heptagon have?',  # index[4]
  'How many sides does a Octagon have?',  # index[5]
  'How many sides does a Nonagon have?',  # index[6]
  'How many sides does a Decagon have?',  # index[7]
  'How many sides does a Hendecagon have?',  # index[8]
  'How many sides does a Dodecagon have?',  # index[9]
  'How many sides does a Tridecagon have?',  # index[10]
  'How many sides does a Tetradecagon have?',  # index[11]
  'How many sides does a Pentadecagon have?',  # index[12]
  'How many sides does a Hexadecagon have?',  # index[13]
  'How many sides does a Heptadecagon have?',  # index[14]
  'How many sides does a Octadecagon have?',  # index[15]
  'How many sides does a Enneadecagon have?',  # index[16]
  'How many sides does a Icosagon have?')  # index[17]

sides = (
  'two sides',  # index[0]
  'three sides',  # index[1]
  'four sides',  # index[2]
  'five sides',  # index[3]
  'six sides',  # index[4]
  'seven sides',  # index[5]
  'eight sides',  # index[6]
  'nine sides',  # index[7]
  'ten sides',  # index[8]
  'eleven sides',  # index[9]
  'twelve sides',  # index[10]
  'thirteen sides',  # index[11]
  'fourteen sides',  # index[12]
  'fifteen sides',  # index[13]
  'sixteen sides',  # index[14]
  'seventeen sides',  # index[15]
  'eighteen sides',  # index[16]
  'nineteen sides',  # index[17]
  'twenty sides')  # index[18]

title = 'know your polygons'.title()

learn_your_polygons = (f"\n{text_col[5]}{title}\n\n{text_col[0]}Oh No! You don't know \
any of your Polygons... Sorry: Please try again.\
\n\n{text_col[2]}Triangles have three equal sides.\
\nSquares have four equal sides.\nPentagons have five equal sides.\
\nHexagons have six equal sides.\nHeptagons have seven equal sides.\
\nOctagons have eight equal sides.\nNonagons have nine equal sides.\
\nDecagons have ten equal sides.\nHendecagons have eleven equal sides.\
\nDodecagons have twelve equal sides.\nTridecagons have thirteen equal sides.\
\nTetradecagons have fourteen equal sides.\nPentadecagons have fifteen equal sides.\
\nHexadecagons have sixteen equal sides.\nHeptadecagons have seventeen equal sides.\
\nOctadecagons have eighteen equal sides.\nEnneadecagons have nineteen equal sides.\
\nIcosagons have twenty equal sides.")

question_prompts = (
  f'{text_col[2]}{polygons[0]}\n\n{text_col[1]}(a) {text_col[2]}{sides[2]}\
\n{text_col[1]}(b) {text_col[2]}{sides[1]}\n{text_col[1]}(c) {text_col[2]}{sides[0]}',

  f'{text_col[2]}{polygons[1]}\n\n{text_col[1]}(a) {text_col[2]}{sides[3]}\
\n{text_col[1]}(b) {text_col[2]}{sides[1]}\n{text_col[1]}(c) {text_col[2]}{sides[2]}',

  f'{text_col[2]}{polygons[2]}\n\n{text_col[1]}(a) {text_col[2]}{sides[3]}\
\n{text_col[1]}(b) {text_col[2]}{sides[1]}\n{text_col[1]}(c) {text_col[2]}{sides[2]}',

  f'{text_col[2]}{polygons[3]}\n\n{text_col[1]}(a) {text_col[2]}{sides[4]}\
\n{text_col[1]}(b) {text_col[2]}{sides[5]}\n{text_col[1]}(c) {text_col[2]}{sides[3]}',

  f'{text_col[2]}{polygons[4]}\n\n{text_col[1]}(a) {text_col[2]}{sides[7]}\
\n{text_col[1]}(b) {text_col[2]}{sides[5]}\n{text_col[1]}(c) {text_col[2]}{sides[6]}',

  f'{text_col[2]}{polygons[5]}\n\n{text_col[1]}(a) {text_col[2]}{sides[5]}\
\n{text_col[1]}(b) {text_col[2]}{sides[4]}\n{text_col[1]}(c) {text_col[2]}{sides[6]}',

  f'{text_col[2]}{polygons[6]}\n\n{text_col[1]}(a) {text_col[2]}{sides[5]}\
\n{text_col[1]}(b) {text_col[2]}{sides[7]}\n{text_col[1]}(c) {text_col[2]}{sides[8]}',

  f'{text_col[2]}{polygons[7]}\n\n{text_col[1]}(a) {text_col[2]}{sides[9]}\
\n{text_col[1]}(b) {text_col[2]}{sides[8]}\n{text_col[1]}(c) {text_col[2]}{sides[10]}',

  f'{text_col[2]}{polygons[8]}\n\n{text_col[1]}(a) {text_col[2]}{sides[8]}\
\n{text_col[1]}(b) {text_col[2]}{sides[10]}\n{text_col[1]}(c) {text_col[2]}{sides[9]}',

  f'{text_col[2]}{polygons[9]}\n\n{text_col[1]}(a) {text_col[2]}{sides[8]}\
\n{text_col[1]}(b) {text_col[2]}{sides[10]}\n{text_col[1]}(c) {text_col[2]}{sides[9]}',

  f'{text_col[2]}{polygons[10]}\n\n{text_col[1]}(a) {text_col[2]}{sides[11]}\
\n{text_col[1]}(b) {text_col[2]}{sides[9]}\n{text_col[1]}(c) {text_col[2]}{sides[12]}',

  f'{text_col[2]}{polygons[11]}\n\n{text_col[1]}(a) {text_col[2]}{sides[11]}\
\n{text_col[1]}(b) {text_col[2]}{sides[12]}\n{text_col[1]}(c) {text_col[2]}{sides[10]}',

  f'{text_col[2]}{polygons[12]}\n\n{text_col[1]}(a) {text_col[2]}{sides[14]}\
\n{text_col[1]}(b) {text_col[2]}{sides[11]}\n{text_col[1]}(c) {text_col[2]}{sides[13]}',

  f'{text_col[2]}{polygons[13]}\n\n{text_col[1]}(a) {text_col[2]}{sides[15]}\
\n{text_col[1]}(b) {text_col[2]}{sides[13]}\n{text_col[1]}(c) {text_col[2]}{sides[14]}',

  f'{text_col[2]}{polygons[14]}\n\n{text_col[1]}(a) {text_col[2]}{sides[16]}\
\n{text_col[1]}(b) {text_col[2]}{sides[14]}\n{text_col[1]}(c) {text_col[2]}{sides[15]}',

  f'{text_col[2]}{polygons[15]}\n\n{text_col[1]}(a) {text_col[2]}{sides[17]}\
\n{text_col[1]}(b) {text_col[2]}{sides[16]}\n{text_col[1]}(c) {text_col[2]}{sides[18]}',

  f'{text_col[2]}{polygons[16]}\n\n{text_col[1]}(a) {text_col[2]}{sides[16]}\
\n{text_col[1]}(b) {text_col[2]}{sides[17]}\n{text_col[1]}(c) {text_col[2]}{sides[18]}',

  f'{text_col[2]}{polygons[17]}\n\n{text_col[1]}(a) {text_col[2]}{sides[18]}\
\n{text_col[1]}(b) {text_col[2]}{sides[17]}\n{text_col[1]}(c) {text_col[2]}{sides[16]}')  # 18 tuple values: 0 through 17 = 18 values

print(len(question_prompts))

prompt = ('b','c','a','a','b','c','b','b','c','b','a','b','c','c','c','b','b','a')

score = 0
loop = 0

while loop <= 17:
  os.system(text_col[7])

  button = input((text_col[5])+f'\n{title}\n\n'+(text_col[2])+\

  question_prompts[loop]+'\n\n'+(text_col[0])+'READY: '+(text_col[1])).strip()

  if button == (prompt[loop]):
      score += 1

  loop += 1

  os.system(text_col[7])

if score / len(question_prompts) == 0:
  print(learn_your_polygons)

elif score < len(question_prompts):
  print(f'\n{text_col[5]}{title}\n\n{text_col[2]}You got\
 {score}/{len(question_prompts)} questions correct:\n\nCongratulations! Your total \
Prize Winnings: {text_col[1]}${score*100*score:,}.00 {text_col[2]}Dollars.\
\n\nCorrect answers you got {text_col[0]}wrong{text_col[2]}:')

else:
  print(f'\n{text_col[5]}{title}\n\n{text_col[2]}You got\
 {score}/{len(question_prompts)} questions correct:\n\nCongratulations! Your total \
Prize Winnings: {text_col[1]}${score*100*score:,}.00 {text_col[2]}Dollars.')

input(f'\n{text_col[6]}Press Enter to exit:')
