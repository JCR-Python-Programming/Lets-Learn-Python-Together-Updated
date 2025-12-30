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

polygons = [
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
  'Icosagon']  # index[17]

sides = [
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
  'twenty equal sides.']  # index[17]

class Polygons:
  def __init__(self,polygon,sides,colour):
    
    self.polygon = polygon
    self.sides = sides
    self.colour = colour

  def return_self(self):
    return polygons[0],sides[0],colour_name[0]

  def class_data(self):
    print(self.colour,self.polygon,'has',self.sides)  

for i in range(18):
  Polygons(polygons[i],sides[i],colour_name[0]).class_data()

print(Polygons.return_self('Agument Placeholder Value')[2])

print(Polygons.return_self('Agument Placeholder Value')[0])

print(Polygons.return_self('Agument Placeholder Value')[1])
