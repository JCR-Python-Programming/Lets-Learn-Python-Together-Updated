

# Here is tuple of values that you can use for your class attribute
# property values. There are 18 tuple values to choose from.

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

  """Polygon"""

  __slots__ = ('polygons1','polygons2','polygons3','polygons4')

  def __init__(self,polygons1,polygons2,polygons3,polygons4):

    self.polygons1 = polygons1
    self.polygons2 = polygons2
    self.polygons3 = polygons3
    self.polygons4 = polygons4  # four explicit attribute properties

print(getattr(Polygon,'__doc__'))

# four explicit argument placeholder values

print(Polygon(polygons[0],polygons[1],polygons[2],polygons[3]).polygons1)

# When an attribute is not found, a fallback error message will stop the program
# from crashing.

print(getattr(Polygon(polygons[0],polygons[1],polygons[2],polygons[3]),'bogus attribute','Sorry! Attribute not found:'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Polygon:

  """Polygon"""

  __slots__ = ('polygons1','polygons2','polygons3','polygons4')

  def __init__(self,polygons1,polygons2,polygons3,polygons4):

    self.polygons1 = polygons[0]
    self.polygons2 = polygons[1]
    self.polygons3 = polygons[2]
    self.polygons4 = polygons[3]  # four implicit attribute properties

print(getattr(Polygon,'__doc__'))

print(Polygon('','','','').polygons1)  # four implicit argument placeholder values

print(getattr(Polygon('','','',''),'polygons1'))  # four implicit argument placeholder values

# or this:

print(Polygon(None,None,None,None).polygons1)  # four implicit argument placeholder values

print(getattr(Polygon(None,None,None,None),'polygons1'))  # four implicit argument placeholder values

# When an attribute is not found, a fallback error message will stop the program
# from crashing.

print(getattr(Polygon(None,None,None,None),'bogus attribute','Sorry! Attribute not found:'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Polygon:

  """Polygon"""

  __slots__ = ('args',)

  def __init__(self,*args):  # two parameters

    self.args = args  # one attribute

print(getattr(Polygon,'__doc__'))

# four explicit argument placeholder values

print(Polygon(polygons[0],polygons[1],polygons[2],polygons[3]).args[0])

print(getattr(Polygon(polygons[0],polygons[1],polygons[2],polygons[3]),'args')[0])

# When an attribute is not found, a fallback error message will stop the program
# from crashing.

print(getattr(Polygon(polygons[0],polygons[1],polygons[2],polygons[3]),'bogus attribute',['Sorry! Attribute not found:'])[0])

 # or this:

print(getattr(Polygon(polygons[0],polygons[1],polygons[2],polygons[3]),'bogus attribute',[''])[0])

# or this:

print(getattr(Polygon(polygons[0],polygons[1],polygons[2],polygons[3]),'bogus attribute',[None])[0])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Polygon:

  """Polygon"""

  __slots__ = ('kwargs',)

  def __init__(self,**kwargs):  # two parameters

    self.kwargs = kwargs  # one attribute

print(getattr(Polygon,'__doc__'))

# four explicit keyword argument placeholder values

print(getattr(Polygon(
  kwargs1 = polygons[0],kwargs2 = polygons[1],
  kwargs3 = polygons[2],kwargs4 = polygons[3]),'kwargs').get('kwargs1'))

# When an attribute is not found, a fallback error message will stop the program
# from crashing.

print(getattr(Polygon(
  kwargs1 = polygons[0],kwargs2 = polygons[1],
  kwargs3 = polygons[2],kwargs4 = polygons[3]),'kwargs').get('bogus attribute','Sorry! Attribute not found:'))

# or this:

print(getattr(Polygon(
  kwargs1 = polygons[0],kwargs2 = polygons[1],
  kwargs3 = polygons[2],kwargs4 = polygons[3]),'kwargs').get('bogus attribute',''))

# or this:

print(getattr(Polygon(
  kwargs1 = polygons[0],kwargs2 = polygons[1],
  kwargs3 = polygons[2],kwargs4 = polygons[3]),'kwargs').get('bogus attribute',None))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Polygon:

  """Polygon"""

  __slots__ = ('__dict__',)

  def __init__(self,**kwargs):

    self.__dict__.update(kwargs)

print(getattr(Polygon,'__doc__'))

# four explicit keyword argument placeholder values

print(getattr(Polygon(
  kwarg1 = polygons[0],
  kwarg2 = polygons[1],
  kwarg3 = polygons[3],
  kwarg4 = polygons[4]),'kwarg1'))

# When an attribute is not found, a fallback error message will stop the program
# from crashing.

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

  """Polygon"""

  __slots__ = ('args','kwargs')

  def __init__(self,*args,**kwargs):  # two parameters

    self.args = args
    self.kwargs = kwargs  # two attribute

print(getattr(Polygon,'__doc__'))

# four explicit argument placeholder values

print(getattr(Polygon(polygons[0],polygons[1],polygons[2],polygons[3]),'args')[0])

# four explicit keyword argument placeholder values

print(getattr(Polygon(
  kwargs1 = polygons[0],kwargs2 = polygons[1],
  kwargs3 = polygons[2],kwargs4 = polygons[3]),'kwargs').get('kwargs1'))

# When an attribute is not found, a fallback error message will stop the program
# from crashing.

print(getattr(Polygon(polygons[0],polygons[1],polygons[2],polygons[3]),'bogus attribute',['Sorry! Attribute not found:'])[0])

# or this:

print(getattr(Polygon(polygons[0],polygons[1],polygons[2],polygons[3]),'bogus attribute',[''])[0])

# or this:

print(getattr(Polygon(polygons[0],polygons[1],polygons[2],polygons[3]),'bogus attribute',[None])[0])

# When an attribute is not found, a fallback error message will stop the program
# from crashing.

print(getattr(Polygon(
  kwargs1 = polygons[0],kwargs2 = polygons[1],
  kwargs3 = polygons[2],kwargs4 = polygons[3]),'kwargs').get('bogus attribute','Sorry! Attribute not found:'))

# or this:

print(getattr(Polygon(
  kwargs1 = polygons[0],kwargs2 = polygons[1],
  kwargs3 = polygons[2],kwargs4 = polygons[3]),'kwargs').get('bogus attribute',''))

# or this:

print(getattr(Polygon(
  kwargs1 = polygons[0],kwargs2 = polygons[1],
  kwargs3 = polygons[2],kwargs4 = polygons[3]),'kwargs').get('bogus attribute',None))

print(getattr(Polygon(polygons[0],polygons[1],polygons[2],polygons[3]),'bogus attribute',[None])[0])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create some instance variables for our print() function.

class Polygon:

  """Polygon"""

  __slots__ = ('polygons1','polygons2','polygons3','polygons4')

  def __init__(self,polygons1,polygons2,polygons3,polygons4):

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

# When an attribute is not found, a fallback error message will stop the program
# from crashing.

print(getattr(instance_var,'bogus attribute','Sorry! Attribute not found:'))

# or this:

print(getattr(instance_var,'bogus attribute',''))

# or this:

print(getattr(instance_var,'bogus attribute',None))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create some instance variables for our print() function.

class Polygon:

  """Polygon"""

  __slots__ = ('polygons1','polygons2','polygons3','polygons4')

  def __init__(self,polygons1,polygons2,polygons3,polygons4):

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

# When an attribute is not found, a fallback error message will stop the program
# from crashing.

print(getattr(instance_var,'bogus attribute','Sorry! Attribute not found:'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create some instance variables for our print() function.

class Polygon:

  """Polygon"""

  __slots__ = ('args',)

  def __init__(self,*args):  # two parameters

    self.args = args  # one attribute

print(getattr(Polygon,'__doc__'))

# four explicit argument placeholder values

instance_var = Polygon(polygons[0],polygons[1],polygons[2],polygons[3])

print(instance_var.args[0])

print(getattr(instance_var,'args')[0])

# When an attribute is not found, a fallback error message will stop the program
# from crashing.

print(getattr(instance_var,'bogus attribute',['Sorry! Attribute not found:'])[0])

 # or this:

print(getattr(instance_var,'bogus attribute',[''])[0])

# or this:

print(getattr(instance_var,'bogus attribute',[None])[0])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create some instance variables for our print() function.

class Polygon:

  """Polygon"""

  __slots__ = ('__dict__',)

  def __init__(self,**kwargs):

    self.__dict__.update(kwargs)

print(getattr(Polygon,'__doc__'))

instance_var = (Polygon(
  kwarg1 = polygons[0],
  kwarg2 = polygons[1],
  kwarg3 = polygons[3],
  kwarg4 = polygons[4]))  #  four explicit keyword argument placeholder values

print(getattr(instance_var,'kwarg1'))

# When an attribute is not found, a fallback error message will stop the program
# from crashing.

print(getattr(instance_var,'bogus attribute','Sorry! Attribute not found:'))

# or this:

print(getattr(instance_var,'bogus attribute',''))

# or this:

print(getattr(instance_var,'bogus attribute',None))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Let's create some instance variables for our print() function.

class Polygon:

  """Polygon"""

  __slots__ = ('kwargs',)

  def __init__(self,**kwargs):  # two parameters

    self.kwargs = kwargs  # one attribute

print(getattr(Polygon,'__doc__'))

instance_var = (Polygon(
  kwargs1 = polygons[0],kwargs2 = polygons[1],
  kwargs3 = polygons[2],kwargs4 = polygons[3]))  # four explicit keyword argument placeholder values

print(getattr(instance_var,'kwargs').get('kwargs3'))

# When an attribute is not found, a fallback error message will stop the program
# from crashing.

print(getattr(instance_var,'kwargs').get('bogus attribute','Sorry! Attribute not found:'))

# or this:

print(getattr(instance_var,'kwargs').get('bogus attribute',''))

# or this:

print(getattr(instance_var,'kwargs').get('bogus attribute',None))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Polygon:

  """Polygon"""

  __slots__ = ('args','kwargs')

  def __init__(self,*args,**kwargs):  # two parameters

    self.args = args
    self.kwargs = kwargs  # two attribute

print(getattr(Polygon,'__doc__'))

instance_var = Polygon(polygons[0],polygons[1],polygons[2],polygons[3])

print(getattr(instance_var,'args')[0])

instance_var = (Polygon(
  kwargs1 = polygons[0],kwargs2 = polygons[1],
  kwargs3 = polygons[2],kwargs4 = polygons[3]))

print(getattr(instance_var,'kwargs').get('kwargs1'))

# When an attribute is not found, a fallback error message will stop the program
# from crashing.

instance_var = Polygon(polygons[0],polygons[1],polygons[2],polygons[3])  # four explicit argument placeholder values

print(getattr(instance_var,'bogus attribute',['Sorry! Attribute not found:'])[0])

# or this:

print(getattr(instance_var,'bogus attribute',[''])[0])

# or this:

print(getattr(instance_var,'bogus attribute',[None])[0])

# When an attribute is not found, a fallback error message will stop the program
# from crashing.

instance_var = (Polygon(
  kwargs1 = polygons[0],kwargs2 = polygons[1],
  kwargs3 = polygons[2],kwargs4 = polygons[3]))  # four explicit keyword argument placeholder values

print(getattr(instance_var,'kwargs').get('bogus attribute','Sorry! Attribute not found:'))

# or this:

print(getattr(instance_var,'kwargs').get('bogus attribute',''))

# or this:

print(getattr(instance_var,'kwargs').get('bogus attribute',None))
