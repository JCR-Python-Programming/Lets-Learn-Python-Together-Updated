class Main:
  def __init__(self,arg1,arg2):

    self.arg1 = arg1
    self.arg2 = arg2

try:
  print(Main('arg1','arg2').arg2)
except AttributeError:
  print('Attribute Error:')
except TypeError:
  print('Type Error:')


class Main:
  def __init__(self,*args):

    self.args = args

try:
  print(Main('arg1','arg2').args[1])
except IndexError:
  print('Index Errror:')


class Main:
  def __init__(self,arg1,arg2):

    self.arg1 = arg1
    self.arg2 = arg2

  def return_args(arg1,arg2):
    return 'arg1','arg2'

Main = Main.return_args('argument placeholder','argument placeholder')

try:
  print(Main[1])
except AttributeError:
  print('Attribute Error:')
except TypeError:
  print('Type Error:')
except IndexError:
  print('Index Error:')


class Main:
  def __init__(self,arg1,arg2):

    self.arg1 = arg1
    self.arg2 = arg2

  def return_self(self):
    return 'arg1','arg2'

  def class_data(self):
    try:
      print(self.arg2)
    except AttributeError:
      print('Attribute Error:')

Main('arg1','arg2').class_data()

try:
  print(Main.return_self('Agument Placeholder Value')[1])
except IndexError:
  print('Index Error:')


class Main:
  def __init__(self,arg1,arg2):

    self.arg1 = arg1
    self.arg2 = arg2

  def return_args(*args):
    return args

Main = Main.return_args('args1','args2','args3','args4','args5')

try:
  print(Main[4])
except IndexError:
  print('Index Error:')


class Main:
  def __init__(self,arg1,arg2):

    self.arg1 = arg1
    self.arg2 = arg2

  def return_keyword_arguments(**kwargs):
    return kwargs

Main = Main.return_keyword_arguments(
  kwargs1 = 'karg1',kwargs2 = 'karg2',
  kwargs3 = 'karg3',kwargs4 = 'karg4'
  )

print(Main.get('kwargs4','Attribute Not Found:'))


class Main:
  def __init__(self,*args):

    self.args = args

  def class_data(self):
    try:
      print(self.args[6])
    except IndexError:
      print('Index Error:')

Main(
  'arg1','arg2','arg3',
  'arg4','arg5','arg6',
  'arg7','arg8','arg9'
  ).class_data()
