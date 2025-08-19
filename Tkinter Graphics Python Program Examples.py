# Tkinter Graphics Python Program Examples:

# Created by JCR, GitHub.com

# Tkinter Rectangle Graphics Python program example:

from tkinter import*

rectangle_graphics = Tk()

black = '#000000'
white = '#ffffff'
red = '#ff0000'
yellow = '#ffff00'
blue = '#0000ff'
green = '#00ff00'
pink = '#ff00ff'
cyan = '#00ffff'

x = 1
j = 5
y = 740

rectangle_graphics.title('Tkinter Rectangle Graphics')

rectangle = Canvas(rectangle_graphics,height = y,width = y,background = black)

for i in range(x,370,15):
    rectangle.create_rectangle(x+i,x+i,y-i,y-i,width = j,outline = cyan)

rectangle.pack()

rectangle_graphics.mainloop()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Tkinter Oval Graphics Python program example:

from tkinter import*

oval_graphics = Tk()

black = '#000000'
white = '#ffffff'
red = '#ff0000'
yellow = '#ffff00'
blue = '#0000ff'
green = '#00ff00'
pink = '#ff00ff'
cyan = '#00ffff'

x = 1
j = 5
y = 740

oval_graphics.title('Tkinter Oval Graphics')

oval = Canvas(oval_graphics,height = y,width = y,background = black)

for i in range(x,370,15):
    oval.create_oval(x+i,x+i,y-i,y-i,width = j,outline = cyan)

oval.pack()

oval_graphics.mainloop()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Tkinter Digital String Art Design Python program example:

from tkinter import*

digital_string_art = Tk()

black = '#000000'
white = '#ffffff'
red = '#ff0000'
yellow = '#ffff00'
blue = '#0000ff'
green = '#00ff00'
pink = '#ff00ff'
cyan = '#00ffff'

x = 0
y = 740

digital_string_art.title('Digital String Art Design')

draw = Canvas(digital_string_art,height = y,width = y,background = black)

for i in range(x,y,4):
    draw.create_line(x+i,x+i ,y,x,y,x,y,y,y,y,y,y,y,y,x,y,x+i,x+i,fill = cyan)

draw.pack()

digital_string_art.mainloop()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Tkinter Rectangle & Oval Zoom I/O Python program example:

from tkinter import*
from time import sleep as wait

shape_zoom = Tk()

black = '#000000'
white = '#ffffff'
red = '#ff0000'
yellow = '#ffff00'
blue = '#0000ff'
green = '#00ff00'
pink = '#ff00ff'
cyan = '#00ffff'

x = 1
xn = -1
y = 740
delay = .01
line_width = 5
range_diameter = 367
everything = 'all'

shape_zoom.title('Rectangle & Oval Zoom I/O')

shape = Canvas(shape_zoom,height = y,width = y,background = black)

try:
    while True:
        for i in range(range_diameter,x,xn):
            shape.create_rectangle(
                x+i,x+i,y-i,y-i,width = line_width,fill = green,outline = red)

            shape.update()
            wait(delay)
            shape.delete(everything)
            shape.pack()

        for i in range(1,range_diameter,x):
            shape.create_rectangle(
                x+i,x+i,y-i,y-i,width = line_width,fill = red,outline = green)

            shape.update()
            wait(delay)
            shape.delete(everything)
            shape.pack()

        for i in range(range_diameter,x,xn):
            shape.create_oval(
                x+i,x+i,y-i,y-i,width = line_width,fill = green,outline = red)

            shape.update()
            wait(delay)
            shape.delete(everything)
            shape.pack()

        for i in range(1,range_diameter,x):
            shape.create_oval(
                x+i,x+i,y-i,y-i,width = line_width,fill = red,outline = green)

            shape.update()
            wait(delay)
            shape.delete(everything)
            shape.pack()
except TclError:pass

shape_zoom.mainloop()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Tkinter Random Lines with Random Colours Python program example:

from time import sleep as wait
from random import*
from tkinter import*

random_lines = Tk()

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

random_lines.title('Tkinter Random Lines with Random Colours')

def random_colour_code():
    hex_chars = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    colour_code = '#'

    for i in range(0,6):
        colour_code = colour_code+choice(hex_chars)
    return colour_code

lines_canvas = Canvas(random_lines,width = w,height = h,background = black)
lines_canvas.grid(row = r,column = c)

try:
    while True:
        for i in range(loop):  # Increse the for loop value to add more lasers on the screen output.
            random_width = randint(rand1,rand2)

            x = randint(randint1,randint2)

            lines_canvas.create_line(
                randint(randint1+x,randint2+x),
                randint(randint1+x,randint2+x),
                randint(randint1+x,randint2+x),
                randint(randint1+x,randint2+x),
                fill = random_colour_code(),
                width = random_width)

        lines_canvas.update()
        wait(seconds)
        lines_canvas.delete(everything)
