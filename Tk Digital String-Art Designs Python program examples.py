# Tk Digital String-Art Designs Python program examples:

# Created by Joseph C. Richardson, GitHub.com

# Let's create a tkinter digital string-art rectangle design using tkinter's
# 'rectangle' command with a for-loop. Type and execute/run the tkinter
# program example below and see what happens.

# Created by Joseph C. Richardson, GitHub.com

from tkinter import*  # the asterisk (*) imports everything from the tkinter module

digital_string_art = Tk()  # start the tkinter function()

digital_string_art.title('Digital String Art Rectangle Design')

x = 1
y = 630

draw = Canvas(digital_string_art,height = y,width = y,bg = '#000000')

for i in range(x,311,15):
    draw.create_rectangle(x+i,x+i,y-i,y-i,width = 5,outline = '#00ffff')

draw.pack()

digital_string_art.mainloop()  # call the mainloop function()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create a tkinter digital string-art oval design using tkinter's 'oval'
# command with a for-loop. Type and execute/run the tkinter program
# example below and see what happens.

# Created by Joseph C. Richardson, GitHub.com

from tkinter import*  # the asterisk (*) imports everything from the tkinter module

digital_string_art = Tk()  # start the tkinter function()

digital_string_art.title('Digital String Art Oval Design')

x = 1
y = 630

draw = Canvas(digital_string_art,height = y,width = y,bg = '#000000')

for i in range(x,311,15):
    draw.create_oval(x+i,x+i,y-i,y-i,width = 5,outline = '#00ffff')

draw.pack()

digital_string_art.mainloop()  # call the mainloop function()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create a tkinter digital string-art line design using a for-loop. Type
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

# I am almost a complete Walking Human Computer Science Research
# Laboratory Machine on Two Legs... 😁
