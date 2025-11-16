# Tkinter Random Gridlines with Random Colours Python program example:

from time import sleep as wait
from random import*
from tkinter import*

Random_Gridlines = Tk()

black = '#000000'
white = '#ffffff'
red = '#ff0000'
yellow = '#ffff00'
blue = '#0000ff'
green = '#00ff00'
pink = '#ff00ff'
cyan = '#00ffff'

w,h = 1920,1080
r,c = 0,0
rand1,rand2 = 0,15
randint1,randint2 = -1920,1920
loop = 20
seconds = .08
everything = 'all'

Random_Gridlines.title('Tkinter Random Lines with Random Colours')

def random_colour_code():
    hex_chars = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    colour_code = '#'

    for i in range(0,6):
        colour_code = colour_code+choice(hex_chars)
    return colour_code

lines_canvas = Canvas(Random_Gridlines,width = w,height = h,background = black)
lines_canvas.grid(row = r,column = c)

try:
    while True:
        for i in range(loop):  # Increse the for loop value to add more lasers on the screen output.
            random_width = randint(rand1,rand2)

            x = randint(randint1,randint2)

            lines_canvas.create_line(r,c+x,w,r+x,fill = random_colour_code(),width = random_width)
            lines_canvas.create_line(r+x,c,r+x,h,fill = random_colour_code(),width = random_width)

        lines_canvas.update()
        wait(seconds)
        lines_canvas.delete(everything)
except TclError:pass

Random_Gridlines.mainloop()
