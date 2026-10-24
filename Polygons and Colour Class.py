
# Type and execute/run these Polygon class program examples:

# Save this Python file as Polygon class.py. Note: double click
# the Python file to view all its cool colour text.

# Created by Joseph C. Richardson, GitHub.com

RGB = (
  '\033[38;2;255;0;0m',  # index 0 = red
  '\033[38;2;255;255;0m',  # index 1 = yellow
  '\033[38;2;0;0;255m',  # index 2 = blue
  '\033[38;2;0;255;0m',  # index 3 = green
  '\033[38;2;255;0;255m',  # index 4 = pink
  '\033[38;2;0;255;255m',  # index 5 = cyan
  '\033[38;2;255;255;255m')  # index 6 = white

colour_name = (
  RGB[0]+'A red',  # index 0 = colour name red
  RGB[1]+'A yellow',  # index 1 = colour name yellow
  RGB[2]+'A blue',  # index 2 = colour name blue
  RGB[3]+'A green',  # index 3 = colour name green
  RGB[4]+'A pink',  # index 4 = colour name pink
  RGB[5]+'A cyan',  # index 5 = colour name cyan
  RGB[6]+'A white')  # index 6 = colour name white

polygons = (
  'Triangle',  # index[0]
  'Square',  # index[1]
  'Pentagon',  # index[2]
  'Hexagon',  # index[3]
  'Heptagon',  # index[4]
  'Octagon',  # index[5]
  'Nonagon',  # index[6]
  'Decagon',  # index[7]
  'Hendecagon',  # index[8]
  'Dodecagon',  # index[9]
  'Tridecagon',  # index[10]
  'Tetradecagon',  # index[11]
  'Pentadecagon',  # index[12]
  'Hexadecagon',  # index[13]
  'Heptadecagon',  # index[14]
  'Octadecagon',  # index[15]
  'Enneadecagon',  # index[16]
  'Icosagon')  # index[17]

sides = (
  'has three equal sides.',  # index[0]
  'has four equal sides.',  # index[1]
  'has five equal sides.',  # index[2]
  'has six equal sides.',  # index[3]
  'has seven equal sides.',  # index[4]
  'has eight equal sides.',  # index[5]
  'has nine equal sides.',  # index[6]
  'has ten equal sides.',  # index[7]
  'has eleven equal sides.',  # index[8]
  'has twelve equal sides.',  # index[9]
  'has thirteen equal sides.',  # index[10]
  'has fourteen equal sides.',  # index[11]
  'has fifteen equal sides.',  # index[12]
  'has sixteen equal sides.',  # index[13]
  'has seventeen equal sides.',  # index[14]
  'has eighteen equal sides.',  # index[15]
  'has nineteen equal sides.',  # index[16]
  'has twenty equal sides.')  # index[17]

# Note: tuples and lists always start at index[0].

# Invoke the len() function to check how many values there are
# in tuples and lists alike.

# Invoke the backslash \ for hard returns to keep your code lines from
# skating across the screen out of view.

index_length =\
             len(RGB),len(colour_name),len(polygons),len(sides)  # default tuple

print(index_length[0],index_length[1],index_length[2])

# Let's learn what __slots__ do! Slots reserve exact memory
# for class attributes. You don't need a huge, empty warehouse
# just to store a few attributes. Slots optimize memory and performance.
# Research Python __slots__ to learn more about them. Two double
# underscores __ __ are required to create __slots__. Simply
# press and hold down the shift key, while pressing the minus key.

# Note: when invoking __slots__ with only one attribute, you must
# place a comma ',' at the end of the slot's single attribute, as not
# to confuse it as a tuple value at execution/run time.

class Polygon:

# Let's learn what 'documentation strings' do with classes. In Python,
# we call these 'doctrings'. We  need to invoke three double quote
# marks """ on each side of the docstring title: """My Polygon Class""".
# The getattr() function simply means the word: 'get attribute'. With
# docstrings, we can see the documentation payload/description
# block of the class at execution/run time. Docstrings are like a
# comment; they descibe what the class is about at execution/run
# time.

  """My Polygon Class"""  # documentation payload/description block

  __slots__ = ('colour','polygon','sides')  # __slots__ optimizes memory and performance

  def __init__(self,colour,polygon,sides):

    self.colour = colour
    self.polygon = polygon
    self.sides = sides

  def return_colour(self):

    return self.colour

  def return_polygon(self):

    return self.polygon

  def return_sides(self):

    return self.sides

# These class instances display all attribute property values on
# the screen at execution/run time. Here are three ways, we can
# create class instances. For example:

# Retrieve attribute property values directly from its class.

print(getattr(Polygon,'__doc__'))  # docstring: Polygon

print(Polygon(colour_name[0],polygons[0],sides[0]).colour)

print(Polygon(colour_name[0],polygons[0],sides[0]).polygon)

print(Polygon(colour_name[0],polygons[0],sides[0]).sides)


print(getattr(Polygon,'__doc__'))  # docstring: Polygon

