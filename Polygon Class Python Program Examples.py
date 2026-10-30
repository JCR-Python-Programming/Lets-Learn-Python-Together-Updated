
# Polygon Class Python Program Examples:

# by Joseph C. Richardson, GitHub.com

# These Python classes are designed for the medium
# to advanced Python programmer. These polygon
# class Python program examples show step by step
# ways to create classes. This lesson clearly shows
# manual, redundant ways to create Python classes.
# As we go, we will learn how to keep our code completely
# DRY!: (Don't Repeat Yourself!). For now, let's take
# things slow and easy. Most importantly. Do not over
# concentrate! Take your time to learn Python. Now, let's
# WAX on and WAX off. Shall we...

# Here is tuple of values that you can use for your class
# attribute property values. There are 18 tuple values to
# choose from.

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

class Polygon:

# Let's learn what 'documentation strings' do with classes. In Python,
# we call these 'doctrings'. We  need to invoke three double quote
# marks """ on each side of the docstring title: """Polygon""".
# The getattr() function simply means the word: 'get attribute'. With
# docstrings, we can see the documentation payload/description
# block of the class at execution/run time. Docstrings are like a
# comment; they descibe what the class is about at execution/run
# time.

  """Polygon"""  # documentation payload/description block

# Let's learn what __slots__ do! Slots reserve exact memory
# for class attributes. You don't need a huge, empty warehouse
# just to store a few attributes. Slots optimize memory and performance.
# Research Python __slots__ to learn more about them. Two double
# underscores __ __ are required to create __slots__. Simply
# press and hold down the shift key, while pressing the minus key.

# Note: when invoking __slots__ with only one attribute, you must
# place a comma ',' at the end of the slot's single attribute, as not
# to confuse it as a tuple value at execution/run time.

  __slots__ = ('polygons1','polygons2','polygons3','polygons4')  # __slots__ optimizes memory and performance

  def __init__(self,polygons1,polygons2,polygons3,polygons4):  # five parameters

    self.polygons1 = polygons1
    self.polygons2 = polygons2
    self.polygons3 = polygons3
    self.polygons4 = polygons4  # four explicit attribute properties

print(getattr(Polygon,'__doc__'))

# Please note: arguments are nothing more than the values you
# see on a computer's monitor at execution/run time, such as the
# word 'Hello' that prints out onto the screen when you type and
# execute/run this Python program example below.

# This what class instance looks like:

# four explicit argument placeholder values

print(Polygon(polygons[0],polygons[1],polygons[2],polygons[3]).polygons1)

# The getattr('get attribute') lookup, looks up valid attributes.
# Think of 'getattr' as the attribute gatekeeper. If an attribute
# does not exist, or is floating, bleeding into other class attributes,
# the gatekeeper, 'getattr' looks up exact attributes with their
# class only. The fallback, 'Attribute Not Found' text prevents
# program crashes from occurring, should a wrong attribute or
# name error happen.

# When an attribute is not found, a fallback error message will stop
# the program from crashing.

