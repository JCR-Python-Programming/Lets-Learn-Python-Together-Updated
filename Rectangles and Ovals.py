#  Rectangles and Ovals Python program example using variables

# Created by Joseph C. Richardson, GitHub.com

from time import sleep as wait
from random import*
from tkinter import*
rectangles_and_ovals = Tk()

rectangles_and_ovals.title('Rectangles and Ovals')
everything = 'all'

def random_colour_code():
    hex_chars = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    colour_code = '#'

    for i in range(0,6):
        colour_code = colour_code+choice(hex_chars)
    return colour_code

colour = '#000000'
w,h = 1920,1080
r,c = 0,0
rand1,rand2 = 0,15
randint1,randint2 = -1920,1920
loop = 20
seconds = .08

shapes_canvas = Canvas(rectangles_and_ovals,width = w,height = h,background = colour)
shapes_canvas.grid(row = r,column = c)

while True:

    for i in range(loop): # increse the for loop value to add more rectangles and ovals on the screen output
        random_width = randint(rand1,rand2)
        x = randint(randint1,randint2)
        shapes_canvas.create_rectangle(
            randint(randint1+x,randint2+x),
            randint(randint1+x,randint2+x),
            randint(randint1+x,randint2+x),
            randint(randint1+x,randint2+x),
            fill=random_colour_code(),
            width = random_width)
        shapes_canvas.create_oval(
            randint(randint1+x,randint2+x),
            randint(randint1+x,randint2+x),
            randint(randint1+x,randint2+x),
            randint(randint1+x,randint2+x),
            fill=random_colour_code(),
            width = random_width)

    shapes_canvas.update()
    wait(seconds)
    shapes_canvas.delete(everything)

rectangles_and_ovals.mainloop()
