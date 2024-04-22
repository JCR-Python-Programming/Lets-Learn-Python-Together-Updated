import math
from tkinter import*
root=Tk()

root.title('cs & ppe'.upper())
trademark=PhotoImage(file='Binary Photo.png')
root.iconphoto(True,trademark)
window_size='230x520'
window_colour='#ff00ff'
font_style='Arial bold'
font_size=25
font_size_custom=16
digit=0,1,2,3,4,5,6,7,8,9,'%','.','/','*','-','+','=','c','BIN','HEX','OCT','DEC'
text_print='programmer functions'.upper()

black='#000000'
grey='#dddddd'
white='#ffffff'
red='#ff0000'
yellow='#fff000'
blue='#000fff'
green='#00ff00'
pink='#ff00ff'
dark_pink='#af00af'
cyan = '#00ffff'

root.geometry(window_size)
root.configure(bg=window_colour)
root.resizable(width=False,height=False)

entry=Entry(root,font=(font_style,font_size),
            bg=grey,fg=red,width=11,bd=15).place(x=0,y=0)

def button_click(number):
    current=entry.get()
    entry.delete(0,END)
    entry.insert(0,str(current)+str(number))

def button_clear():
    entry.delete(0,END)

def button_add():
    first_number=entry.get()
    global f_num
    global math
    math='addition'
    f_num=int(first_number)
    entry.delete(0,END)

def button_subtract():
    first_number=entry.get()
    global f_num
    global math
    math='subtraction'
    f_num=int(first_number)
    entry.delete(0,END)

def button_multiply():
    first_number=entry.get()
    global f_num
    global math
    math='multiplication'
    f_num=int(first_number)
    entry.delete(0,END)
    
def button_divide():
    first_number=entry.get()
    global f_num
    global math
    math='division'
    f_num=int(first_number)
    entry.delete(0,END)

def button_equal():
    second_number=entry.get()
    entry.delete(0,END)
    if math=='addition':
        entry.insert(0,f_num+int(second_number))

    elif math=='subtraction':
        entry.insert(0,f_num-int(second_number))

    elif math=='multiplication':
        entry.insert(0,f_num*int(second_number))

    elif math=='division':
        entry.insert(0,f_num/int(second_number))

label = Label(root,text=text_print,font=(font_style,12),fg=cyan,bg=pink)
label.place(x=4,y=366)

b0=Button(root,font=(font_style,font_size)
          ,anchor=CENTER,
          bg=cyan,
          fg=dark_pink,
          activeforeground=cyan,
          activebackground=dark_pink,
          width=10,
          bd=5,
          text=digit[16]).place(x=8,y=439)

b1=Button(root,font=(font_style,font_size_custom),
          anchor=CENTER,
          bg=cyan,
          fg=dark_pink,
          activeforeground=cyan,
          activebackground=dark_pink,
          width=3,
          bd=5,
          text=digit[18]).place(x=6,y=391)

b2=Button(root,font=(font_style,font_size_custom),
          anchor=CENTER,
          bg=cyan,
          fg=dark_pink,
          activeforeground=cyan,
          activebackground=dark_pink,
          width=3,
          bd=5,
          text=digit[19]).place(x=61,y=391)

b3=Button(root,font=(font_style,font_size_custom)
          ,anchor=CENTER,
          bg=cyan,
          fg=dark_pink,
          activeforeground=cyan,
          activebackground=dark_pink,
          width=3,
          bd=5,
          text=digit[20]).place(x=116,y=391)

b4=Button(root,font=(font_style,font_size_custom),
          anchor=CENTER,
          bg=cyan,
          fg=dark_pink,
          activeforeground=cyan,
          activebackground=dark_pink,
          width=3,
          bd=5,
          text=digit[21]).place(x=171,y=391)

b5=Button(root,font=(font_style,font_size),
          anchor=CENTER,
          bg=cyan,
          fg=dark_pink,
          activeforeground=cyan,
          activebackground=dark_pink,
          width=2,
          bd=5,
          text=digit[11]).place(x=4,y=293)

