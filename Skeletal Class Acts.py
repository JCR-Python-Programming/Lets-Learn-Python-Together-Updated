
# Skeletal Single Class Act:

class Single_class_skeleton_structure:
  def single(self):
    print('Single Class Act.')

Single_class_skeleton_structure().single()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Skeletal Inheritance Class Act:

class Main_class_skeleton_structure:
  def main(self):
    print('Main Class Act.')

class Sub_class_skeleton_structure_one(Main_class_skeleton_structure):
  def sub1(self):
    print('Sub One Class Act.')

class Sub_class_skeleton_structure_two(Sub_class_skeleton_structure_one):
  def sub2(self):
    print('Sub Two Class Act.')

class Class_all(
  Sub_class_skeleton_structure_two,  # Method Resolution Order
  Sub_class_skeleton_structure_one,
  Main_class_skeleton_structure):pass

Class_all().main()
Class_all().sub1()
Class_all().sub2()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Skeletal Super Inheritance Class Act:

class Main_class_skeleton_structure:
  def __init__(self,parameter1,parameter2,parameter3):  # attribute property parameters
    self.parameter1 = parameter1
    self.parameter2 = parameter2
    self.parameter3 = parameter3

class Sub_super_class_skeleton_structure_one(Main_class_skeleton_structure):
  def __init__(self,parameter1,parameter2,parameter3):pass

  def __init__(self,parameter1,parameter2,parameter3):
    super().__init__(parameter1,parameter2,parameter3)

class Sub_super_class_skeleton_structure_two(Sub_super_class_skeleton_structure_one):
  def __init__(self,parameter1,parameter2,parameter3):pass

  def __init__(self,parameter1,parameter2,parameter3):
    super().__init__(parameter1,parameter2,parameter3)

class Class_all(
  Sub_super_class_skeleton_structure_two,  # Method Resolution Order
  Sub_super_class_skeleton_structure_one,
  Main_class_skeleton_structure):pass

print(Class_all('Main Class Act.','Sub One Class Act.','Sub Two Class Act.').parameter1)
print(Class_all('Main Class Act.','Sub One Class Act.','Sub Two Class Act.').parameter2)
print(Class_all('Main Class Act.','Sub One Class Act.','Sub Two Class Act.').parameter3)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Skeletal Single Class Act with return define function:

class Single_class_skeleton_structure:

  def single(self):
    return 'Single Class Act.'

print(Single_class_skeleton_structure().single())
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Skeletal Inheritance Class Act with return define functions:

class Main_class_skeleton_structure:

  def main(self):
    return 'Main Class Act.'

class Sub_class_skeleton_structure_one(Main_class_skeleton_structure):

  def sub1(self):
    return 'Sub One Class Act.'

class Sub_class_skeleton_structure_two(Sub_class_skeleton_structure_one):

  def sub2(self):
    return 'Sub Two Class Act.'

class Class_all(
  Sub_class_skeleton_structure_two,  # Method Resolution Order
  Sub_class_skeleton_structure_one,
  Main_class_skeleton_structure):pass

print(Class_all().main())
print(Class_all().sub1())
print(Class_all().sub2())
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Skeletal Super Inheritance Class Act with return define functions:

class Main_class_skeleton_structure:
  def __init__(self,parameter1,parameter2,parameter3):  # attribute property parameters
    self.parameter1 = parameter1
    self.parameter2 = parameter2
    self.parameter3 = parameter3

  def return_function1(self):
    return 'Main Class Act.'

class Sub_super_class_skeleton_structure_one(Main_class_skeleton_structure):
  def __init__(self,parameter1,parameter2,parameter3):pass

  def __init__(self,parameter1,parameter2,parameter3):
    super().__init__(parameter1,parameter2,parameter3)

  def return_function2(self):
    return 'Sub One Class Act.'

class Sub_super_class_skeleton_structure_two(Sub_super_class_skeleton_structure_one):
  def __init__(self,parameter1,parameter2,parameter3):pass

  def __init__(self,parameter1,parameter2,parameter3):
    super().__init__(parameter1,parameter2,parameter3)

  def return_function3(self):
    return 'Sub Two Class Act.'

class Class_all(
  Sub_super_class_skeleton_structure_two,  # Method Resolution Order
  Sub_super_class_skeleton_structure_one,
  Main_class_skeleton_structure):pass

print(Class_all('Main Class Act.','Sub One Class Act.','Sub Two Class Act.').parameter1)
print(Class_all('Main Class Act.','Sub One Class Act.','Sub Two Class Act.').parameter2)
print(Class_all('Main Class Act.','Sub One Class Act.','Sub Two Class Act.').parameter3)

print(Class_all('arg placeholder value1','arg placeholder value2','arg placeholder value3').return_function1())
print(Class_all('arg placeholder value1','arg placeholder value2','arg placeholder value3').return_function2())
print(Class_all('arg placeholder value1','arg placeholder value2','arg placeholder value3').return_function3())

print(Main_class_skeleton_structure(
  'arg placeholder value1','arg placeholder value2','arg placeholder value3').return_function1())


print(Sub_super_class_skeleton_structure_one(
  'arg placeholder value1','arg placeholder value2','arg placeholder value3').return_function1())

print(Sub_super_class_skeleton_structure_one(
  'arg placeholder value1','arg placeholder value2','arg placeholder value3').return_function2())


