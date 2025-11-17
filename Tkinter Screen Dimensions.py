# Tkinter Screen Dimensions

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

screensaver.title('Tkinter Screen Dimensions')
