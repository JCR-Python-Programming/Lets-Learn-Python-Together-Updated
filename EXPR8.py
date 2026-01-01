class Main:
  def __init__(self,arg1,arg2):

    self.arg1 = arg1
    self.arg2 = arg2

try:
  print(Main('arg1','arg2').arg2)
except AttributeError:
  print('Attribute Error:')
except NameError:
  print('Name Error:')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  def __init__(self,*args):

    self.args = args

try:
  print(Main('arg1','arg2').args[1])
except NameError:
  print('Name Errror:')
except IndexError:
  print('Index Error:')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  def __init__(self,arg1,arg2):

    self.arg1 = arg1
    self.arg2 = arg2

  def return_args(arg1,arg2):
    return 'arg1','arg2'

Main = Main.return_args(
  'argument placeholder','argument placeholder')

try:
  print(Main[1])
except AttributeError:
  print('Attribute Error:')
except NameError:
  print('Name Error:')
except IndexError:
  print('Index Error:')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  def __init__(self,arg1,arg2):

    self.arg1 = arg1
    self.arg2 = arg2

  def return_self(self):
    return 'arg1','arg2'

  def class_data(self):
    try:
      print(self.arg1)
    except AttributeError:
      print('Attribute Error:')

Main('arg1','arg2').class_data()

try:
  print(Main.return_self('Agument Placeholder Value')[1])
except NameError:
  print('Name Error:')
except IndexError:
  print('Index Error:')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  def __init__(self,arg1,arg2):

    self.arg1 = arg1
    self.arg2 = arg2

  def return_args(*args):
    return args

main = Main.return_args(
  'args1','args2','args3','args4','args5')

try:
  print(main[4])
except NameError:
  print('Name Error:')
except IndexError:
  print('Index Error:')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  def __init__(self,arg1,arg2):

    self.arg1 = arg1
    self.arg2 = arg2

  def return_keyword_args(**kwargs):
    return kwargs

Main = Main.return_keyword_args(
  kwargs1 = 'karg1',kwargs2 = 'karg2',
  kwargs3 = 'karg3',kwargs4 = 'karg4'
  )

print(Main.get('kwargs4','Attribute Not Found:'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  def __init__(self,**kwargs):

    self.args = kwargs

  def return_keyword_args(**kwargs):
    return kwargs

main = Main.return_keyword_args(
  kwargs1 = 'karg1',kwargs2 = 'karg2',
  kwargs3 = 'karg3',kwargs4 = 'karg4'
  )

print(main.get('kwargs4','Attribute Not Found:'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
    def __init__(self,**kwargs):

        self.kwargs = kwargs

class Sub(Main):pass

main = Sub(
  kwargs1 = 'keyword argument1',
  kwargs2 = 'keyword argument2',
  kwargs3 = 'keyword argument3')

print(main.kwargs.get('kwargs3','Attribute Not Found:'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
    def __init__(self,**kwargs):

        self.__dict__.update(kwargs)

class Sub(Main):pass

main = Main(
  kwargs1 = 'keyword argument1',
  kwargs2 = 'keyword argument2',
  kwargs3 = 'keyword argument3')

try:
  print(main.kwargs3)
except AttributeError:
  print('Attribute Error:')
except NameError:
  print('Name Error:')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  def __init__(self,*args):

    self.args = args

  def class_data(self):
    try:
      print(self.args[8])
    except IndexError:
      print('Index Error:')

Main(
  'arg1','arg2','arg3',
  'arg4','arg5','arg6',
  'arg7','arg8','arg9'
  ).class_data()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  def __init__(self,**kwargs):

    self.kwargs = kwargs

  def class_data(self):

    try:
      print(self.kwargs.get('kwargs5','Attribute Not Found:'))
    except IndexError:
      print('Index Error:')

Main(
  kwargs1 = 'karg1',kwargs2 = 'karg2',
  kwargs3 = 'karg3',kwargs4 = 'karg4',
  kwargs5 = 'karg5',kwargs6 = 'karg6',
  kwargs7 = 'karg7',kwargs8 = 'karg8',
  kwargs9 = 'karg9',kwargs10 = 'karg10'
  ).class_data()
