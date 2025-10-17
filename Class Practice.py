polygon = (
  'triangle','square','pentagon','hexagon','heptagon',
  'octagon','nonagon','decagon','hendecagon','dodecagon',
  'tridecagon','tetradecagon', 'pentadecagon','hexadecagon',
  'heptadecagon','octadecagon','enneadecagon','icosagon')  # tuple( ) array

sides = 3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20  # default tuple array

colour = [
  'red','yellow','blue','green','pink','cyan','white'
  ,'black','brown', 'orange','purple','gray','silver',
  'gold','maroon','indigo','lavender','violet']  # list[ ] array

colour.sort()  # sort the polygon_colour list in alphabetical order

material = 'paper','plastic','wood','metal','glass'  # tuple( ) array

class Polygons:

  def __init__(self,polygon,sides,colour):

    self.polygon = polygon
    self.sides = sides
    self.colour = colour

  def polygon_name():
      return polygon

  def polygon_sides():
      return sides

  def polygon_colour():
      return colour

  def polygon_sides_colour_no_argument():
      return polygon,sides,colour

  def polygon_sides_colour_with_argument(self):
      return self.polygon,self.sides,self.colour

class Super_sub_same_attributes(Polygons):

  def __init__(self,polygon,sides,colour):
    super().__init__(polygon,sides,colour)

class Super_sub_extra_attribute(Polygons):

  def __init__(self,polygon,sides,colour,material):
    super().__init__(polygon,sides,colour)

    self.material = material

class Child_class_all(Super_sub_extra_attribute,Super_sub_same_attributes,Polygons):
  pass

# Class values:

print(Polygons(polygon,sides,colour).polygon[0])

print(Polygons(polygon,sides,colour).sides[0])

print(Polygons(polygon,sides,colour).colour[0])

# Define function returned class values:

print(Polygons.polygon_name()[0])

print(Polygons.polygon_sides()[0])

print(Polygons.polygon_colour()[0])

# Define function returned no argument class value:

print(Polygons.polygon_sides_colour_no_argument()[0][0])

# Define function returned with argument class value:

print(Polygons(polygon,sides,colour).polygon_sides_colour_with_argument()[0][0])

# Super clas and super sub class values:

print(Super_sub_same_attributes(polygon,sides,colour).polygon[0])

print(Super_sub_extra_attribute(polygon,sides,colour,material).polygon[0])

# Child class values:

print(Child_class_all(polygon,sides,colour,material).polygon[0])

print(Child_class_all(polygon,sides,colour,material).sides[0])

print(Child_class_all(polygon,sides,colour,material).colour[0])

print(Child_class_all(polygon,sides,colour,material).material[0])