print(Polygon(colour_name[1],polygons[1],sides[1]).colour)

print(Polygon(colour_name[1],polygons[1],sides[1]).polygon)

print(Polygon(colour_name[1],polygons[1],sides[1]).sides)

input('\nPress Enter to exit Command Prompt:')

# The getattr('get attribute') lookup, looks up valid attributes.
# Think of 'getattr' as the attribute gatekeeper. If an attribute
# does not exist, or is floating, bleeding into other class attributes,
# the gatekeeper, 'getattr' looks up exact attributes with their
# class only. The fallback, 'Attribute Not Found' text prevents
# program crashes from occurring, should a wrong attribute or
# name error happen.

print(getattr(Polygon,'__doc__'))  # docstring: Polygon

print(getattr(Polygon(colour_name[0],polygons[0],sides[0]),'colour','Attribute Not Found:'))  # getattr('get attribute') lookup

print(getattr(Polygon(colour_name[0],polygons[0],sides[0]),'polygon','Attribute Not Found:'))  # getattr('get attribute') lookup

print(getattr(Polygon(colour_name[0],polygons[0],sides[0]),'sides','Attribute Not Found:'))  # getattr('get attribute') lookup


print(getattr(Polygon,'__doc__'))  # docstring: Polygon

print(getattr(Polygon(colour_name[1],polygons[1],sides[1]),'colour','Attribute Not Found:'))  # getattr('get attribute') lookup

print(getattr(Polygon(colour_name[1],polygons[1],sides[1]),'polygon','Attribute Not Found:'))  # getattr('get attribute') lookup

print(getattr(Polygon(colour_name[1],polygons[1],sides[1]),'sides','Attribute Not Found:'))  # getattr('get attribute') lookup

input('\nPress Enter to exit Command Prompt:')

# There are three define, def functions() inside the Polygon class.
# These three def functions() return attribute values within these class
# instances below. The 'self' is a callback to itself, hence the word
# 'self'. The 'self' contains the returned attribute value into the return
# method.

print(getattr(Polygon,'__doc__'))  # docstring: Polygon

print(Polygon(colour_name[0],polygons[0],sides[0]).return_colour())  # return attribute values

print(Polygon(colour_name[0],polygons[0],sides[0]).return_polygon())  # return attribute values

print(Polygon(colour_name[0],polygons[0],sides[0]).return_sides())  # return attribute values


print(getattr(Polygon,'__doc__'))  # docstring: Polygon

print(Polygon(colour_name[1],polygons[1],sides[1]).return_colour())  # return attribute values

print(Polygon(colour_name[1],polygons[1],sides[1]).return_polygon())  # return attribute values

print(Polygon(colour_name[1],polygons[1],sides[1]).return_sides())  # return attribute values

input('\nPress Enter to exit Command Prompt:')

# Let's see what for loops do with these class instance print() functions.
# And always remember to stay DRY!: Don't Repeat Yourself!

# Note: we can invoke two single or twp double quote marks
# if we like. However, the 'None' constant is far easier to
# spot in your Python code.

# Polygon('',polygons[j],'').polygon

# Polygon("",polygons[j],"").polygon

# Polygon(None,polygons[j],None).polygon

print(getattr(Polygon,'__doc__'))  # docstring: Polygon

for i in range(7):
  print(
    Polygon(colour_name[i],None,None).colour,
    Polygon(None,polygons[i],None).polygon,
    Polygon(None,None,sides[i]).sides)

input('\nPress Enter to exit Command Prompt:')

# screen output:
'''
My Polygon Class
A red Triangle has three equal sides.
A yellow Square has four equal sides.
A blue Pentagon has five equal sides.
A green Hexagon has six equal sides.
A pink Heptagon has seven equal sides.
A cyan Octagon has eight equal sides.
A white Nonagon has nine equal sides.
'''

print(getattr(Polygon,'__doc__'))  # docstring: Polygon

for i in range(7):
  print(
    getattr(Polygon(colour_name[i],None,None),'colour','Attribute Not Found:'),
    getattr(Polygon(None,polygons[i],None),'polygon','Attribute Not Found:'),
    getattr(Polygon(None,None,sides[i]),'sides','Attribute Not Found:'))

input('\nPress Enter to exit Command Prompt:')

# screen output:
'''
My Polygon Class
A red Triangle has three equal sides.
A yellow Square has four equal sides.
A blue Pentagon has five equal sides.
A green Hexagon has six equal sides.
A pink Heptagon has seven equal sides.
A cyan Octagon has eight equal sides.
A white Nonagon has nine equal sides.
'''

print(getattr(Polygon,'__doc__'))  # docstring: Polygon

for i in range(7):
  print(
    Polygon(colour_name[i],None,None).return_colour(),
    Polygon(None,polygons[i],None).return_polygon(),
    Polygon(None,None,sides[i]).return_sides())

input('\nPress Enter to exit Command Prompt:')

