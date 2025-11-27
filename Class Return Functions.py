class Class_act:

  def __init__(self,attribute1,attribute2):

    self.attribute1 = attribute1  # attribute1 property:

    self.attribute2 = attribute2  # attribute2 property:

  def return_first_name(fname):
    return 'John'

  def return_last_name(lname):
    return 'Smith'

  def return_age(age):
    return 60

class_attribute_values = Class_act(
  'I am the attribute property value of attribute1',
  'I am the attribute property value of attribute2')

print(class_attribute_values.attribute1)

print(class_attribute_values.attribute2)

print(Class_act.return_first_name('argument placeholder'))

print(Class_act.return_last_name('argument placeholder'))

print(Class_act.return_age('argument placeholder'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Class_act:

  def __init__(self,attribute1,attribute2):

    self.attribute1 = attribute1  # attribute1 property:

    self.attribute2 = attribute2  # attribute2 property:

  def return_first_name(fname):
    return fname

  def return_last_name(lname):
    return lname

  def return_age(age):
    return age

  def return_addition(num1,num2):
    return num1+num2

class_attribute_values = Class_act(
  'I am the attribute property value of attribute1',
  'I am the attribute property value of attribute2')

print(class_attribute_values.attribute1)

print(class_attribute_values.attribute2)

print(Class_act.return_first_name('John'))

print(Class_act.return_last_name('Smith'))

print(Class_act.return_age(60))

print(Class_act.return_addition(50,10))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Class_act:

  def __init__(self,fname,lname,age):

    self.fname = fname  # attribute1 property:

    self.lname = lname  # attribute2 property:

    self.age = age  # attribute3 property:

  def return_name_age(self):
    return f'{self.fname} {self.lname} {self.age}'

print(Class_act('John','Smith',60).return_name_age())

# or this:

a = Class_act('John','Smith',60)

print(a.return_name_age())

# or this:

a = Class_act('John','Smith',60).return_name_age()

print(a)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Class_act:

  def __init__(self,fname,lname,age):

    self.fname = fname  # attribute1 property:

    self.lname = lname  # attribute2 property:

    self.age = age  # attribute3 property:

  def return_name_age(self):
    return f'{self.fname} {self.lname} {self.age}'

class Super_Class(Class_act):

  def __init__(self,fname,lname,age):
    super().__init__(fname,lname,age)

  def return_super_class(self):
    return f'{self.fname} {self.lname} {self.age}'

print(Class_act('John','Smith',60).return_name_age())

print(Super_Class('Super','Smith',60).return_name_age())

print(Super_Class('Super','Smith',60).return_super_class())

# or this:

a = Class_act('John','Smith',60)

b = Super_Class('Super','Smith',60)

print(a.return_name_age())

print(b.return_name_age())

print(b.return_super_class())

# or this:

a = Class_act('John','Smith',60).return_name_age()

b = Super_Class('Super','Smith',60).return_name_age()

c = Super_Class('Super','Smith',60).return_super_class()

print(a)

print(b)

print(c)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Polygons:
    def __init__(shape,polygon,num,sides):

        shape.polygon = polygon
        shape.num = num
        shape.sides = sides

    def return_Polygons(shape):
        return f'{shape.polygon} {shape.num} {shape.sides}'

a = Polygons('Triangle',3,'sides')
b = Polygons('Square',4,'sides')
c = Polygons('Pentagon',5,'sides')
d = Polygons('Hexagon',6,'sides')
e = Polygons('Heptagon',7,'sides')
f = Polygons('Octagon',8,'sides')
g = Polygons('Nonagon',9,'sides')
h = Polygons('Decagon',10,'sides')
i = Polygons('Hendecagon',11,'sides')
j = Polygons('Dodecagon',12,'sides')
k = Polygons('Tridecagon',13,'sides')
l = Polygons('Tetradecagon',14,'sides')
m = Polygons('Pentadecagon',15,'sides')
n = Polygons('Hexadecagon',16,'sides')
o = Polygons('Heptadecagon',17,'sides')
p = Polygons('Octadecagon',18,'sides')
q = Polygons('Nonadecagon',19,'sides')
r = Polygons('Icosagon',20,'sides')

print(f'{a.polygon} {b.polygon} {c.polygon}')
print(f'{a.num} {b.num} {c.num}')

print(f'{a.return_Polygons()}')
print(f'{b.return_Polygons()}')
print(f'{c.return_Polygons()}')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Polygons:
    def __init__(shape,polygon,num,sides):

        shape.polygon = polygon
        shape.num = num
        shape.sides = sides

    def return_Polygons(shape):
        return f'{shape.polygon} {shape.num} {shape.sides}'

polygon_list = [
  Polygons('Triangle',3,'sides'),Polygons('Square',4,'sides'),
  Polygons('Pentagon',5,'sides'),Polygons('Hexagon',6,'sides'),
  Polygons('Heptagon',7,'sides'),Polygons('Octagon',8,'sides'),
  Polygons('Nonagon',9,'sides'),Polygons('Decagon',10,'sides'),
  Polygons('Hendecagon',11,'sides'),Polygons('Dodecagon',12,'sides'),
  Polygons('Tridecagon',13,'sides'),Polygons('Tetradecagon',14,'sides'),
  Polygons('Pentadecagon',15,'sides'),Polygons('Hexadecagon',16,'sides'),
  Polygons('Heptadecagon',17,'sides'),Polygons('Octadecagon',18,'sides'),
  Polygons('Nonadecagon',19,'sides'), Polygons('Icosagon',20,'sides')]

for i in polygon_list:
  print(i.return_Polygons())
