class Practice:
  def __init__(self,attribute1,attribute2,attribute3):
    self.attrb1 = attribute1
    self.attrb2 = attribute2
    self.attrb3 = attribute3

print(Practice('attribute1','attribute2','attribute3').attrb1)

class Practice:
  def __init__(self,attribute1,attribute2,attribute3):
    self.attrb1 = 'Attribute One'
    self.attrb2 = 'Attribute Two'
    self.attrb3 = 'Attribute Three'

print(Practice('','','').attrb2)

class Practice:
  def __init__(self,*args):
    self.argsttribute = args

print(Practice('Args One','Args Two','Args Three').argsttribute[0])

class Practice:
  def __init__(self,**kwargs):
    self.kwargsttribute = kwargs

print(Practice(
  kwargs1 = 'Keyword Argument One',
  kwargs2 = 'Keyword Argument Two',
  kwargs3 = 'Keyword Argument Three').kwargsttribute.get('kwargs2','Attribute Not Found:'))

def print_positional_args(*args):

    return 'text value 1','text value 2'

print(print_positional_args('argument placeholder value','argument placeholder value','argument placeholder value')[0])

def print_keyword_args(**kwargs):
   return 'one','two','three.'

try:
    print(print_keyword_args(kwargs1 = 'argument placeholder',kwargs2 = 'argument placeholder')[2])
except (IndexError,TypeError):
    print('Value does not exist:')
