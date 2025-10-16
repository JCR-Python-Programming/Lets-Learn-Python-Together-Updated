polygon = (
  'triangle','square','pentagon','hexagon','heptagon',
  'octagon','nonagon','decagon','hendecagon','dodecagon',
  'tridecagon','tetradecagon', 'pentadecagon','hexadecagon',
  'heptadecagon','octadecagon','enneadecagon','icosagon')  # tuple( ) array

num_sides = 3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20  # default tuple array

colour = [
  'red','yellow','blue','green','pink','cyan','white'
  ,'black','brown', 'orange','purple','gray','silver',
  'gold','maroon','indigo','lavender','violet']  # list[ ] array

shape_material = 'paper','plastic','wood','metal','glass'  # tuple( ) array

colour.sort()  # sort the shape_colour list in alphabetical order

class Polygons:

  def __init__(self,polygon,sides,colour):

    self.polygon = polygon
    self.sides = sides
    self.colour = colour

  def shape_name():
      return polygon

  def shape_num_sides():
      return num_sides

  def shape_colour():
      return colour

  def shape_sides_colour():
      return polygon,num_sides,colour

class Super_sub_same(Polygons):

  def __init__(self,polygon,sides,colour):
    super().__init__(polygon,sides,colour)

class Super_sub_different(Polygons):

  def __init__(self,polygon,sides,colour,material):
    super().__init__(polygon,sides,colour)

    self.material = material

# Class values:

print(Polygons(polygon,num_sides,colour).sides[0])

print(Polygons(polygon,num_sides,colour).colour[0])

# Define function returned class values:

print(Polygons.shape_name()[0])

print(Polygons.shape_num_sides()[0])

print(Polygons.shape_colour()[0])

print(Polygons.shape_sides_colour()[0][0])

# Super sub class values:

print(Super_sub_same(polygon,num_sides,colour).sides[0])

print(Super_sub_different(polygon,num_sides,colour,shape_material).material[0])
