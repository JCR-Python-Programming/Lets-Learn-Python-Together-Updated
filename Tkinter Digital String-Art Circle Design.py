# Let's create a tkinter digital string-art oval design using tkinter's 'oval'
# command with a for-loop. Type and execute/run the tkinter program
# example below and see what happens.

# Created by Joseph C. Richardson, GitHub.com

from tkinter import*  # the asterisk (*) imports everything from the tkinter module

digital_string_art = Tk()  # start the tkinter function()

digital_string_art.title('Digital String Art Circle Design')

x = 1
y = 630

draw = Canvas(digital_string_art,height = y,width = y,bg = '#000000')

for i in range(x,311,15):
    draw.create_oval(x+i,x+i,y-i,y-i,width = 5,outline = '#00ffff')

draw.pack()

digital_string_art.mainloop()  # call the mainloop function()
