
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

  def single(self):return 'Single Class Act.'

print(Single_class_skeleton_structure().single())
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Skeletal Inheritance Class Act with return define functions:

class Main_class_skeleton_structure:

  def main(self):return 'Main Class Act.'

class Sub_class_skeleton_structure_one(Main_class_skeleton_structure):

  def sub1(self):return 'Sub One Class Act.'

class Sub_class_skeleton_structure_two(Sub_class_skeleton_structure_one):

  def sub2(self):return 'Sub Two Class Act.'

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

  def return_function1(self):return 'Main Class Act.'

class Sub_super_class_skeleton_structure_one(Main_class_skeleton_structure):
  def __init__(self,parameter1,parameter2,parameter3):pass

  def __init__(self,parameter1,parameter2,parameter3):
    super().__init__(parameter1,parameter2,parameter3)

  def return_function2(self):return 'Sub One Class Act.'

class Sub_super_class_skeleton_structure_two(Sub_super_class_skeleton_structure_one):
  def __init__(self,parameter1,parameter2,parameter3):pass

  def __init__(self,parameter1,parameter2,parameter3):
    super().__init__(parameter1,parameter2,parameter3)

  def return_function3(self):return 'Sub Two Class Act.'

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

# I am almost a complete Walking Human Computer Science Research
# Laboratory Machine on Two Legs... 😁