except TclError:pass

random_lines.mainloop()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Tkinter Random Rectangles with Random Colours Python program example:

from time import sleep as wait
from random import*
from tkinter import*

random_rectangles = Tk()

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
rand1,rand2 = 1,15
randint1,randint2 = -1920,1920
loop = 20
seconds = .08
everything = 'all'

random_rectangles.title('Tkinter Random Rectangles with Random Colours')

def random_colour_code():
    hex_chars = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    colour_code = '#'

    for i in range(0,6):
        colour_code = colour_code+choice(hex_chars)
    return colour_code

rectangles_canvas = Canvas(random_rectangles,width = w,height = h,background = black)
rectangles_canvas.grid(row = r,column = c)

try:
    while True:
        for i in range(loop): # Increse the for loop value to add more rectangles on the screen output.
            random_width = randint(rand1,rand2)

            x = randint(randint1,randint2)

            rectangles_canvas.create_rectangle(
                randint(randint1+x,randint2+x),
                randint(randint1+x,randint2+x),
                randint(randint1+x,randint2+x),
                randint(randint1+x,randint2+x),
                outline = random_colour_code(),
                fill = random_colour_code(),
                width = random_width)

        rectangles_canvas.update()
        wait(seconds)
        rectangles_canvas.delete(everything)
except TclError:pass

random_rectangles.mainloop()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Tkinter Random Ovals with Random Colours Python program example:

from time import sleep as wait
from random import*
from tkinter import*

random_ovals = Tk()

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
rand1,rand2 = 1,15
randint1,randint2 = -1920,1920
loop = 20
seconds = .08
everything = 'all'

random_ovals.title('Tkinter Random Ovals with Random Colours')

def random_colour_code():
    hex_chars = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    colour_code = '#'

    for i in range(0,6):
        colour_code = colour_code+choice(hex_chars)
    return colour_code

ovals_canvas = Canvas(random_ovals,width = w,height = h,background = black)
ovals_canvas.grid(row = r,column = c)

try:
    while True:
        for i in range(loop): # Increse the for loop value to add more ovals on the screen output.
            random_width = randint(rand1,rand2)

            x = randint(randint1,randint2)

            ovals_canvas.create_oval(
                randint(randint1+x,randint2+x),
                randint(randint1+x,randint2+x),
                randint(randint1+x,randint2+x),
                randint(randint1+x,randint2+x),
                outline = random_colour_code(),
                fill = random_colour_code(),
                width = random_width)

        ovals_canvas.update()
        wait(seconds)
        ovals_canvas.delete(everything)
except TclError:pass

random_ovals.mainloop()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Tkinter Random Shapes with Random Colours Python program example:

from time import sleep as wait
from random import*
from tkinter import*

random_shapes = Tk()

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

random_shapes.title('Tkinter Random shapes with Random Colours')

def random_colour_code():
    hex_chars = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    colour_code = '#'

    for i in range(0,6):
        colour_code = colour_code+choice(hex_chars)
    return colour_code

shapes_canvas = Canvas(random_shapes,width = w,height = h,background = black)
shapes_canvas.grid(row = r,column = c)

try:
    while True:
        for i in range(loop):  # Increse the for loop value to add more shapes on the screen output.
            random_width = randint(rand1,rand2)

            x = randint(randint1,randint2)

            shapes_canvas.create_line(
                randint(randint1+x,randint2+x),
                randint(randint1+x,randint2+x),
                randint(randint1+x,randint2+x),
                randint(randint1+x,randint2+x),
                fill = random_colour_code(),
                width = random_width)

            shapes_canvas.create_rectangle(
                randint(randint1+x,randint2+x),
                randint(randint1+x,randint2+x),
                randint(randint1+x,randint2+x),
                randint(randint1+x,randint2+x),
                outline = random_colour_code(),
                fill = random_colour_code(),
                width = random_width)

            shapes_canvas.create_oval(
                randint(randint1+x,randint2+x),
                randint(randint1+x,randint2+x),
                randint(randint1+x,randint2+x),
                randint(randint1+x,randint2+x),
                outline = random_colour_code(),
                fill = random_colour_code(),
                width = random_width)

        shapes_canvas.update()
        wait(seconds)
        shapes_canvas.delete(everything)
except TclError:pass

random_shapes.mainloop()

# I am almost a complete Walking Human Computer Science Research
# Laboratory Machine on Two Legs... 😁
