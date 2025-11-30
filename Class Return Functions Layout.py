
# Class examples that show step by step, how to create classes in Python.
# Start with this easy to understand class example below first to gain an
# understanding of how classes work in Python. The 'self' variable calls
# itself to give access to class attribute properties. Note: 'self' can be any
# name you like. However, the variable name 'self' is the programming
# standard in Python; Python programmers prefer the 'self' variable name.

class Main_class:

  def __init__(self,attribute):  # two parameters: 'self' and 'attribute'

    self.attribute = attribute

print(Main_class('See the attribute value on the screen output.').attribute)

# Invoke the variable name 'me' instead of the variable name 'self'.

class Main_class:

  def __init__(me,attribute):  # two parameters: 'me' and 'attribute'

    me.Happy_Python_Programming = attribute

print(Main_class('See the attribute value on the screen output.').Happy_Python_Programming)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main_class:

  def __init__(self,attribute):

    self.attribute = attribute

  def return_attributes(self):
    return f'{self.argument_placeholder}'

print(Main_class('See the return attribute value on the screen output.').attribute)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main_class:

  def __init__(self,attribute1,attribute2,attribute3):  # four parameters: including 'self'

    self.attribute1 = attribute1
    self.attribute2 = attribute2
    self.attribute3 = attribute3

print(Main_class('attribute1','attribute2','attribute3').attribute3)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main_class:

  def __init__(self,attribute1,attribute2,attribute3):

    self.attribute1 = attribute1
    self.attribute2 = attribute2
    self.attribute3 = attribute3

  def return_attributes(self):
    return f'{self.argument_placeholder1} {self.argument_placeholder2} {self.argument_placeholder3}'

print(Main_class('return attribute1','return attribute2','return attribute3').attribute3)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main_class:

  def __init__(self,attribute1,attribute2,attribute3):

    self.attribute1 = attribute1
    self.attribute2 = attribute2
    self.attribute3 = attribute3

class Child_class(Main_class):
  pass

print(Main_class('attribute1','attribute2','attribute3').attribute3)

print(Child_class('attribute1','attribute2','attribute3').attribute3)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main_class:

  def __init__(self,attribute1,attribute2,attribute3):

    self.attribute1 = attribute1
    self.attribute2 = attribute2
    self.attribute3 = attribute3

  def return_attributes(self):
    return f'{self.argument_placeholder1} {self.argument_placeholder2} {self.argument_placeholder3}'

class Child_class(Main_class):
  pass

print(Main_class('return attribute1','return attribute2','return attribute3').attribute3)

print(Child_class('attribute1','attribute2','attribute3').attribute3)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main_class:

  def __init__(self,attribute1,attribute2,attribute3):

    self.attribute1 = attribute1
    self.attribute2 = attribute2
    self.attribute3 = attribute3

class Super_class(Main_class):

  def __init__(self,attribute1,attribute2,attribute3,attribute4):  # five parameters, including 'self'
    super().__init__(attribute1,attribute2,attribute3)

    self.attribute4 = attribute4

class Child_class(Super_class,Main_class):  # Method Resolution Order (MRO)
  pass

print(Main_class('attribute1','attribute2','attribute3').attribute3)

print(Super_class('attribute1','attribute2','attribute3','attribute4').attribute4)

print(Child_class('attribute1','attribute2','attribute3','attribute4').attribute4)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main_class:

  def __init__(self,attribute1,attribute2,attribute3):

    self.attribute1 = attribute1
    self.attribute2 = attribute2
    self.attribute3 = attribute3

class Super_class(Main_class):

  def __init__(self,attribute1,attribute2,attribute3,attribute4):
    super().__init__(attribute1,attribute2,attribute3)

    self.attribute4 = attribute4

  def return_attributes(self):
    return f'{self.argument_placeholder1} {self.argument_placeholder2} {self.argument_placeholder3}'

class Child_class(Super_class,Main_class):  # Method Resolution Order (MRO)
  pass

print(Main_class('attribute1','attribute2','attribute3').attribute3)

print(Super_class('return attribute1','return attribute2','return attribute3','return attribute4').attribute4)

print(Child_class('attribute1','attribute2','attribute3','attribute4').attribute4)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main_class:

  def __init__(self,attribute1,attribute2,attribute3):

    self.attribute1 = attribute1
    self.attribute2 = attribute2
    self.attribute3 = attribute3

  def return_attributes(self):
    return f'{self.argument_placeholder1} {self.argument_placeholder2} {self.argument_placeholder3}'

class Super_class(Main_class):

  def __init__(self,attribute1,attribute2,attribute3,attribute4):
    super().__init__(attribute1,attribute2,attribute3)

    self.attribute4 = attribute4

  def return_attributes(self):
    return f'{self.argument_placholder1} {self.argument_placeholder2} {self.argument_placeholder3} {self.argument_placeholder4}'

class Child_class(Super_class,Main_class):  # Method Resolution Order (MRO)
  pass

print(Main_class('return attribute1','return attribute2','return attribute3').attribute3)

print(Super_class('return attribute1','return attribute2','return attribute3','return attribute4').attribute4)

print(Child_class('attribute1','attribute2','attribute3','attribute4').attribute4)
