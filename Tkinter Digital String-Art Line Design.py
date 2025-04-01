# Let's create a tkinter digital string-art line design using a for-loop.Type
# and execute/run the tkinter program example below and see what happens.

# Created by Joseph C. Richardson, GitHub.com

from tkinter import*  # the asterisk (*) imports everything from the tkinter module

digital_string_art = Tk()  # start the tkinter function()

digital_string_art.title('Digital String Art Line Design')

x = 0
y = 630

draw = Canvas(digital_string_art,height = y,width = y,bg = '#000000')

for i in range(x,628,3):
    draw.create_line(x+i,x+i ,y,x,y,x,y,y,y,y,y,y,y,y,x,y,x+i,x+i,fill = '#00ffff')

draw.pack()

digital_string_art.mainloop()  # call the mainloop function()
