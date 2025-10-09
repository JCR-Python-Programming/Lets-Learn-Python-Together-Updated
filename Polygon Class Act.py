# Let's create a really fun class act with polygon shapes, number of sides and colour attribute
# properties. Save the Python file as 'Polygon Class act.py'. Next, double-click the Python
# file to see all the cool coloured text effects.

text_col = (
  '\x1b[31m',  # index 0 = red
  '\x1b[32m',  # index 1 = green
  '\x1b[33m',  # index 2 = yellow
  '\x1b[34m',  # index 3 = blue
  '\x1b[35m',  # index 4 = purple
  '\x1b[36m',  # index 5 = cyan
  '\x1b[37m')  # index 6 = white

colour_name = (
  'A red',  # index 0 = red
  'A green',  # index 1 = green
  'A Yellow',  # index 2 = yellow
  'A blue',  # index 3 = blue
  'A purple',  # index 4 = purple
  'A cyan',  # index 5 = cyan
  'A white')  # index 6 = white

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
  'three equal sides.',  # index[0]
  'four equal sides.',  # index[1]
  'five equal sides.',  # index[2]
  'six equal sides.',  # index[3]
  'seven equal sides.',  # index[4]
  'eight equal sides.',  # index[5]
  'nine equal sides.',  # index[6]
  'ten equal sides.',  # index[7]
  'eleven equal sides.',  # index[8]
  'twelve equal sides.',  # index[9]
  'thirteen equal sides.',  # index[10]
  'fourteen equal sides.',  # index[11]
  'fifteen equal sides.',  # index[12]
  'sixteen equal sides.',  # index[13]
  'seventeen equal sides.',  # index[14]
  'eighteen equal sides.',  # index[15]
  'nineteen equal sides.',  # index[16]
  'twenty equal sides.')  # index[17]

class Polygons:
  def __init__(self,polygon,sides,colour):
    self.polygon = polygon
    self.sides = sides
    self.colour = colour

polygons = (
  Polygons(text_col[0]+polygons[0],text_col[0]+sides[0],text_col[0]+colour_name[0]),
  Polygons(text_col[1]+polygons[1],text_col[1]+sides[1],text_col[1]+colour_name[1]),
  Polygons(text_col[2]+polygons[2],text_col[2]+sides[2],text_col[2]+colour_name[2]),
  Polygons(text_col[3]+polygons[3],text_col[3]+sides[3],text_col[3]+colour_name[3]),
  Polygons(text_col[4]+polygons[4],text_col[4]+sides[4],text_col[4]+colour_name[4]),
  Polygons(text_col[5]+polygons[5],text_col[5]+sides[5],text_col[5]+colour_name[5]),
  Polygons(text_col[6]+polygons[6],text_col[6]+sides[6],text_col[6]+colour_name[6]),
  Polygons(text_col[0]+polygons[7],text_col[0]+sides[7],text_col[0]+colour_name[0]),
  Polygons(text_col[1]+polygons[8],text_col[1]+sides[8],text_col[1]+colour_name[1]),
  Polygons(text_col[2]+polygons[9],text_col[2]+sides[9],text_col[2]+colour_name[2]),
  Polygons(text_col[3]+polygons[10],text_col[3]+sides[10],text_col[3]+colour_name[3]),
  Polygons(text_col[4]+polygons[11],text_col[4]+sides[11],text_col[4]+colour_name[4]),
  Polygons(text_col[5]+polygons[12],text_col[5]+sides[12],text_col[5]+colour_name[5]),
  Polygons(text_col[6]+polygons[13],text_col[6]+sides[13],text_col[6]+colour_name[6]),
  Polygons(text_col[0]+polygons[14],text_col[0]+sides[14],text_col[0]+colour_name[0]),
  Polygons(text_col[1]+polygons[15],text_col[1]+sides[15],text_col[1]+colour_name[1]),
  Polygons(text_col[2]+polygons[16],text_col[2]+sides[16],text_col[2]+colour_name[2]),
  Polygons(text_col[3]+polygons[17],text_col[3]+sides[17],text_col[3]+colour_name[3]))

for i in polygons:print(f'{i.colour} {i.polygon} has {i.sides}')  # new f' string format

# Try these different formatting string examples below:

for i in polygons:print(i.colour,i.polygon,'has',i.sides)  # non formatted string

for i in polygons:print(i.colour,i.polygon+' has '+i.sides)  # non formatted string

for i in polygons:print(f'{i.colour} {i.polygon} has '+i.sides)  # new f' string format mix with non formatted string

for i in polygons:print('{} {} has {}'.format(i.colour, i.polygon,i.sides))  # old formatted string

input('\nPress Enter to exit:')

# I am almost a complete Walking Human Computer Science Research
# Laboratory Machine on Two Legs... 😁
