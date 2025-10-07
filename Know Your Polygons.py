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
  'How many equal sides does a Triangle have?',  # index[0]
  'How many equal sides does a Square have?',  # index[1]
  'How many equal sides does a Pentagon have?',  # index[2]
  'How many equal sides does a Hexagon have?',  # index[3]
  'How many equal sides does a Heptagon have?',  # index[4]
  'How many equal sides does a Octagon have?',  # index[5]
  'How many equal sides does a Nonagon have?',  # index[6]
  'How many equal sides does a Decagon have?',  # index[7]
  'How many equal sides does a Hendecagon have?',  # index[8]
  'How many equal sides does a Dodecagon have?',  # index[9]
  'How many equal sides does a Tridecagon have?',  # index[10]
  'How many equal sides does a Tetradecagon have?',  # index[11]
  'How many equal sides does a Pentadecagon have?',  # index[12]
  'How many equal sides does a Hexadecagon have?',  # index[13]
  'How many equal sides does a Heptadecagon have?',  # index[14]
  'How many equal sides does a Octadecagon have?',  # index[15]
  'How many equal sides does a Enneadecagon have?',  # index[16]
  'How many equal sides does a Icosagon have?')  # index[17]

sides = (
  'two equal sides',  # index[0]
  'three equal sides',  # index[1]
  'four equal sides',  # index[2]
  'five equal sides',  # index[3]
  'six equal sides',  # index[4]
  'seven equal sides',  # index[5]
  'eight equal sides',  # index[6]
  'nine equal sides',  # index[7]
  'ten equal sides',  # index[8]
  'eleven equal sides',  # index[9]
  'twelve equal sides',  # index[10]
  'thirteen equal sides',  # index[11]
  'fourteen equal sides',  # index[12]
  'fifteen equal sides',  # index[13]
  'sixteen equal sides',  # index[14]
  'seventeen equal sides',  # index[15]
  'eighteen equal sides',  # index[16]
  'nineteen equal sides',  # index[17]
  'twenty equal sides')  # index[18]

answers = (
  'Triangles have three equal sides.',  # index[0]
  'Squares have four equal sides.',  # index[1]
  'Pentagons have five equal sides.',  # index[2]
  'Hexagons have six equal sides.',  # index[3]
  'Heptagons have seven equal sides.',  # index[4]
  'Octagons have eight equal sides.',  # index[5]
  'Nonagons have nine equal sides.',  # index[6]
  'Decagons have ten equal sides.',  # index[7]
  'Hendecagons have eleven equal sides.',  # index[8]
  'Dodecagons have twelve equal sides.',  # index[9]
  'Tridecagons have thirteen equal sides.',  # index[10]
  'Tetradecagons have fourteen equal sides.',  # index[11]
  'Pentadecagons have fifteen equal sides.',  # index[12]
  'Hexadecagons have sixteen equal sides.',  # index[13]
  'Heptadecagons have seventeen equal sides.',  # index[14]
  'Octadecagons have eighteen equal sides.',  # index[15]
  'Enneadecagons have nineteen equal sides.',  # index[16]
  'Icosagons have twenty equal sides.')  # index[17]