print(Sub_super_class_skeleton_structure_two(
  'arg placeholder value1','arg placeholder value2','arg placeholder value3').return_function1())

print(Sub_super_class_skeleton_structure_two(
  'arg placeholder value1','arg placeholder value2','arg placeholder value3').return_function2())

print(Sub_super_class_skeleton_structure_two(
  'arg placeholder value1','arg placeholder value2','arg placeholder value3').return_function3())
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Skeletal Single Class Act with return define function, along with two returned values:

class Single_class_skeleton_structure:

  def single(self,parameter1,parameter2):
    return 'Return Single Class Act One.','Return Single Class Act Two.'

print(Single_class_skeleton_structure().single('arg placeholder value1','arg placeholder value2')[0])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Skeletal Inheritance Class Act with return define function, along with two returned values:

class Main_class_skeleton_structure:
  def main(self,parameter1,parameter2):
    return 'Return Main Class Act One.','Return Main Class Act Two.'

class Sub_class_skeleton_structure_one(Main_class_skeleton_structure):
  def sub1(self,parameter1,parameter2):
    return 'Return Sub1 Class Act One.','Return Sub1 Class Act Two.'

class Sub_class_skeleton_structure_two(Sub_class_skeleton_structure_one):
  def sub2(self,parameter1,parameter2):
    return 'Return Sub2 Class Act One.','Return Sub2 Class Act Two.'

class Class_all(
  Sub_class_skeleton_structure_two,  # Method Resolution Order
  Sub_class_skeleton_structure_one,
  Main_class_skeleton_structure):pass

print(Class_all().main('arg placeholder value1','arg placeholder value2')[0])
print(Class_all().sub1('arg placeholder value1','arg placeholder value2')[0])
print(Class_all().sub2('arg placeholder value1','arg placeholder value2')[0])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Skeletal Super Inheritance Class Act with return define function, along with two returned values:

class Main_class_skeleton_structure:
  def __init__(self,parameter1,parameter2,parameter3):  # attribute property parameters
    self.parameter1 = parameter1
    self.parameter2 = parameter2
    self.parameter3 = parameter3

  def return_function1(self,parameter1,parameter2):
    return 'Return Main Class Act One.','Return Main Class Act Two.'

class Sub_super_class_skeleton_structure_one(Main_class_skeleton_structure):
  def __init__(self,parameter1,parameter2,parameter3):pass

  def __init__(self,parameter1,parameter2,parameter3):
    super().__init__(parameter1,parameter2,parameter3)

  def return_function2(self,parameter1,parameter2):
    return 'Return Sub1 Class Act One.','Return Sub1 Class Act Two.'

class Sub_super_class_skeleton_structure_two(Sub_super_class_skeleton_structure_one):
  def __init__(self,parameter1,parameter2,parameter3):pass

  def __init__(self,parameter1,parameter2,parameter3):
    super().__init__(parameter1,parameter2,parameter3)

  def return_function3(self,parameter1,parameter2):
    return 'Return Sub2 Class Act One.','Return Sub2 Class Act Two.'

class Class_all(
  Sub_super_class_skeleton_structure_two,  # Method Resolution Order
  Sub_super_class_skeleton_structure_one,
  Main_class_skeleton_structure):pass

print(Class_all('Main Class Act.','Sub One Class Act.','Sub Two Class Act.').parameter1)
print(Class_all('Main Class Act.','Sub One Class Act.','Sub Two Class Act.').parameter2)
print(Class_all('Main Class Act.','Sub One Class Act.','Sub Two Class Act.').parameter3)


print(Class_all.return_function1('arg placeholder value1','arg placeholder value2','arg placeholder value3')[0])
print(Class_all.return_function2('arg placeholder value1','arg placeholder value2','arg placeholder value3')[0])
print(Class_all.return_function3('arg placeholder value1','arg placeholder value2','arg placeholder value3')[0])


print(Main_class_skeleton_structure.return_function1(
  'arg placeholder value1','arg placeholder value2','arg placeholder value3')[0])


print(Sub_super_class_skeleton_structure_one.return_function1(
  'arg placeholder value1','arg placeholder value2','arg placeholder value3')[0])

print(Sub_super_class_skeleton_structure_one.return_function2(
  'arg placeholder value1','arg placeholder value2','arg placeholder value3')[0])


print(Sub_super_class_skeleton_structure_two.return_function1(
  'arg placeholder value1','arg placeholder value2','arg placeholder value3')[0])

print(Sub_super_class_skeleton_structure_two.return_function2(
  'arg placeholder value1','arg placeholder value2','arg placeholder value3')[0])

print(Sub_super_class_skeleton_structure_two.return_function3(
  'arg placeholder value1','arg placeholder value2','arg placeholder value3')[0])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Polygons:
  def __init__(self,polygon,sides,colour):

    self.polygon = polygon
    self.sides = sides
    self.colour = colour

  def return_selfction(self):
    return polygons[0],sides[0],colour_name[0]

  def class_data(self):
    print(self.colour,self.polygon,'has',self.sides)

for i in range(18):
  Polygons(polygons[i],sides[i],colour_name[0]).class_data()

print(Polygons.return_selfction('Agument Placeholder Value')[2])

print(Polygons.return_selfction('Agument Placeholder Value')[0])

print(Polygons.return_selfction('Agument Placeholder Value')[1])

# I am almost a complete Walking Human Computer Science Research
# Laboratory Machine on Two Legs... 😁
