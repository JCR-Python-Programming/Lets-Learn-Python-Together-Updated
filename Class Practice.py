def find_equal_text():
  if 'text' == 'text':
    return True
  else:
    return False

print(find_equal_text())

def find_in_text():
  if 'x' in 'text':
    return True
  else:
    return False

print(find_in_text())

def find_not_in_text():
  if 'c' not in 'text':
    return True
  else:
    return False

print(find_not_in_text())

def num_logic():
  if 1 == 1:
    return True
  else:
    return False

print(num_logic())
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
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

  def Child_class_return_value():
    return 'Yay! We did it!!'

  def Child_class_return_addition(num1,num2):
    return num1 + num2

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

# Define function returned child class value:

print(Child_class_all.Child_class_return_value())

# Define function returned arguments child class values:

print(Child_class_all.Child_class_return_addition(2,3))  # 2 + 3 = 5
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Math_class:

  def __init__(self,addition,subtraction,multiplication,division,exponent):

    self.addition = addition
    self.subtraction = subtraction
    self.multiplication = multiplication
    self.division = division
    self.exponent = exponent

  def addition(num1,num2):
      return num1 + num2

  def subtraction(num1,num2):
      return num1 - num2

  def multiplication(num1,num2):
      return num1 * num2

  def division(num1,num2):
      return num1 / num2

  def exponent(num1,num2):
      return num1 ** num2

class Super_sub_same_attributes(Math_class):

  def __init__(self,addition,subtraction,multiplication,division,exponent):
    super().__init__(addition,subtraction,multiplication,division,exponent)

class Super_sub_extra_attribute(Math_class):

  def __init__(self,addition,subtraction,multiplication,division,exponent,professor):
    super().__init__(addition,subtraction,multiplication,division,exponent)

    self.professor = professor

professors = 'Galileo Galilei','Isaac Newton','Albert Einstein','Stephen Hawking'

a,b = 8,2

# Define function returned class with two argument values:

print(Math_class.addition(a,b))

print(Math_class.subtraction(a,b))

print(Math_class.multiplication(a,b))

print(int(Math_class.division(a,b)))

print(Math_class.exponent(a,b))

# Super sub one class with two argument values:

print(Super_sub_same_attributes.addition(a,b))

print(Super_sub_same_attributes.subtraction(a,b))

print(Super_sub_same_attributes.multiplication(a,b))

print(int(Super_sub_same_attributes.division(a,b)))

print(Super_sub_same_attributes.exponent(a,b))

# Super sub two class with two argument values:

print(Super_sub_extra_attribute.addition(a,b))

print(Super_sub_extra_attribute.subtraction(a,b))

print(Super_sub_extra_attribute.multiplication(a,b))

print(int(Super_sub_extra_attribute.division(a,b)))

print(Super_sub_extra_attribute.exponent(a,b))

print(Super_sub_extra_attribute(a+b,a-b,a*b,a/b,a**b,professors).professor[0])

# Class values:

print(Math_class(a+b,a-b,a*b,a/b,a**b).addition)

print(Math_class(a+b,a-b,a*b,a/b,a**b).subtraction)

print(Math_class(a+b,a-b,a*b,a/b,a**b).multiplication)

print(int(Math_class(a+b,a-b,a*b,a/b,a**b).division))

print(Math_class(a+b,a-b,a*b,a/b,a**b).exponent)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import os,time,datetime

class Time_and_date:

  def __init__(self,hours,minutes,seconds,day,month,date,year,weeks,days):

    self.hours = hours
    self.minutes = minutes
    self.seconds = seconds
    self.day = day
    self.month = month
    self.date = date
    self.year = year
    self.weeks = weeks
    self.days = days

while True:

  time = datetime.datetime.now().strftime

  a,b,c,d,e,f,g,h,i = (
    Time_and_date(time('%H:'),time('%M:'),time('%S'),time('%A'),time('%B'),time('%d,'),time('%Y'),time('%U'),time('%j')).hours,
    Time_and_date(time('%H:'),time('%M:'),time('%S'),time('%A'),time('%B'),time('%d,'),time('%Y'),time('%U'),time('%j')).minutes,
    Time_and_date(time('%H:'),time('%M:'),time('%S'),time('%A'),time('%B'),time('%d,'),time('%Y'),time('%U'),time('%j')).seconds,
    Time_and_date(time('%H:'),time('%M:'),time('%S'),time('%A'),time('%B'),time('%d,'),time('%Y'),time('%U'),time('%j')).day,
    Time_and_date(time('%H:'),time('%M:'),time('%S'),time('%A'),time('%B'),time('%d,'),time('%Y'),time('%U'),time('%j')).month,
    Time_and_date(time('%H:'),time('%M:'),time('%S'),time('%A'),time('%B'),time('%d,'),time('%Y'),time('%U'),time('%j')).date,
    Time_and_date(time('%H:'),time('%M:'),time('%S'),time('%A'),time('%B'),time('%d,'),time('%Y'),time('%U'),time('%j')).year,
    Time_and_date(time('%H:'),time('%M:'),time('%S'),time('%A'),time('%B'),time('%d,'),time('%Y'),time('%U'),time('%j')).weeks,
    Time_and_date(time('%H:'),time('%M:'),time('%S'),time('%A'),time('%B'),time('%d,'),time('%Y'),time('%U'),time('%j')).days)

  print(a+b+c,d,e,f,g,f'\nweeks {h} days {i}')

  os.system('cls')

