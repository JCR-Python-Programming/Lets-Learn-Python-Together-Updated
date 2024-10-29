# Auto Type Text Colour Effects with Sound Python program example.

# Created by Joseph C. Richardson, GitHub.com

# Please note: after you save your file, you must double click this file to view its cool
# coloured text effects and layout. Next, create a folder for your typing sound effect
# wave file and your Python file so they can execute/run together. Note: all sound files
# must be wave format; Python will not execute/run sound files in mp3 format, without
# importing a Python module for that, which I do not have at this moment.

# import these three Python modules below

import os,time,winsound

# Create a tuple variable for all seven colour values,
# starting at index 0 through index 6. Note: index numbers
# always start at 0, not 1. Be careful of how you count
# how many values you have within tuples and lists alike.

text_colours=(
    '\x1b[31m', # index 0 = red
    '\x1b[32m', # index 1 = green
    '\x1b[33m', # index 2 = yellow
    '\x1b[34m', # index 3 = blue
    '\x1b[35m', # index 4 = purple
    '\x1b[36m', # index 5 = cyan
    '\x1b[37m'  # index 6 = white
    )

# Create some more variables to make programming less bulky
# and less code redundant on the programming part.

clear_screen='cls'
single_line_break='\n'
double_line_break='\n\n'
indent=' '*2
wave_sound='TYPE'

# Create another tuple variable for a print() function text string value
# and a clear_screen variable that contains the os value 'cls' to clear
# the screen output, while executing/running the Python program.

text_words=(
f"{single_line_break}{indent}This is how you do auto type text colour effects \
with sound in Python. {double_line_break}{indent}You can type as many lines \
of text you please by invoking the '\\' {single_line_break}{indent}backslash to \
create hard returns within the text code programming{single_line_break}{indent}\
part of the Python program only.",clear_screen)

length=0

while length<=len(text_words[0]):
    for i in text_colours:
        print(i+text_words[0][:length])
        winsound.PlaySound(wave_sound,winsound.SND_ASYNC)
        time.sleep(.08)
        os.system(text_words[1])
        length+=1

print(text_colours[6]+text_words[0])

# Place an input() function so you can press the Enter key to close the
# Python program when you want to, without it closing right away after
# it's executed.

input(f'{double_line_break}{indent}Press Enter to exit and close this Python program example:')
