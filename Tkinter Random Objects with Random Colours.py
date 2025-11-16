# Tkinter Random Objects with Random Colours Python program example:

from time import sleep as wait
from random import*
from tkinter import*

screensaver = Tk()

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
screensaver_time_cycle = 400
everything = 'all'

screensaver.title('Tkinter Random Objects with Random Colours')

def random_colour_code():
    hex_chars = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    colour_code = '#'

    for i in range(0,6):
        colour_code = colour_code+choice(hex_chars)
    return colour_code

objects_canvas = Canvas(screensaver,width = w,height = h,background = black)
objects_canvas.grid(row = r,column = c)

try:
    while True:

        for i in range(screensaver_time_cycle):
            for j in range(loop):  # Increse the for loop value to add more random lines on the screen output.
                random_width = randint(rand1,rand2)

                x = randint(randint1,randint2)

                objects_canvas.create_line(
                randint(randint1+x,randint2+x),
                randint(randint1+x,randint2+x),
                randint(randint1+x,randint2+x),
                randint(randint1+x,randint2+x),
                fill = random_colour_code(),
                width = random_width)

            objects_canvas.update()
            wait(seconds)
            objects_canvas.delete(everything)

        for i in range(screensaver_time_cycle):
            for j in range(loop):  # Increse the for loop value to add more random gridlines on the screen output.
                random_width = randint(rand1,rand2)

                x = randint(randint1,randint2)

                objects_canvas.create_line(r,c+x,w,r+x,fill = random_colour_code(),width = random_width)
                objects_canvas.create_line(r+x,c,r+x,h,fill = random_colour_code(),width = random_width)

            objects_canvas.update()
            wait(seconds)
            objects_canvas.delete(everything)

        for i in range(screensaver_time_cycle):
            for j in range(loop):  # Increse the for loop value to add more random diagonal gridlines on the screen output.
                random_width = randint(rand1,rand2)

                x = randint(randint1,randint2)

                objects_canvas.create_line(r,c+x,w,h+x,fill = random_colour_code(),width = random_width)
                objects_canvas.create_line(r,h+x,w,c+x,fill = random_colour_code(),width = random_width)

            objects_canvas.update()
            wait(seconds)
            objects_canvas.delete(everything)

        for i in range(screensaver_time_cycle):
            for j in range(loop):  # Increse the for loop value to add more random rectangles on the screen output.
                random_width = randint(rand1,rand2)

                x = randint(randint1,randint2)

                objects_canvas.create_rectangle(
                randint(randint1+x,randint2+x),
                randint(randint1+x,randint2+x),
                randint(randint1+x,randint2+x),
                randint(randint1+x,randint2+x),
                outline = random_colour_code(),
                width = random_width)

            objects_canvas.update()
            wait(seconds)
            objects_canvas.delete(everything)

        for i in range(screensaver_time_cycle):
            for j in range(loop):  # Increse the for loop value to add more random ovals on the screen output.
                random_width = randint(rand1,rand2)

                x = randint(randint1,randint2)

                objects_canvas.create_oval(
                randint(randint1+x,randint2+x),
                randint(randint1+x,randint2+x),
                randint(randint1+x,randint2+x),
                randint(randint1+x,randint2+x),
                outline = random_colour_code(),
                width = random_width)

            objects_canvas.update()
            wait(seconds)
            objects_canvas.delete(everything)

        for i in range(screensaver_time_cycle):
            for j in range(loop):  # Increse the for loop value to add more random lines, random rectangles and random ovals on the screen output.
                random_width = randint(rand1,rand2)

                x = randint(randint1,randint2)

                objects_canvas.create_line(
                randint(randint1+x,randint2+x),
                randint(randint1+x,randint2+x),
                randint(randint1+x,randint2+x),
                randint(randint1+x,randint2+x),
                fill = random_colour_code(),
                width = random_width)

                objects_canvas.create_rectangle(
                randint(randint1+x,randint2+x),
                randint(randint1+x,randint2+x),
                randint(randint1+x,randint2+x),
                randint(randint1+x,randint2+x),
                outline = random_colour_code(),
                width = random_width)

                objects_canvas.create_oval(
                randint(randint1+x,randint2+x),
                randint(randint1+x,randint2+x),
                randint(randint1+x,randint2+x),
                randint(randint1+x,randint2+x),
                outline = random_colour_code(),
                width = random_width)

            objects_canvas.update()
            wait(seconds)
            objects_canvas.delete(everything)

        for i in range(screensaver_time_cycle):
            for j in range(loop):  # Increse the for loop value to add more random solid rectangles on the screen output.
                random_width = randint(rand1,rand2)

                x = randint(randint1,randint2)

                objects_canvas.create_rectangle(
                randint(randint1+x,randint2+x),
                randint(randint1+x,randint2+x),
                randint(randint1+x,randint2+x),
                randint(randint1+x,randint2+x),
                outline = random_colour_code(),
                fill = random_colour_code(),
                width = random_width)

            objects_canvas.update()
            wait(seconds)
            objects_canvas.delete(everything)

        for i in range(screensaver_time_cycle):
            for j in range(loop):  # Increse the for loop value to add more random solid ovals on the screen output.
                random_width = randint(rand1,rand2)

                x = randint(randint1,randint2)

                objects_canvas.create_oval(
                randint(randint1+x,randint2+x),
                randint(randint1+x,randint2+x),
                randint(randint1+x,randint2+x),
                randint(randint1+x,randint2+x),
                outline = random_colour_code(),
                fill = random_colour_code(),
                width = random_width)

            objects_canvas.update()
            wait(seconds)
            objects_canvas.delete(everything)

        for i in range(screensaver_time_cycle):
            for j in range(loop):  # Increse the for loop value to add more random solid rectangles and random solid ovals on the screen output.
                random_width = randint(rand1,rand2)

                x = randint(randint1,randint2)

                objects_canvas.create_rectangle(
                randint(randint1+x,randint2+x),
                randint(randint1+x,randint2+x),
                randint(randint1+x,randint2+x),
                randint(randint1+x,randint2+x),
                outline = random_colour_code(),
                fill = random_colour_code(),
                width = random_width)

                objects_canvas.create_oval(
                randint(randint1+x,randint2+x),
                randint(randint1+x,randint2+x),
                randint(randint1+x,randint2+x),
                randint(randint1+x,randint2+x),
                outline = random_colour_code(),
                fill = random_colour_code(),
                width = random_width)

            objects_canvas.update()
            wait(seconds)
            objects_canvas.delete(everything)
except TclError:pass

screensaver.mainloop()