question_prompts = (
  f'{text_col[2]}{polygons[0]}\n\n{text_col[1]}(a) {text_col[2]}{sides[2]}\
\n{text_col[1]}(b) {text_col[2]}{sides[1]}\n{text_col[1]}(c) {text_col[2]}{sides[0]}',  # index[0]

  f'{text_col[2]}{polygons[1]}\n\n{text_col[1]}(a) {text_col[2]}{sides[3]}\
\n{text_col[1]}(b) {text_col[2]}{sides[1]}\n{text_col[1]}(c) {text_col[2]}{sides[2]}',  # index[1]

  f'{text_col[2]}{polygons[2]}\n\n{text_col[1]}(a) {text_col[2]}{sides[3]}\
\n{text_col[1]}(b) {text_col[2]}{sides[1]}\n{text_col[1]}(c) {text_col[2]}{sides[2]}',  # index[2]

  f'{text_col[2]}{polygons[3]}\n\n{text_col[1]}(a) {text_col[2]}{sides[4]}\
\n{text_col[1]}(b) {text_col[2]}{sides[5]}\n{text_col[1]}(c) {text_col[2]}{sides[3]}',  # index[3]

  f'{text_col[2]}{polygons[4]}\n\n{text_col[1]}(a) {text_col[2]}{sides[7]}\
\n{text_col[1]}(b) {text_col[2]}{sides[5]}\n{text_col[1]}(c) {text_col[2]}{sides[6]}',  # index[4]

  f'{text_col[2]}{polygons[5]}\n\n{text_col[1]}(a) {text_col[2]}{sides[5]}\
\n{text_col[1]}(b) {text_col[2]}{sides[4]}\n{text_col[1]}(c) {text_col[2]}{sides[6]}',   # index[5]

  f'{text_col[2]}{polygons[6]}\n\n{text_col[1]}(a) {text_col[2]}{sides[5]}\
\n{text_col[1]}(b) {text_col[2]}{sides[7]}\n{text_col[1]}(c) {text_col[2]}{sides[8]}',  # index[6]

  f'{text_col[2]}{polygons[7]}\n\n{text_col[1]}(a) {text_col[2]}{sides[9]}\
\n{text_col[1]}(b) {text_col[2]}{sides[8]}\n{text_col[1]}(c) {text_col[2]}{sides[10]}',  # index[7]

  f'{text_col[2]}{polygons[8]}\n\n{text_col[1]}(a) {text_col[2]}{sides[8]}\
\n{text_col[1]}(b) {text_col[2]}{sides[10]}\n{text_col[1]}(c) {text_col[2]}{sides[9]}',  # index[8]

  f'{text_col[2]}{polygons[9]}\n\n{text_col[1]}(a) {text_col[2]}{sides[8]}\
\n{text_col[1]}(b) {text_col[2]}{sides[10]}\n{text_col[1]}(c) {text_col[2]}{sides[9]}',  # index[9]

  f'{text_col[2]}{polygons[10]}\n\n{text_col[1]}(a) {text_col[2]}{sides[11]}\
\n{text_col[1]}(b) {text_col[2]}{sides[9]}\n{text_col[1]}(c) {text_col[2]}{sides[12]}',  # index[10]

  f'{text_col[2]}{polygons[11]}\n\n{text_col[1]}(a) {text_col[2]}{sides[11]}\
\n{text_col[1]}(b) {text_col[2]}{sides[12]}\n{text_col[1]}(c) {text_col[2]}{sides[10]}',  # index[11]

  f'{text_col[2]}{polygons[12]}\n\n{text_col[1]}(a) {text_col[2]}{sides[14]}\
\n{text_col[1]}(b) {text_col[2]}{sides[11]}\n{text_col[1]}(c) {text_col[2]}{sides[13]}',  # index[12]

  f'{text_col[2]}{polygons[13]}\n\n{text_col[1]}(a) {text_col[2]}{sides[15]}\
\n{text_col[1]}(b) {text_col[2]}{sides[13]}\n{text_col[1]}(c) {text_col[2]}{sides[14]}',  # index[13]

  f'{text_col[2]}{polygons[14]}\n\n{text_col[1]}(a) {text_col[2]}{sides[16]}\
\n{text_col[1]}(b) {text_col[2]}{sides[14]}\n{text_col[1]}(c) {text_col[2]}{sides[15]}',  # index[14]

  f'{text_col[2]}{polygons[15]}\n\n{text_col[1]}(a) {text_col[2]}{sides[17]}\
\n{text_col[1]}(b) {text_col[2]}{sides[16]}\n{text_col[1]}(c) {text_col[2]}{sides[18]}',  # index[15]

  f'{text_col[2]}{polygons[16]}\n\n{text_col[1]}(a) {text_col[2]}{sides[16]}\
\n{text_col[1]}(b) {text_col[2]}{sides[17]}\n{text_col[1]}(c) {text_col[2]}{sides[18]}',  # index[16]

  f'{text_col[2]}{polygons[17]}\n\n{text_col[1]}(a) {text_col[2]}{sides[18]}\
\n{text_col[1]}(b) {text_col[2]}{sides[17]}\n{text_col[1]}(c) {text_col[2]}{sides[16]}')  # index[17]

title = 'know your polygons'.title()

learn_your_polygons = (f"\n{text_col[5]}{title}\n\n{text_col[0]}Oh No! \
You don't know any of your Polygons... Sorry! Please try again.\n")

choice = ('b','c','a','a','b','c','b','b','c','b','a','b','c','c','c','b','b','a')  # choice values: 0 through 17 = 18

def subroutine():

  score = 0
  loop = 0

  while loop <= 17:
    os.system(text_col[7])

    button = input(
      text_col[5]+f'\n{title}\n\n'+text_col[2]+question_prompts[loop]+
      '\n\n'+text_col[0]+'READY: '+text_col[1]).strip()

    if button == (choice[loop]):
      score += 1

    loop += 1

    os.system(text_col[7])

  if score / len(question_prompts) == 0:
    print(learn_your_polygons)

    for i in answers:
      print(text_col[5]+i)

  elif score < len(question_prompts):
    print(f'\n{text_col[5]}{title}\n\n{text_col[2]}You got \
{score}/{len(question_prompts)} questions correct:\n\nCongratulations! \
Your Grand Total Prize Winnings: {text_col[1]}${score*100*score:,}.00 {text_col[2]}Dollars.')

  elif score == len(question_prompts) == 18:
    print(f'{text_col[5]}{title}\n\n{text_col[2]}You got \
{score}/{len(question_prompts)} questions correct:\n\nCongratulations! {text_col[4]}\
Wow! You got them all right. {text_col[2]}Your Grand Total Prize Winnings with Bonus: {text_col[1]}${score\
*500*score:,}.00 {text_col[2]}Dollars.')

  else:
    print(f'\n{text_col[5]}{title}\n\n{text_col[2]}You got \
{score}/{len(question_prompts)} questions correct:\n\nCongratulations! Your Grand Total \
Prize Winnings: {text_col[1]}${score*100*score:,}.00 {text_col[2]}Dollars.')

  play_again = input(f'\n{text_col[2]}Press P to play again or press ENTER to exit: ').lower().strip()

  if play_again == 'p':
    subroutine()

  elif play_again == '':
    pass

subroutine()
