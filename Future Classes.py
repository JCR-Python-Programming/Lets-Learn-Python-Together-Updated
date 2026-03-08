class Main:
  """Class Main"""
  __slots__ = ('__dict__',)
  def __init__(self,*args):

    self.explicit_argument = args

try:
  Main().explicit_argument
except AttributeError:pass

print(getattr(Main('Explicit Argument','Another Explicit Argument'),'explicit_argument')[0])

print(getattr(Main,'__doc__'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  """Class Main"""
  __slots__ = ('__dict__',)
  def __init__(self):

    self.implicit_argument = 'Implicit Argument','Another Implicit Argument'

try:
  Main().implicit_argument
except AttributeError:pass

print(getattr(Main(),'implicit_argument')[0])

print(getattr(Main,'__doc__'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  """Class Main"""
  __slots__ = ('__dict__',)
  def __init__(self, *args):

    self.explicit_argument = args

main = Main('Explicit Argument','Another Explicit Argument')

get_attribute = getattr(main,'explicit_argument','Attribute not found:')

print(get_attribute[0])

print(getattr(Main,'__doc__'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  """Class Main"""
  __slots__ = ('__dict__',)
  def __init__(self):

    self.implicit_argument = 'Implicit Argument','Another Implicit Argument'

get_attribute = getattr(Main(),'implicit_argument','Attribute not found:')

print(get_attribute[0])

print(getattr(Main,'__doc__'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  """Class Main"""
  __slots__ = ('par1','par2','par3')
  def __init__(self,par1,par2,par3):

    self.par1,self.par2,self.par3 = par1,par2,par3

try:
  Main('','','').par1
  Main('','','').par2
  Main('','','').par3
except AttributeError:pass

print(Main('Explicit Argument One','Explicit Argument Two','Explicit Argument Three').par1)

print(getattr(Main,'__doc__'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  """Class Main"""
  __slots__ = ('__dict__',)
  def __init__(self):

    self.par1,self.par2,self.par3 = 'Implicit Argument One','Implicit Argument Two','Implicit Argument Three'

try:
  Main().par1
  Main().par2
  Main().par3
except AttributeError:pass

print(Main().par1)

print(getattr(Main,'__doc__'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
