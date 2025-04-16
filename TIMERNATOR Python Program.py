# TIMERNATOR Python Program Example

# Created by Joseph C. Richardson, GitHub.com

# Try this fun Timernator Clock Python program example.

# Note: you must execute/run the program from
# the OS output screen, via double-clicking the Python
# program file itself.

import os,datetime,asyncio,winsound
from time import sleep as timernator

os.system('title TIMERNATOR')

text_colour=(
    '\x1b[31m',  # index 0 = red
    '\x1b[32m',  # index 1 = green
    '\x1b[33m',  # index 2 = yellow
    '\x1b[36m'   # index 3 = light blue
    )

special_fx=(
    f'{text_colour[0]}TIMERNATOR', # index 0 = special_fx

    'Speech Off',  # index 1 = special_fx

    'cls','\n','\n\n',' '  # index 2 = special_fx
    )

time_fx=(
f'{text_colour[2]}12 Hour {text_colour[0]}%I\
{text_colour[1]}:{text_colour[0]}%M{text_colour[1]}\
:{text_colour[0]}%S {text_colour[2]}%p',  # index 0 = time_fx

f'{text_colour[2]}24 Hour {text_colour[0]}%H{text_colour[1]}:\
{text_colour[0]}%M{text_colour[1]}:{text_colour[0]}%S',  # index 1 = time_fx

f'{text_colour[2]}%A %B {text_colour[0]}%d{text_colour[1]}:\
{text_colour[0]}%Y',f'{text_colour[2]}Week{text_colour[1]}:\
{text_colour[0]}%U {text_colour[2]}Day{text_colour[1]}:\
{text_colour[0]}%j'  # index 2 = time_fx
    )

text_fx=(
    f'{text_colour[3]}You\'re TIMERNATED!',  # index 0 = text_fx

    f'{text_colour[3]}Look at me if you want the time.',  # index 1 = text_fx

    f'{text_colour[3]}I need your hours, your minutes and your seconds.',  # index 2 = text_fx

    f'{text_colour[3]}I swear I will tell the time.',  # index 3 = text_fx

    f'{text_colour[3]}I cannot self timernate.'  # index 4 = text_fx
    )

redundant_code1='''
print(
    special_fx[3],
    special_fx[5]*1,
    special_fx[0],
    special_fx[4],
    special_fx[5]*1,
    text_fx[x]
    )
'''
redundant_code2='''
print(
    special_fx[3],
    special_fx[5]*1,
    timer.strftime(time_fx[y])
    )
'''
while True:
    for x in range(4):
        os.system(special_fx[2])
        winsound.PlaySound(
            special_fx[1],winsound.SND_ASYNC
            )

        exec(redundant_code1)

        for y in range(4):
            timer=datetime.datetime.now()
            exec(redundant_code2)

        timernator(1)

        os.system(special_fx[2])

        winsound.PlaySound(
            special_fx[1],winsound.SND_ASYNC
            )

        exec(redundant_code1)

        for y in range(4):
            timer=datetime.datetime.now()
            exec(redundant_code2)

        timernator(1)

        os.system(special_fx[2])

        winsound.PlaySound(
            special_fx[1],winsound.SND_ASYNC
            )

        exec(redundant_code1)

        for y in range(4):
            timer=datetime.datetime.now()
            exec(redundant_code2)

        timernator(1)

# I am almost a complete Walking Human Computer Science Research
# Laboratory Machine on Two Legs... 😁