print(getattr(Polygon(polygons[0],polygons[1],polygons[2],polygons[3]),'bogus attribute','Sorry! Attribute not found:'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Try these implicit instance argument placeholder value examples:

class Polygon:

  """Polygon"""  # documentation payload/description block

  __slots__ = ('polygons1','polygons2','polygons3','polygons4')  # __slots__ optimizes memory and performance

  def __init__(self,polygons1,polygons2,polygons3,polygons4):  # five parameters

    self.polygons1 = polygons[0]
    self.polygons2 = polygons[1]
    self.polygons3 = polygons[2]
    self.polygons4 = polygons[3]  # four implicit attribute properties

print(getattr(Polygon,'__doc__'))

print(Polygon(
  'argument placeholder',
  'argument placeholder',
  'argument placeholder',
  'argument placeholder').polygons1)  # four implicit argument placeholder values

# or this:

print(Polygon('','','','').polygons1)  # four implicit argument placeholder values

print(getattr(Polygon('','','',''),'polygons1'))  # four implicit argument placeholder values

# or this:

print(Polygon(None,None,None,None).polygons1)  # four implicit argument placeholder values

print(getattr(Polygon(None,None,None,None),'polygons1'))  # four implicit argument placeholder values

# When an attribute is not found, a fallback error message will stop the program
# from crashing.

print(getattr(Polygon(None,None,None,None),'bogus attribute','Sorry! Attribute not found:'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's learn what *args and **kwargs do. These are easy, once
# you learn them. We will take it step by step, like we did before.
# Invoke the asterisk * in front of the *args attribute. Note: *args
# can be any name you wish. However, the Python standard is
# invoked as *args for its name, which is short for the name
# 'arguments'.

# With *args, we don't have to worry about how many parameters
# we need to satisfy how many arguments we need as we had to
# before. *args are great when there are far too many arguments
# needed to satisfy the exact number of parameter values.

class Polygon:

  """Polygon"""  # documentation payload/description block

  __slots__ = ('args',)  # __slots__ optimizes memory and performance

  def __init__(self,*args):  # two parameters

    self.args = args  # one attribute

print(getattr(Polygon,'__doc__'))

print(Polygon(polygons[0],polygons[1],polygons[2],polygons[3]).args[0])  # four explicit argument placeholder values

print(getattr(Polygon(polygons[0],polygons[1],polygons[2],polygons[3]),'args')[0])  # four explicit argument placeholder values

# When an attribute is not found, a fallback error message will stop the program
# from crashing.

# four explicit argument placeholder values

print(getattr(Polygon(polygons[0],polygons[1],polygons[2],polygons[3]),'bogus attribute',['Sorry! Attribute not found:'])[0])

 # or this:

print(getattr(Polygon(polygons[0],polygons[1],polygons[2],polygons[3]),'bogus attribute',[''])[0])

# or this:

print(getattr(Polygon(polygons[0],polygons[1],polygons[2],polygons[3]),'bogus attribute',[None])[0])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's see what **kwargs do. Invoke the double asterisk ** in front of
# the **kwargs attribute. Note: **kwargs can be any name you wish.
# However, the Python standard is invoked as **kwargs for its name,
# which is short for the name 'keyword_arguments'.

# With **kwargs, we don't have to worry about how many parameters
# we need to satisfy how many keyword arguments we need as we
# had to before. **kwargs are great when there are far too many keyword
# arguments needed to satisfy the exact number of parameter values.

class Polygon:

  """Polygon"""  # documentation payload/description block

  __slots__ = ('__dict__',)  # __slots__ optimizes memory and performance

  def __init__(self,**kwargs):  # two parameters

    self.__dict__.update(kwargs)

print(getattr(Polygon,'__doc__'))

# four explicit keyword argument placeholder values

print(getattr(Polygon(
  kwarg1 = polygons[0],
  kwarg2 = polygons[1],
  kwarg3 = polygons[3],
  kwarg4 = polygons[4]),'kwarg1'))

# When an attribute is not found, a fallback error message will stop
# the program from crashing.

print(getattr(Polygon(
  kwarg1 = polygons[0],
  kwarg2 = polygons[1],
  kwarg3 = polygons[3],
  kwarg4 = polygons[4]),'bogus attribute','Sorry! Attribute not found:'))

# or this:

print(getattr(Polygon(
  kwarg1 = polygons[0],
  kwarg2 = polygons[1],
  kwarg3 = polygons[3],
  kwarg4 = polygons[4]),'bogus attribute',''))

# or this:

print(getattr(Polygon(
  kwarg1 = polygons[0],
  kwarg2 = polygons[1],
  kwarg3 = polygons[3],
  kwarg4 = polygons[4]),'bogus attribute',None))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Polygon:

  """Polygon"""  # documentation payload/description block

  __slots__ = ('kwargs',)  # __slots__ optimizes memory and performance

  def __init__(self,**kwargs):  # two parameters

    self.kwargs = kwargs  # one attribute

print(getattr(Polygon,'__doc__'))

# four explicit keyword argument placeholder values

print(getattr(Polygon(
  kwargs1 = polygons[0],
  kwargs2 = polygons[1],
  kwargs3 = polygons[2],
  kwargs4 = polygons[3]),'kwargs').get('kwargs1'))

# When an attribute is not found, a fallback error message will stop
# the program from crashing.

print(getattr(Polygon(
  kwargs1 = polygons[0],
  kwargs2 = polygons[1],
  kwargs3 = polygons[2],
  kwargs4 = polygons[3]),'kwargs').get('bogus attribute','Sorry! Attribute not found:'))

# or this:

print(getattr(Polygon(
  kwargs1 = polygons[0],
  kwargs2 = polygons[1],
  kwargs3 = polygons[2],
  kwargs4 = polygons[3]),'kwargs').get('bogus attribute',''))

# or this:

print(getattr(Polygon(
  kwargs1 = polygons[0],
  kwargs2 = polygons[1],
  kwargs3 = polygons[2],
  kwargs4 = polygons[3]),'kwargs').get('bogus attribute',None))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Polygon:

  """Polygon"""  # documentation payload/description block

  __slots__ = ('args','kwargs')  # __slots__ optimizes memory and performance

  def __init__(self,*args,**kwargs):  # two parameters

    self.args = args
    self.kwargs = kwargs  # two attribute

print(getattr(Polygon,'__doc__'))

# four explicit argument placeholder values

print(getattr(Polygon(
  polygons[0],polygons[1],
  polygons[2],polygons[3]),'args')[0])

# four explicit keyword argument placeholder values

print(getattr(Polygon(
  kwargs1 = polygons[0],
  kwargs2 = polygons[1],
  kwargs3 = polygons[2],
  kwargs4 = polygons[3]),'kwargs').get('kwargs1'))

# When an attribute is not found, a fallback error message will stop
# the program from crashing.

print(getattr(Polygon(
  polygons[0],polygons[1],
  polygons[2],polygons[3]),'bogus attribute',['Sorry! Attribute not found:'])[0])

# or this:

print(getattr(Polygon(
  polygons[0],polygons[1],
  polygons[2],polygons[3]),'bogus attribute',[''])[0])

# or this:

print(getattr(Polygon(
  polygons[0],polygons[1],
  polygons[2],polygons[3]),'bogus attribute',[None])[0])

# When an attribute is not found, a fallback error message will stop
# the program from crashing.

print(getattr(Polygon(
  kwargs1 = polygons[0],
  kwargs2 = polygons[1],
  kwargs3 = polygons[2],
  kwargs4 = polygons[3]),'kwargs').get('bogus attribute','Sorry! Attribute not found:'))

# or this:

print(getattr(Polygon(
  kwargs1 = polygons[0],
  kwargs2 = polygons[1],
  kwargs3 = polygons[2],
  kwargs4 = polygons[3]),'kwargs').get('bogus attribute',''))

# or this:

print(getattr(Polygon(
  kwargs1 = polygons[0],
  kwargs2 = polygons[1],
  kwargs3 = polygons[2],
  kwargs4 = polygons[3]),'kwargs').get('bogus attribute',None))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create some instance variables for our print() function.

class Polygon:

  """Polygon""" # documentation payload/description block

  __slots__ = ('polygons1','polygons2','polygons3','polygons4')  # __slots__ optimizes memory and performance

  def __init__(self,polygons1,polygons2,polygons3,polygons4):  # five parameters

    self.polygons1 = polygons1
    self.polygons2 = polygons2
    self.polygons3 = polygons3
    self.polygons4 = polygons4  # four explicit attribute properties

print(getattr(Polygon,'__doc__'))

# four explicit argument placeholder values

instance_var = Polygon(polygons[0],polygons[1],polygons[2],polygons[3])

print(instance_var.polygons1)

# four explicit argument placeholder values

print(getattr(instance_var,'polygons1'))

# When an attribute is not found, a fallback error message will stop
# the program from crashing.

print(getattr(instance_var,'bogus attribute','Sorry! Attribute not found:'))

# or this:

print(getattr(instance_var,'bogus attribute',''))

# or this:

print(getattr(instance_var,'bogus attribute',None))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create some instance variables for our print() function.

class Polygon:

  """Polygon"""  # documentation payload/description block

  __slots__ = ('polygons1','polygons2','polygons3','polygons4')  # __slots__ optimizes memory and performance

  def __init__(self,polygons1,polygons2,polygons3,polygons4):  # five parameters

    self.polygons1 = polygons[0]
    self.polygons2 = polygons[1]
    self.polygons3 = polygons[2]
    self.polygons4 = polygons[3]  # four implicit attribute properties

print(getattr(Polygon,'__doc__'))

instance_var = Polygon('','','','')  # four implicit argument placeholder values

print(instance_var.polygons1)

print(getattr(instance_var,'polygons1'))  # four implicit argument placeholder values

# or this:

instance_var = Polygon(None,None,None,None)  # four implicit argument placeholder values

print(instance_var.polygons1)

# or this:

print(getattr(instance_var,'polygons1'))

# When an attribute is not found, a fallback error message will stop
# the program from crashing.

print(getattr(instance_var,'bogus attribute','Sorry! Attribute not found:'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create some instance variables for our print() function.

class Polygon:

  """Polygon"""  # documentation payload/description block

  __slots__ = ('args',)  # __slots__ optimizes memory and performance

  def __init__(self,*args):  # two parameters

    self.args = args  # one attribute

print(getattr(Polygon,'__doc__'))

# four explicit argument placeholder values

instance_var = Polygon(polygons[0],polygons[1],polygons[2],polygons[3])

print(instance_var.args[0])

print(getattr(instance_var,'args')[0])

# When an attribute is not found, a fallback error message will stop
# the program from crashing.

print(getattr(instance_var,'bogus attribute',['Sorry! Attribute not found:'])[0])

 # or this:

print(getattr(instance_var,'bogus attribute',[''])[0])

# or this:

print(getattr(instance_var,'bogus attribute',[None])[0])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create some instance variables for our print() function.

class Polygon:

  """Polygon"""  # documentation payload/description block

  __slots__ = ('__dict__',)  # __slots__ optimizes memory and performance

  def __init__(self,**kwargs):  # two parameters

    self.__dict__.update(kwargs)

print(getattr(Polygon,'__doc__'))

instance_var = (Polygon(
  kwarg1 = polygons[0],
  kwarg2 = polygons[1],
  kwarg3 = polygons[3],
  kwarg4 = polygons[4]))  #  four explicit keyword argument placeholder values

print(getattr(instance_var,'kwarg1'))

# When an attribute is not found, a fallback error message will stop
# the program from crashing.

print(getattr(instance_var,'bogus attribute','Sorry! Attribute not found:'))

# or this:

print(getattr(instance_var,'bogus attribute',''))

# or this:

print(getattr(instance_var,'bogus attribute',None))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create some instance variables for our print() function.

class Polygon:

  """Polygon"""  # documentation payload/description block

  __slots__ = ('kwargs',)  # __slots__ optimizes memory and performance

  def __init__(self,**kwargs):  # two parameters

    self.kwargs = kwargs  # one attribute

print(getattr(Polygon,'__doc__'))

instance_var = (Polygon(
  kwargs1 = polygons[0],
  kwargs2 = polygons[1],
  kwargs3 = polygons[2],
  kwargs4 = polygons[3]))  # four explicit keyword argument placeholder values

print(getattr(instance_var,'kwargs').get('kwargs3'))

# When an attribute is not found, a fallback error message will stop
# the program from crashing.

print(getattr(instance_var,'kwargs').get('bogus attribute','Sorry! Attribute not found:'))

# or this:

print(getattr(instance_var,'kwargs').get('bogus attribute',''))

# or this:

print(getattr(instance_var,'kwargs').get('bogus attribute',None))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create some instance variables for our print() function.

class Polygon:

  """Polygon"""  # documentation payload/description block

  __slots__ = ('args','kwargs')  # __slots__ optimizes memory and performance

  def __init__(self,*args,**kwargs):  # three parameters

    self.args = args
    self.kwargs = kwargs  # two attribute

print(getattr(Polygon,'__doc__'))

instance_var = Polygon(polygons[0],polygons[1],polygons[2],polygons[3])

print(getattr(instance_var,'args')[0])

instance_var = (Polygon(
  kwargs1 = polygons[0],
  kwargs2 = polygons[1],
  kwargs3 = polygons[2],
  kwargs4 = polygons[3]))  # four explicit keyword argument placeholder values

print(getattr(instance_var,'kwargs').get('kwargs1'))

# When an attribute is not found, a fallback error message will stop
# the program from crashing.

instance_var = Polygon(polygons[0],polygons[1],polygons[2],polygons[3])  # four explicit argument placeholder values

print(getattr(instance_var,'bogus attribute',['Sorry! Attribute not found:'])[0])

# or this:

print(getattr(instance_var,'bogus attribute',[''])[0])

# or this:

print(getattr(instance_var,'bogus attribute',[None])[0])

# When an attribute is not found, a fallback error message will stop
# the program from crashing.

instance_var = (Polygon(
  kwargs1 = polygons[0],kwargs2 = polygons[1],
  kwargs3 = polygons[2],kwargs4 = polygons[3]))  # four explicit keyword argument placeholder values

print(getattr(instance_var,'kwargs').get('bogus attribute','Sorry! Attribute not found:'))

# or this:

print(getattr(instance_var,'kwargs').get('bogus attribute',''))

# or this:

print(getattr(instance_var,'kwargs').get('bogus attribute',None))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create some for loop examples with our Polygon class instances.

class Polygon:

  """Polygon"""  # documentation payload/description block

  __slots__ = ('polygons1','polygons2','polygons3','polygons4')  # __slots__ optimizes memory and performance

  def __init__(self,polygons1,polygons2,polygons3,polygons4):  # five parameters

    self.polygons1 = polygons1
    self.polygons2 = polygons2
    self.polygons3 = polygons3
    self.polygons4 = polygons4  # four explicit attribute properties

print(getattr(Polygon,'__doc__'))

for i in polygons:
  print(Polygon(i,None,None,None).polygons1)  # four explicit argument placeholder values

# or this:

for i in polygons:
  print(getattr(Polygon(i,None,None,None),'polygons1','Sorry! Attribute not found:'))  # four explicit argument placeholder values

# or this:

for i in polygons:
  print(Polygon(i,i,i,i).polygons1)  # four explicit argument placeholder values

# or this:

for i in polygons:
  print(getattr(Polygon(i,i,i,i),'polygons1','Sorry! Attribute not found:'))  # four explicit argument placeholder values
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create some for loop examples with our Polygon class instances.

class Polygon:

  """Polygon"""  # documentation payload/description block

  __slots__ = ('args',)  # __slots__ optimizes memory and performance

  def __init__(self,*args):  # two parameters

    self.args = args  # one attribute

print(getattr(Polygon,'__doc__'))

for i in polygons:
  print(Polygon(i,None,None,None).args[0])  # four explicit argument placeholder values

# or this:

for i in polygons:
  print(getattr(Polygon(i,None,None,None),'args')[0])  # four explicit argument placeholder values

# or this:

for i in polygons:
  print(Polygon(i,i,i,i).args[0])  # four explicit argument placeholder values

# or this:

for i in polygons:
  print(getattr(Polygon(i,i,i,i),'args')[0])  # four explicit argument placeholder values
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create some for loop examples with our Polygon class instances.

class Polygon:

  """Polygon"""  # documentation payload/description block

  __slots__ = ('__dict__',)  # __slots__ optimizes memory and performance

  def __init__(self,**kwargs):  # two parameters

    self.__dict__.update(kwargs)

print(getattr(Polygon,'__doc__'))

# four explicit keyword argument placeholder values

for i in polygons:
  print(getattr(Polygon(
    kwarg1 = i,
    kwarg2 = None,
    kwarg3 = None,
    kwarg4 = None),'kwarg1'))

# When an attribute is not found, a fallback error message will stop
# the program from crashing.

for i in polygons:
  print(getattr(Polygon(
    kwarg1 = i,
    kwarg2 = None,
    kwarg3 = None,
    kwarg4 = None),'bogus attribute','Sorry! Attribute not found:'))

# or this:

for i in polygons:
  print(getattr(Polygon(
    kwarg1 = i,
    kwarg2 = i,
    kwarg3 = i,
    kwarg4 = i),'kwarg1'))

# When an attribute is not found, a fallback error message will stop
# the program from crashing.

for i in polygons:
  print(getattr(Polygon(
    kwarg1 = i,
    kwarg2 = i,
    kwarg3 = i,
    kwarg4 = i),'bogus attribute','Sorry! Attribute not found:'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create some for loop examples with our Polygon class instances.

class Polygon:

  """Polygon"""  # documentation payload/description block

  __slots__ = ('__dict__',)  # __slots__ optimizes memory and performance

  def __init__(self,**kwargs):  # two parameters

    self.kwargs = kwargs  # one attribute

print(getattr(Polygon,'__doc__'))

# four explicit keyword argument placeholder values

for i in polygons:
  print(getattr(Polygon(
    kwarg1 = i,
    kwarg2 = None,
    kwarg3 = None,
    kwarg4 = None),'kwargs').get('kwargs1'))

# When an attribute is not found, a fallback error message will stop
# the program from crashing.

for i in polygons:
  print(getattr(Polygon(
    kwarg1 = i,
    kwarg2 = None,
    kwarg3 = None,
    kwarg4 = None),'kwargs').get('bogus attribute','Sorry! Attribute not found:'))

# or this:

for i in polygons:
  print(getattr(Polygon(
    kwarg1 = i,
    kwarg2 = i,
    kwarg3 = i,
    kwarg4 = i),'kwargs').get('kwargs1'))

# When an attribute is not found, a fallback error message will stop
# the program from crashing.

for i in polygons:
  print(getattr(Polygon(
    kwarg1 = i,
    kwarg2 = i,
    kwarg3 = i,
    kwarg4 = i),'kwargs').get('bogus attribute','Sorry! Attribute not found:'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create some for loop examples with our Polygon class instances.

class Polygon:

  """Polygon"""  # documentation payload/description block

  __slots__ = ('args','__dict__')  # __slots__ optimizes memory and performance

  def __init__(self,*args,**kwargs):  # three parameters

    self.args = args
    self.__dict__.update(kwargs)

print(getattr(Polygon,'__doc__'))

# four explicit argument placeholder values

for i in polygons:
  print(Polygon(i,None,None,None).args[0])  # four explicit argument placeholder values

# or this:

for i in polygons:
  print(getattr(Polygon(i,None,None,None),'args')[0])  # four explicit argument placeholder values

# or this:

for i in polygons:
  print(Polygon(i,i,i,i).args[0])  # four explicit argument placeholder values

# or this:

for i in polygons:
  print(getattr(Polygon(i,i,i,i),'args')[0])  # four explicit argument placeholder values

# four explicit keyword argument placeholder values

for i in polygons:
  print(getattr(Polygon(
    kwarg1 = i,
    kwarg2 = None,
    kwarg3 = None,
    kwarg4 = None),'kwarg1'))

# When an attribute is not found, a fallback error message will stop
# the program from crashing.

for i in polygons:
  print(getattr(Polygon(
    kwarg1 = i,
    kwarg2 = None,
    kwarg3 = None,
    kwarg4 = None),'bogus attribute','Sorry! Attribute not found:'))

# or this:

for i in polygons:
  print(getattr(Polygon(
    kwarg1 = i,
    kwarg2 = i,
    kwarg3 = i,
    kwarg4 = i),'kwarg1'))

# When an attribute is not found, a fallback error message will stop
# the program from crashing.

for i in polygons:
  print(getattr(Polygon(
    kwarg1 = i,
    kwarg2 = i,
    kwarg3 = i,
    kwarg4 = i),'bogus attribute','Sorry! Attribute not found:'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create some for loop examples with our Polygon class instances.

class Polygon:

  """Polygon"""  # documentation payload/description block

  __slots__ = ('args','kwargs')  # __slots__ optimizes memory and performance

  def __init__(self,*args,**kwargs):  # three parameters

    self.args = args
    self.kwargs = kwargs  # two attribute

print(getattr(Polygon,'__doc__'))

# four explicit argument placeholder values

for i in polygons:
  print(Polygon(i,None,None,None).args[0])  # four explicit argument placeholder values

# or this:

for i in polygons:
  print(getattr(Polygon(i,None,None,None),'args')[0])  # four explicit argument placeholder values

# or this:

for i in polygons:
  print(Polygon(i,i,i,i).args[0])  # four explicit argument placeholder values

# or this:

for i in polygons:
  print(getattr(Polygon(i,i,i,i),'args')[0])  # four explicit argument placeholder values

# four explicit keyword argument placeholder values

for i in polygons:
  print(getattr(Polygon(
    kwarg1 = i,
    kwarg2 = None,
    kwarg3 = None,
    kwarg4 = None),'kwargs').get('kwargs1'))

# When an attribute is not found, a fallback error message will stop
# the program from crashing.

for i in polygons:
  print(getattr(Polygon(
    kwarg1 = i,
    kwarg2 = None,
    kwarg3 = None,
    kwarg4 = None),'kwargs').get('bogus attribute','Sorry! Attribute not found:'))

# or this:

for i in polygons:
  print(getattr(Polygon(
    kwarg1 = i,
    kwarg2 = i,
    kwarg3 = i,
    kwarg4 = i),'kwargs').get('kwargs1'))

# When an attribute is not found, a fallback error message will stop
# the program from crashing.

for i in polygons:
  print(getattr(Polygon(
    kwarg1 = i,
    kwarg2 = i,
    kwarg3 = i,
    kwarg4 = i),'kwargs').get('bogus attribute','Sorry! Attribute not found:'))

# I am almost a complete Walking Human Computer Science Research Laboratory Machine on Two Legs... 😁