# screen output:
'''
My Polygon Class
A red Triangle has three equal sides.
A yellow Square has four equal sides.
A blue Pentagon has five equal sides.
A green Hexagon has six equal sides.
A pink Heptagon has seven equal sides.
A cyan Octagon has eight equal sides.
A white Nonagon has nine equal sides.
'''

print(getattr(Polygon,'__doc__'))  # docstring: Polygon

# Let's create some nested for loops.

for i in range(7):  # colour_name has seven colour values only
  print(
    Polygon(colour_name[i],None,None).colour)
  for j in range(18):  # polygons has eighteen polygon values only
    print(
      Polygon(None,polygons[j],None).polygon,
      Polygon(None,None,sides[j]).sides)

input('\nPress Enter to exit Command Prompt:')


print(getattr(Polygon,'__doc__'))  # docstring: Polygon

for i in range(7):
  print(
    getattr(Polygon(colour_name[i],None,None),'colour','Attribute Not Found:'))
  for j in range(18):
    print(
      getattr(Polygon(None,polygons[j],None),'polygon','Attribute Not Found:'),
      getattr(Polygon(None,None,sides[j]),'sides','Attribute Not Found:'))

input('\nPress Enter to exit Command Prompt:')


print(getattr(Polygon,'__doc__'))  # docstring: Polygon

for i in range(7):
  print(
    Polygon(colour_name[i],None,None).return_colour())
  for j in range(18):
    print(
      Polygon(None,polygons[j],None).return_polygon(),
      Polygon(None,None,sides[j]).return_sides())

input('\nPress Enter to exit Command Prompt:')

# Let's have some fun now. Let's use our tuples to create an actual,
# logical program out of our Polygon class with logical 'if' and 'elif'
# conditions.

user_input1 = input(
  '''
Choose a colour for your polygon.
Red = 1, Yellow = 2, Blue = 3, Green = 4, Pink = 5, Cyan = 6, White = 7:
''')

if user_input1 == '1':
  print(Polygon(RGB[0],None,None).colour)  # Red

elif user_input1 == '2':
   print(Polygon(RGB[1],None,None).colour)  # Yellow

elif user_input1 == '3':
   print(Polygon(RGB[2],None,None).colour)  # Blue

elif user_input1 == '4':
   print(Polygon(RGB[3],None,None).colour)  # Green

elif user_input1 == '5':
   print(Polygon(RGB[4],None,None).colour)  # Pink

elif user_input1 == '6':
   print(Polygon(RGB[5],None,None).colour)  # Cyan

elif user_input1 == '7':
   print(Polygon(RGB[6],None,None).colour)  # White

user_input2 = input(
    '''
Choose a polygon.
Triangle = 1, Square = 2, Pentagon = 3, Hexagon = 4, Heptagon = 5
Octagon = 6, Nonagon = 7, Decagon = 8, Hendecagon = 9, Dodecagon = 10
Tridecagon = 11, Tetradecagon = 12, Pentadecagon = 13, Hexadecagon = 14
Heptadecagon = 15, Octadecagon = 16, Enneadecagon = 17, Icosagon = 18
''')

if user_input2 == '1':
  print(Polygon(None,polygons[0],None).polygon)  # Triangle

elif user_input2 == '2':
   print(Polygon(None,polygons[1],None).polygon)  # Square

elif user_input2 == '3':
   print(Polygon(None,polygons[2],None).polygon)  # Pentagon

elif user_input2 == '4':
   print(Polygon(None,polygons[3],None).polygon)  # Hexagon

elif user_input2 == '5':
   print(Polygon(None,polygons[4],None).polygon)  # Heptagon

elif user_input2 == '6':
   print(Polygon(None,polygons[5],None).polygon)  # Octagon

elif user_input2 == '7':
   print(Polygon(None,polygons[6],None).polygon)  # Nonagon

elif user_input2 == '8':
   print(Polygon(None,polygons[7],None).polygon)  # Decagon

elif user_input2 == '9':
   print(Polygon(None,polygons[8],None).polygon)  # Hendecagon

elif user_input2 == '10':
   print(Polygon(None,polygons[9],None).polygon)  # Dodecagon

elif user_input2 == '11':
   print(Polygon(None,polygons[10],None).polygon)  # Tridecagon

elif user_input2 == '12':
   print(Polygon(None,polygons[11],None).polygon)  # Tetradecagon

elif user_input2 == '13':
   print(Polygon(None,polygons[12],None).polygon)  # Pentadecagon

elif user_input2 == '14':
   print(Polygon(None,polygons[13],None).polygon)  # Hexadecagon

elif user_input2 == '15':
   print(Polygon(None,polygons[14],None).polygon)  # Heptadecagon

elif user_input2 == '16':
   print(Polygon(None,polygons[15],None).polygon)  # Octadecagon

elif user_input2 == '17':
   print(Polygon(None,polygons[16],None).polygon)  # Enneadecagon

elif user_input2 == '18':
   print(Polygon(None,polygons[17],None).polygon)  # Icosagon

input('\nPress Enter to exit Command Prompt:')

# I am almost a complete Walking Human Computer Science Research Laboratory Machine on Two Legs... 😁
