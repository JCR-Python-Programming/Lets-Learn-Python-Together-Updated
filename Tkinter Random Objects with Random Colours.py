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

w,h = 1365,744
r,c = 0,0
line_width1,line_width2 = 1,20
screen_width1,screen_width2 = -1365,1365
increase_decrease_screen_objects = 20
blink_rate = .12
screensaver_time_cycle = 200
everything = 'all'

screensaver.title('Tkinter Random Objects with Random Colours')

def random_colour_code():
    hex_chars = ['1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    colour_code = '#'

    for i in range(6):
        colour_code = colour_code+choice(hex_chars)
    return colour_code

objects_canvas = Canvas(screensaver,width = w,height = h,background = black)
objects_canvas.grid(row = r,column = c)

try:
    while True:

        for i in range(screensaver_time_cycle):

            # increase_decrease_screen_objects value to add more random lines on the screen output

            for j in range(increase_decrease_screen_objects):
                random_width = randint(line_width1,line_width2)

                x = randint(screen_width1,screen_width2)

                objects_canvas.create_line(
                randint(screen_width1+x,screen_width2+x),
                randint(screen_width1+x,screen_width2+x),
                randint(screen_width1+x,screen_width2+x),
                randint(screen_width1+x,screen_width2+x),
                fill = random_colour_code(),
                width = random_width)

            objects_canvas.update()
            wait(blink_rate)
            objects_canvas.delete(everything)

        for i in range(screensaver_time_cycle):

            # You can increase_decrease_screen_objects value to add more or less random gridlines on the screen output.

            for j in range(increase_decrease_screen_objects):
                random_width = randint(line_width1,line_width2)

                x = randint(screen_width1,screen_width2)

                objects_canvas.create_line(r,c+x,w,r+x,fill = random_colour_code(),width = random_width)
                objects_canvas.create_line(r+x,c,r+x,h,fill = random_colour_code(),width = random_width)

            objects_canvas.update()
            wait(blink_rate)
            objects_canvas.delete(everything)

        for i in range(screensaver_time_cycle):

             # You can increase_decrease_screen_objects value to add more or less random diagonal gridlines on the screen output.

            for j in range(increase_decrease_screen_objects):
                random_width = randint(line_width1,line_width2)

                x = randint(screen_width1,screen_width2)

                objects_canvas.create_line(r,c+x,w,h+x,fill = random_colour_code(),width = random_width)
                objects_canvas.create_line(r,h+x,w,c+x,fill = random_colour_code(),width = random_width)

            objects_canvas.update()
            wait(blink_rate)
            objects_canvas.delete(everything)

        for i in range(screensaver_time_cycle):

            # You can increase_decrease_screen_objects value to add more or less random rectangles on the screen output.

            for j in range(increase_decrease_screen_objects):
                random_width = randint(line_width1,line_width2)

                x = randint(screen_width1,screen_width2)

                objects_canvas.create_rectangle(
                randint(screen_width1+x,screen_width2+x),
                randint(screen_width1+x,screen_width2+x),
                randint(screen_width1+x,screen_width2+x),
                randint(screen_width1+x,screen_width2+x),
                outline = random_colour_code(),
                width = random_width)

            objects_canvas.update()
            wait(blink_rate)
            objects_canvas.delete(everything)

        for i in range(screensaver_time_cycle):

            # You can increase_decrease_screen_objects value to add more or less random ovals on the screen output.

            for j in range(increase_decrease_screen_objects):
                random_width = randint(line_width1,line_width2)

                x = randint(screen_width1,screen_width2)

                objects_canvas.create_oval(
                randint(screen_width1+x,screen_width2+x),
                randint(screen_width1+x,screen_width2+x),
                randint(screen_width1+x,screen_width2+x),
                randint(screen_width1+x,screen_width2+x),
                outline = random_colour_code(),
                width = random_width)

            objects_canvas.update()
            wait(blink_rate)
            objects_canvas.delete(everything)

        for i in range(screensaver_time_cycle):

            # You can increase_decrease_screen_objects value to add more or less random lines, random rectangles and random
            # ovals on the screen output.

            for j in range(increase_decrease_screen_objects):
                random_width = randint(line_width1,line_width2)

                x = randint(screen_width1,screen_width2)

                objects_canvas.create_line(
                randint(screen_width1+x,screen_width2+x),
                randint(screen_width1+x,screen_width2+x),
                randint(screen_width1+x,screen_width2+x),
                randint(screen_width1+x,screen_width2+x),
                fill = random_colour_code(),
                width = random_width)

                objects_canvas.create_rectangle(
                randint(screen_width1+x,screen_width2+x),
                randint(screen_width1+x,screen_width2+x),
                randint(screen_width1+x,screen_width2+x),
                randint(screen_width1+x,screen_width2+x),
                outline = random_colour_code(),
                width = random_width)

                objects_canvas.create_oval(
                randint(screen_width1+x,screen_width2+x),
                randint(screen_width1+x,screen_width2+x),
                randint(screen_width1+x,screen_width2+x),
                randint(screen_width1+x,screen_width2+x),
                outline = random_colour_code(),
                width = random_width)

            objects_canvas.update()
            wait(blink_rate)
            objects_canvas.delete(everything)

        for i in range(screensaver_time_cycle):

            # You can increase_decrease_screen_objects value to add more or less random solid rectangles on the screen output.

            for j in range(increase_decrease_screen_objects):
                random_width = randint(line_width1,line_width2)

                x = randint(screen_width1,screen_width2)

                objects_canvas.create_rectangle(
                randint(screen_width1+x,screen_width2+x),
                randint(screen_width1+x,screen_width2+x),
                randint(screen_width1+x,screen_width2+x),
                randint(screen_width1+x,screen_width2+x),
                outline = random_colour_code(),
                fill = random_colour_code(),
                width = random_width)

            objects_canvas.update()
            wait(blink_rate)
            objects_canvas.delete(everything)

        for i in range(screensaver_time_cycle):

             # You can increase_decrease_screen_objects value to add more or less random solid ovals on the screen output.

            for j in range(increase_decrease_screen_objects):
                random_width = randint(line_width1,line_width2)

                x = randint(screen_width1,screen_width2)

                objects_canvas.create_oval(
                randint(screen_width1+x,screen_width2+x),
                randint(screen_width1+x,screen_width2+x),
                randint(screen_width1+x,screen_width2+x),
                randint(screen_width1+x,screen_width2+x),
                outline = random_colour_code(),
                fill = random_colour_code(),
                width = random_width)

            objects_canvas.update()
            wait(blink_rate)
            objects_canvas.delete(everything)

        for i in range(screensaver_time_cycle):

            # You can increase_decrease_screen_objects value to add more or less random solid rectangles and random solid
            # ovals on the screen output.

            for j in range(increase_decrease_screen_objects):
                random_width = randint(line_width1,line_width2)

                x = randint(screen_width1,screen_width2)

                objects_canvas.create_rectangle(
                randint(screen_width1+x,screen_width2+x),
                randint(screen_width1+x,screen_width2+x),
                randint(screen_width1+x,screen_width2+x),
                randint(screen_width1+x,screen_width2+x),
                outline = random_colour_code(),
                fill = random_colour_code(),
                width = random_width)

                objects_canvas.create_oval(
                randint(screen_width1+x,screen_width2+x),
                randint(screen_width1+x,screen_width2+x),
                randint(screen_width1+x,screen_width2+x),
                randint(screen_width1+x,screen_width2+x),
                outline = random_colour_code(),
                fill = random_colour_code(),
                width = random_width)

            objects_canvas.update()
            wait(blink_rate)
            objects_canvas.delete(everything)
except TclError:pass

screensaver.mainloop()
