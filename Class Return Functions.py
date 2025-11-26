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
class polygons:
    def __init__(self,polygon,num,sides):

        self.polygon = polygon
        self.num = num
        self.sides = sides

    def return_polygon_sides(self):
        return f'{self.polygon} {self.num} {self.sides}'

a = polygons('Triangle',3,'sides')
b = polygons('Square',4,'sides')
c = polygons('Pentagon',5,'sides')
d = polygons('Hexagon',6,'sides')
e = polygons('Heptagon',7,'sides')
f = polygons('Octagon',8,'sides')
g = polygons('Nonagon',9,'sides')
h = polygons('Decagon',10,'sides')
i = polygons('Hendecagon',11,'sides')
j = polygons('Dodecagon',12,'sides')
k = polygons('Tridecagon',13,'sides')
l = polygons('Tetradecagon',14,'sides')
m = polygons('Pentadecagon',15,'sides')
n = polygons('Hexadecagon',16,'sides')
o = polygons('Heptadecagon',17,'sides')
p = polygons('Octadecagon',18,'sides')
q = polygons('Enneadecagon',19,'sides')
r = polygons('Icosagon',20,'sides')

print(f'{a.polygon} {b.polygon} {c.polygon}')
print(f'{a.num} {b.num} {c.num}')

print(f'{a.return_polygon_sides()}')
print(f'{b.return_polygon_sides()}')
print(f'{c.return_polygon_sides()}')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class polygons:
    def __init__(self,polygon,num,sides):

        self.polygon = polygon
        self.num = num
        self.sides = sides

    def return_polygon_sides(self):
        return f'{self.polygon} {self.num} {self.sides}'

polygon_list = [
  polygons('Triangle',3,'sides'),polygons('Square',4,'sides'),polygons('Pentagon',5,'sides'),
  polygons('Hexagon',6,'sides'),polygons('Heptagon',7,'sides'),polygons('Nonagon',9,'sides'),
  polygons('Decagon',10,'sides'),polygons('Hendecagon',11,'sides'),polygons('Dodecagon',12,'sides'),
  polygons('Tridecagon',13,'sides'),polygons('Tetradecagon',14,'sides'),polygons('Pentadecagon',15,'sides'),
  polygons('Hexadecagon',16,'sides'),polygons('Heptadecagon',17,'sides'),polygons('Octadecagon',18,'sides'),
  polygons('Enneadecagon',19,'sides'),polygons('Icosagon',20,'sides')]

for i in polygon_list:
  print(i.return_polygon_sides())