b6=Button(root,font=(font_style,font_size),
          anchor=CENTER,
          bg=cyan,
          fg=dark_pink,
          activeforeground=cyan,
          activebackground=dark_pink,
          width=2,
          bd=5,
          text=digit[0]).place(x=60,y=293)

b7=Button(root,font=(font_style,font_size),
          anchor=CENTER,
          bg=cyan,
          fg=dark_pink,
          activeforeground=cyan,
          activebackground=dark_pink,
          width=2,
          bd=5,
          text=digit[17]).place(x=116,y=293)

b8=Button(root,font=(font_style,font_size),
          anchor=CENTER,
          bg=cyan,
          fg=dark_pink,
          activeforeground=cyan,
          activebackground=dark_pink,
          width=2,
          bd=5,
          text=digit[15]).place(x=172,y=293)

b9=Button(root,font=(font_style,font_size),
          anchor=CENTER,
          bg=cyan,
          fg=dark_pink,
          activeforeground=cyan,
          activebackground=dark_pink,
          width=2,
          bd=5,
          text=digit[1]).place(x=4,y=220)

b10=Button(root,font=(font_style,font_size),
          anchor=CENTER,
          bg=cyan,
          fg=dark_pink,
          activeforeground=cyan,
          activebackground=dark_pink,
          width=2,
          bd=5,
          text=digit[2]).place(x=60,y=220)

b11=Button(root,font=(font_style,font_size),
           anchor=CENTER,
           bg=cyan,
           fg=dark_pink,
           activeforeground=cyan,
           activebackground=dark_pink,
           width=2,
           bd=5,
           text=digit[3]).place(x=116,y=220)

b12=Button(root,font=(font_style,font_size),
           anchor=CENTER,
           bg=cyan,
           fg=dark_pink,
           activeforeground=cyan,
           activebackground=dark_pink,
           width=2,
           bd=5,
           text=digit[14]).place(x=172,y=220)

b13=Button(root,font=(font_style,font_size),
           anchor=CENTER,
           bg=cyan,
           fg=dark_pink,
           activeforeground=cyan,
           activebackground=dark_pink,
           width=2,
           bd=5,
           text=digit[4]).place(x=4,y=147)

b14=Button(root,font=(font_style,font_size),
           anchor=CENTER,
           bg=cyan,
           fg=dark_pink,
           activeforeground=cyan,
           activebackground=dark_pink,
           width=2,
           bd=5,
           text=digit[5]).place(x=60,y=147)

b15=Button(root,font=(font_style,font_size),
           anchor=CENTER,
           bg=cyan,
           fg=dark_pink,
           activeforeground=cyan,
           activebackground=dark_pink,
           width=2,
           bd=5,
           text=digit[6]).place(x=116,y=147)

b16=Button(root,font=(font_style,font_size),
           anchor=CENTER,
           bg=cyan,
           fg=dark_pink,
           activeforeground=cyan,
           activebackground=dark_pink,
           width=2,
           bd=5,
           text=digit[13]).place(x=172,y=147)

b17=Button(root,font=(font_style,font_size),
           anchor=CENTER,
           bg=cyan,
           fg=dark_pink,
           activeforeground=cyan,
           activebackground=dark_pink,
           width=2,
           bd=5,
           text=digit[7]).place(x=4,y=74)

b18=Button(root,font=(font_style,font_size),
           anchor=CENTER,
           bg=cyan,
           fg=dark_pink,
           activeforeground=cyan,
           activebackground=dark_pink,
           width=2,
           bd=5,
           text=digit[8]).place(x=60,y=74)

b19=Button(root,font=(font_style,font_size),
           anchor=CENTER,
           bg=cyan,
           fg=dark_pink,
           activeforeground=cyan,
           activebackground=dark_pink,
           width=2,
           bd=5,
           text=digit[9]).place(x=116,y=74)

b20=Button(root,font=(font_style,font_size),
           anchor=CENTER,
           bg=cyan,
           fg=dark_pink,
           activeforeground=cyan,
           activebackground=dark_pink,
           width=2,
           bd=5,
           text=digit[12]).place(x=172,y=74)

root.mainloop()
