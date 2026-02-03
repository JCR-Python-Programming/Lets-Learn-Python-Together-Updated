class Main:
  """Class Main"""
  __slots__ = ('arg1','arg2','arg3')
  def __init__(self,arg1,arg2,arg3):

    self.arg1 = arg1
    self.arg2 = arg2
    self.arg3 = arg3

try:
  Main('','','').arg4
except AttributeError:pass

print(getattr(Main('arg1','arg2','arg3'),'arg1'))

print(getattr(Main,'__doc__'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  """Class Main"""
  __slots__ = ('arg1','arg2','arg3')
  def __init__(self,arg1,arg2,arg3):

    self.arg1 = arg1
    self.arg2 = arg2
    self.arg3 = arg3

  def class_datta(self):
    print(self.arg2)

try:
  Main('','','').arg1
except AttributeError:pass

Main('arg1','arg2','arg3').class_datta()

print(getattr(Main,'__doc__'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  """Class Main"""
  __slots__ = ('args')
  def __init__(self,*args):

    self.args = args

try:
  Main('','','').args
except AttributeError:pass

print(Main('arg1','arg2','arg3').args[0])

print(getattr(Main,'__doc__'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  """Class Main"""
  __slots__ = ('arg1','arg2','arg3')
  def __init__(self,arg1,arg2,arg3):

    self.arg1 = arg1
    self.arg2 = arg2
    self.arg3 = arg3

  def return_args(arg1,arg2,arg3):
    return 'arg1','arg2','arg3'

try:
  Main('','','').arg1
except AttributeError:pass

print(Main.return_args(
  'argument placeholder',
  'argument placeholder',
  'argument placeholder')[0])

print(getattr(Main,'__doc__'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  """Class Main"""
  __slots__ = ('arg1','arg2','arg3')
  def __init__(self,arg1,arg2,arg3):

    self.arg1 = arg1
    self.arg2 = arg2
    self.arg3 = arg3

  def return_args(*args):
    return args

try:
  Main('','','').arg1
except AttributeError:pass

print(Main.return_args('args1','args2','args3')[2])

print(getattr(Main,'__doc__'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  """Class Main"""
  __slots__ = ('arg1','arg2','arg3')
  def __init__(self,arg1,arg2,arg3):

    self.arg1 = arg1
    self.arg2 = arg2
    self.arg3 = arg3

  def return_keyword_args(**kwargs):
    return kwargs

try:
  Main('','','').arg1
except AttributeError:pass

print(Main.return_keyword_args(
  kwarg1 = 'karg1',kwarg2 = 'karg2',kwarg3 = 'karg3').get('kwarg3','Attribute Not Found:'))

print(getattr(Main,'__doc__'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  """Class Main"""
  __slots__ = ('kwargs',)
  def __init__(self,**kwargs):

    self.kwargs = kwargs

  def return_keyword_args(**kwargs):
    return kwargs

try:
  Main().kwargs
except AttributeError:pass

print(Main.return_keyword_args(
  kwarg1 = 'karg1',kwarg2 = 'karg2',kwarg3 = 'karg3').get('kwarg3','Attribute Not Found:'))

print(getattr(Main,'__doc__'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  """Class Main"""
  __slots__ = ('kwargs',)
  def __init__(self,**kwargs):

    self.kwargs = kwargs

class Sub(Main):pass

try:
  Main().kwargs
except AttributeError:pass

print(Main(
  kwarg1 = 'keyword argument1',
  kwarg2 = 'keyword argument2',
  kwarg3 = 'keyword argument3').kwargs.get('kwarg3','Attribute Not Found:'))

print(getattr(Main,'__doc__'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  """Class Main"""
  __slots__ = ('kwarg1','kwarg2','kwarg3')
  def __init__(
    self,kwarg1 = 'keyword argeument one',
    kwarg2 = 'keyword argeument two',
    kwarg3 = 'keyword argeument three'):

    self.kwarg1 = kwarg1
    self.kwarg2 = kwarg2
    self.kwarg3 = kwarg3

try:
  Main().kwarg1
except AttributeError:pass

print(getattr(Main(),'kwarg1'))

print(getattr(Main,'__doc__'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  """Class Main"""
  __slots__ = ('kwarg1','kwarg2','kwarg3')
  def __init__(self,kwarg1 = '',kwarg2 = '',kwarg3 = ''):

    self.kwarg1 = 'keyword argeument one'
    self.kwarg2 = 'keyword argeument two'
    self.kwarg3 = 'keyword argeument two'

try:
  Main().kwarg
except AttributeError:pass

print(getattr(Main(),'kwarg1'))

print(getattr(Main,'__doc__'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  """Class Main"""
  __slots__ = ('__dict__',)
  def __init__(self,**kwargs):

    self.__dict__.update(kwargs)

class Sub(Main):pass

try:
  Main().__dict__
except AttributeError:pass

print(getattr(Main(
  kwarg1 = 'keyword argument1',
  kwarg2 = 'keyword argument2',
  kwarg3 = 'keyword argument3'),'kwarg1'))

print(getattr(Main,'__doc__'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  """Class Main"""
  __slots__ = ('args',)
  def __init__(self,*args):

    self.args = args

  def class_datta(self):
    print(self.args[0])

try:
  Main().args
except AttributeError:pass

Main('arg1','arg2','arg3').class_datta()

print(getattr(Main,'__doc__'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  """Class Main"""
  __slots__ = ('kwargs',)
  def __init__(self,**kwargs):

    self.kwargs = kwargs

  def class_datta(self):
    print(self.kwargs.get('kwarg3','Attribute Not Found:'))

try:
  Main().kwargs
except AttributeError:pass

Main(kwarg1 = 'karg1',kwarg2 = 'karg2',kwarg3 = 'karg3').class_datta()

print(getattr(Main,'__doc__'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  """Class Main"""
  __slots__ = ('attribute1','attribute2')
  def __init__(self,attribute1,attribute2):

    self.attribute1 = attribute1
    self.attribute2 = attribute2

  def return_value(variable_value):
    return 'Returned Variable Value from Main.'

class Superclass1(Main):
  def __init__(self,attribute1,attribute2):
    super().__init__(attribute1,attribute2)

class Superclass2(Superclass1):
  __slots__ = ('attribute3','attribute4')
  def __init__(
    self,attribute1,attribute2,attribute3,attribute4):
    super().__init__(attribute1,attribute2)

    self.attribute3 = attribute3
    self.attribute4 = attribute4

try:
  Main('','').attribute1
  Superclass2('','','','').attribute3
except AttributeError:pass

print(getattr(Main(
  'I am the attribute property value of attribute1',
  'I am the attribute property value of attribute2'),'attribute1'))

print(getattr(Superclass1(
  'I am the attribute property value of attribute1',
  'I am the attribute property value of attribute2'),'attribute1'))

print(getattr(Superclass2(
  'I am the attribute property value of attribute1',
  'I am the attribute property value of attribute2',
  'I am the attribute property value of attribute3',
  'I am the attribute property value of attribute4'),'attribute1'))

print(Main.return_value('argument placeholder'))

print(Superclass1.return_value('argument placeholder'))

print(Superclass2.return_value('argument placeholder'))

print(getattr(Main,'__doc__'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  """Class Main"""
  __slots__ = ('args',)
  def __init__(self,*args):

    self.args = args

  def return_value(variable_value):
    return 'Returned Variable Value from Main.'

class Superclass1(Main):
  def __init__(self,*args):
    super().__init__(*args)

    self.args = args

class Superclass2(Superclass1):
  def __init__(self,*args):
    super().__init__(*args)

    self.args = args

try:
  Main('','').args
except AttributeError:print('test')

print(Main(
  'I am the attribute property value of attribute1',
  'I am the attribute property value of attribute2').args[0])

print(Superclass1(
  'I am the attribute property value of attribute1',
  'I am the attribute property value of attribute2').args[0])

print(Superclass2(
  'I am the attribute property value of attribute1',
  'I am the attribute property value of attribute2',
  'I am the attribute property value of attribute3',
  'I am the attribute property value of attribute4').args[0])

print(Main.return_value('argument placeholder'))

print(Superclass1.return_value('argument placeholder'))

print(Superclass2.return_value('argument placeholder'))

print(getattr(Main,'__doc__'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  """Class Main"""
  __slots__ = ('kwargs',)
  def __init__(self,**kwargs):

    self.kwargs = kwargs

  def return_value(variable_value):
    return 'Returned Variable Value from Main.'

class Superclass1(Main):
  def __init__(self,**kwargs):
    super().__init__(**kwargs)

    self.kwargs = kwargs

class Superclass2(Superclass1):
  def __init__(self,**kwargs):
    super().__init__(**kwargs)

    self.kwargs = kwargs

try:
  Main().kwargs
except AttributeError:pass

print(Main(
  kwarg1 = 'I am the attribute property value of attribute1',
  kwarg2 = 'I am the attribute property value of attribute2').kwargs.get('kwarg1','Attribute Not Found:'))

print(Superclass1(
  kwarg1 = 'I am the attribute property value of attribute1',
  kwarg2 = 'I am the attribute property value of attribute2').kwargs.get('kwarg1','Attribute Not Found:'))

print(Superclass2(
  kwarg1 = 'I am the attribute property value of attribute1',
  kwarg2 = 'I am the attribute property value of attribute2',
  kwarg3 = 'I am the attribute property value of attribute3',
  kwarg4 = 'I am the attribute property value of attribute4').kwargs.get('kwarg1','Attribute Not Found:'))

print(Main.return_value('argument placeholder'))

print(Superclass1.return_value('argument placeholder'))

print(Superclass2.return_value('argument placeholder'))

print(getattr(Main,'__doc__'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  """Class Main"""
  __slots__ = ('__dict__',)
  def __init__(self,**kwargs):

    self.__dict__.update(kwargs)

  def return_value(variable_value):
    return 'Returned Variable Value from Main.'

class Superclass1(Main):
  def __init__(self,**kwargs):
    super().__init__(**kwargs)

    self.kwargs = kwargs

class Superclass2(Main):
  def __init__(self,**kwargs):
    super().__init__(**kwargs)

    self.kwargs = kwargs

try:
  Main().__dict__
except AttributeError:pass

print(getattr(Main(
  kwarg1 = 'I am the attribute property value of attribute1',
  kwarg2 = 'I am the attribute property value of attribute2'),'kwarg2'))

print(getattr(Superclass1(
  kwarg1 = 'I am the attribute property value of attribute1',
  kwarg2 = 'I am the attribute property value of attribute2'),'kwarg2'))

print(getattr(Superclass2(
  kwarg1 = 'I am the attribute property value of attribute1',
  kwarg2 = 'I am the attribute property value of attribute2',
  kwarg3 = 'I am the attribute property value of attribute3',
  kwarg4 = 'I am the attribute property value of attribute4'),'kwarg4'))

print(Main.return_value('argument placeholder'))

print(Superclass1.return_value('argument placeholder'))

print(Superclass2.return_value('argument placeholder'))

print(getattr(Main,'__doc__'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  """Main"""
  __slots__ = ('main1','main2','main3')
  def __init__(self,main1,main2,main3):

    self.main1 = main1
    self.main2 = main2
    self.main3 = main3

class Sub_one:
  """Sub_one"""
  __slot__ = ('sub_one1','sub_one2','sub_one3')
  def __init__(self,sub_one1,sub_one2,sub_one3):

    self.sub_one1 = sub_one1
    self.sub_one2 = sub_one2
    self.sub_one3 = sub_one3

class Sub_two:
  """Sub_two"""
  __slot__ = ('sub_two1','sub_two2','sub_two3')
  def __init__(self,sub_two1,sub_two2,sub_two3):

    self.sub_two1 = sub_two1
    self.sub_two2 = sub_two2
    self.sub_two3 = sub_two3

class Sub_three:
  """Sub_three"""
  __slots__ = ('sub_three1','sub_three2','sub_three3')
  def __init__(self,sub_three1,sub_three2,sub_three3):

    self.sub_three1 = sub_three1
    self.sub_three2 = sub_three2
    self.sub_three3 = sub_three3

class Class_all(Main):
  """Class_all"""
  __slots__ = (
      'main1','main2','main3',
      'sub_one1','sub_one2','sub_one3',
      'sub_two1','sub_two2','sub_two3',
      'sub_three1','sub_three2','sub_three3')
  def __init__(
    self,main1,main2,main3,
    sub_one1,sub_one2,sub_one3,
    sub_two1,sub_two2,sub_two3,sub_three1,sub_three2,sub_three3):

    Main.__init__(self,main1,main2,main3)
    Sub_one.__init__(self,sub_one1,sub_one2,sub_one3)
    Sub_two.__init__(self,sub_two1,sub_two2,sub_two3)
    Sub_three.__init__(self,sub_three1,sub_three2,sub_three3)

try:
  Main('','','').main1
  Sub_one('','','').sub_one1
  Sub_two('','','').sub_two1
  Sub_three('','','').sub_three1
  Class_all('','','','','','','','','','','','').main1
except AttributeError:pass

print(getattr(Class_all(
  'Main value1','Main value2','Main value3',
  'Sub_one value1','Sub_one value2','Sub_one value3',
  'Sub_two value1','Sub_two value2','Sub_two value3',
  'Sub_three value1','Sub_three value2','Sub_three value3'),'sub_three3'))

print(getattr(Main,'__doc__'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  """Main"""
  def __init__(self,main1,main2,main3,*args):

    self.main1 = main1
    self.main2 = main2
    self.main3 = main3
    super().__init__(*args)

class Sub_one:
  """Sub_one"""
  def __init__(self,sub_one1,sub_one2,sub_one3,*args):

    self.sub_one1 = sub_one1
    self.sub_one2 = sub_one2
    self.sub_one3 = sub_one3
    super().__init__(*args)

class Sub_two:
  """Sub_two"""
  def __init__(self,sub_two1,sub_two2,sub_two3,*args):

    self.sub_two1 = sub_two1
    self.sub_two2 = sub_two2
    self.sub_two3 = sub_two3
    super().__init__(*args)

class Sub_three:
  """Sub_three"""
  def __init__(self,sub_three1,sub_three2,sub_three3,*args):

    self.sub_three1 = sub_three1
    self.sub_three2 = sub_three2
    self.sub_three3 = sub_three3
    super().__init__(*args)

class Class_all(Main,Sub_one,Sub_two,Sub_three):
  """Class_all"""
  __slots__ = (
      'main1','main2','main3',
      'sub_one1','sub_one2','sub_one3',
      'sub_two1','sub_two2','sub_two3',
      'sub_three1','sub_three2','sub_three3')
  def __init__(
    self,main1,main2,main3,
    sub_one1,sub_one2,sub_one3,
    sub_two1,sub_two2,sub_two3,
    sub_three1,sub_three2,sub_three3):
    super().__init__(
      main1,main2,main3,
      sub_one1,sub_one2,sub_one3,
      sub_two1,sub_two2,sub_two3,
      sub_three1,sub_three2,sub_three3)

try:
  Main('','','').main1
  Sub_one('','','').sub_one1
  Sub_two('','','').sub_two1
  Sub_three('','','').sub_three1
  Class_all('','','','','','','','','','','','').main1
except AttributeError:pass

print(getattr(Class_all(
  'Main value1','Main value2','Main value3',
  'Sub_one value1','Sub_one value2','Sub_one value3',
  'Sub_two value1','Sub_two value2','Sub_two value3',
  'Sub_three value1','Sub_three value2','Sub_three value3'),'sub_three1'))

print(getattr(Main,'__doc__'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  """Main"""
  def __init__(
    self,main1 = '',main2 = '',main3 = '',**kwargs):

    self.main1 = main1
    self.main2 = main2
    self.main3 = main3
    super().__init__(**kwargs)

class Sub_one:
  """Sub_one"""
  def __init__(
    self,sub_one1 = '',sub_one2 = '',sub_one3 = '',**kwargs):

    self.sub_one1 = sub_one1
    self.sub_one2 = sub_one2
    self.sub_one3 = sub_one3
    super().__init__(**kwargs)

class Sub_two:
  """Sub_two"""
  def __init__(
    self,sub_two1 = '',sub_two2 = '',sub_two3 = '',**kwargs):

    self.sub_two1 = sub_two1
    self.sub_two2 = sub_two2
    self.sub_two3 = sub_two3
    super().__init__(**kwargs)

class Sub_three:
  """Sub_two"""
  def __init__(
    self,sub_three1 = '',sub_three2 = '',sub_three3 = '',**kwargs):

    self.sub_three1 = sub_three1
    self.sub_three2 = sub_three2
    self.sub_three3 = sub_three3
    super().__init__(**kwargs)

class Class_all(Main,Sub_one,Sub_two,Sub_three):
  """Class_all"""
  __slots__ = (
      'main1','main2','main3',
      'sub_one1','sub_one2','sub_one3',
      'sub_two1','sub_two2','sub_two3',
      'sub_three1','sub_three2','sub_three3')
  def __init__(
    self,main1,main2,main3,
    sub_one1,sub_one2,sub_one3,
    sub_two1,sub_two2,sub_two3,
    sub_three1,sub_three2,sub_three3):
    super().__init__(
      main1 = main1,main2 = main2,
      main3 = main3,sub_one1 = sub_one1,
      sub_one2 = sub_one2,sub_one3 = sub_one3,
      sub_two1 = sub_two1,sub_two2 = sub_two2,
      sub_two3 = sub_two3,sub_three1 = sub_three1,
      sub_three2 = sub_three2,sub_three3 = sub_three3)

try:
  Main('','','').main1
  Sub_one('','','').sub_one1
  Sub_two('','','').sub_two1
  Sub_three('','','').sub_three1
  Class_all('','','','','','','','','','','','').sub_three1
except AttributeError:pass

print(getattr(Class_all(
  'Main value1','Main value2','Main value3',
  'Sub_one value1','Sub_one value2','Sub_one value3',
  'Sub_two value1','Sub_two value2','Sub_two value3',
  'Sub_three value1','Sub_three value2','Sub_three value3'),'sub_three3'))

print(getattr(Main,'__doc__'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  """Class Main"""

  def __init__(
    self,main1 = '',main2 = '',main3 = '',**kwargs):

    self.main1 = main1
    self.main2 = main2
    self.main3 = main3
    super().__init__(**kwargs)

class Sub_one(Main):
  def __init__(
    self,sub_one1 = '',sub_one2 = '',sub_one3 = '',**kwargs):

    self.sub_one1 = sub_one1
    self.sub_one2 = sub_one2
    self.sub_one3 = sub_one3
    super().__init__(**kwargs)

class Sub_two(Sub_one):
  def __init__(
    self,sub_two1 = '',sub_two2 = '',sub_two3 = '',**kwargs):

    self.sub_two1 = sub_two1
    self.sub_two2 = sub_two2
    self.sub_two3 = sub_two3
    super().__init__(**kwargs)

class Sub_three(Sub_two):
  def __init__(
    self,sub_three1 = '',sub_three2 = '',sub_three3 = '',**kwargs):

    self.sub_three1 = sub_three1
    self.sub_three2 = sub_three2
    self.sub_three3 = sub_three3
    super().__init__(**kwargs)

class Class_all(Sub_three,Sub_two,Sub_one,Main):
  __slots__ = (
      'main1','main2','main3',
      'sub_one1','sub_one2','sub_one3',
      'sub_two1','sub_two2','sub_two3',
      'sub_three1','sub_three2','sub_three3')
  def __init__(
    self,main1,main2,main3,
    sub_one1,sub_one2,sub_one3,
    sub_two1,sub_two2,sub_two3,
    sub_three1,sub_three2,sub_three3):
    super().__init__(
      main1 = main1,main2 = main2,main3 = main3,
      sub_one1 = sub_one1,sub_one2 = sub_one2,sub_one3 = sub_one3,
      sub_two1 = sub_two1,sub_two2 = sub_two2,sub_two3 = sub_two3,
      sub_three1 = sub_three1,sub_three2 = sub_three2,sub_three3 = sub_three3)

try:
  Main('','','').main1
  Sub_one('','','').sub_one1
  Sub_two('','','').sub_two1
  Sub_three('','','').sub_three1
  Class_all('','','','','','','','','','','','').sub_three1
except AttributeError:pass

print(getattr(Class_all(
  'Main value1','Main value2','Main value3',
  'Sub_one value1','Sub_one value2','Sub_one value3',
  'Sub_two value1','Sub_two value2','Sub_two value3',
  'Sub_three value1','Sub_three value2','Sub_three value3'),'sub_three3'))

print(getattr(Main,'__doc__'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  """Main"""
  def __init__(self,**kwargs):

    self.main1 = 'main1'
    self.main2 = 'main2'
    self.main3 = 'main3'

class Sub_one(Main):
  """Sub_one"""
  def __init__(self,**kwargs):

    self.sub_one1 = 'sub_one1'
    self.sub_one2 = 'sub_one2'
    self.sub_one3 = 'sub_one3'
    super().__init__(**kwargs)

class Sub_two(Sub_one):
  """Sub_two"""
  def __init__(self,**kwargs):

    self.sub_two1 = 'sub_two1'
    self.sub_two2 = 'sub_two2'
    self.sub_two3 = 'sub_two3'
    super().__init__(**kwargs)

class Sub_three(Sub_two):
  """Sub_three"""
  def __init__(self,**kwargs):

    self.sub_three1 = 'sub_three1'
    self.sub_three2 = 'sub_three2'
    self.sub_three3 = 'sub_three3'
    super().__init__(**kwargs)

class Class_all(Sub_three,Sub_two,Sub_one,Main):
  """Class_all"""
  __slots__ = (
      'main1','main2','main3',
      'sub_one1','sub_one2','sub_one3',
      'sub_two1','sub_two2','sub_two3',
      'sub_three1','sub_three2','sub_three3')
  def __init__(
    self,main1,main2,main3,
    sub_one1,sub_one2,sub_one3,
    sub_two1,sub_two2,sub_two3,
    sub_three1,sub_three2,sub_three3):
    super().__init__(
      main1 = main1,main2 = main2,main3 = main3,
      sub_one1 = sub_one1,sub_one2 = sub_one2,sub_one3 = sub_one3,
      sub_two1 = sub_two1,sub_two2 = sub_two2,sub_two3 = sub_two3,
      sub_three1 = sub_three1,sub_three2 = sub_three2,sub_three3 = sub_three3)

try:
  Main().main1
  Sub_one().sub_one1
  Sub_two().sub_two1
  Sub_three().sub_three1
  Class_all('','','','','','','','','','','','').sub_three1
except AttributeError:print('test')

print(getattr(Class_all(
  'Main value1','Main value2','Main value3',
  'Sub_one value1','Sub_one value2','Sub_one value3',
  'Sub_two value1','Sub_two value2','Sub_two value3',
  'Sub_three value1','Sub_three value2','Sub_three value3'),'sub_three3'))

print(getattr(Main,'__doc__'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  """Main"""
  def __init__(self,**kwargs):

    self.main1 = 'main1'
    self.main2 = 'main2'
    self.main3 = 'main3'

class Sub_one:
  """Sub_one"""
  def __init__(self,**kwargs):

    self.sub_one1 = 'sub_one1'
    self.sub_one2 = 'sub_one2'
    self.sub_one3 = 'sub_one3'
    super().__init__(**kwargs)

class Sub_two:
  """Sub_two"""
  def __init__(self,**kwargs):

    self.sub_two1 = 'sub_two1'
    self.sub_two2 = 'sub_two2'
    self.sub_two3 = 'sub_two3'
    super().__init__(**kwargs)

class Sub_three:
  """Sub_three"""
  def __init__(self,**kwargs):

    self.sub_three1 = 'sub_three1'
    self.sub_three2 = 'sub_three2'
    self.sub_three3 = 'sub_three3'
    super().__init__(**kwargs)

class Class_all(Sub_three,Sub_two,Sub_one,Main):
  """Class_all"""
  __slots__ = (
      'main1','main2','main3',
      'sub_one1','sub_one2','sub_one3',
      'sub_two1','sub_two2','sub_two3',
      'sub_three1','sub_three2','sub_three3')
  def __init__(
    self,main1,main2,main3,
    sub_one1,sub_one2,sub_one3,
    sub_two1,sub_two2,sub_two3,
    sub_three1,sub_three2,sub_three3):
    super().__init__(
      main1 = main1,main2 = main2,
      main3 = main3,sub_one1 = sub_one1,
      sub_one2 = sub_one2,sub_one3 = sub_one3,
      sub_two1 = sub_two1,sub_two2 = sub_two2,sub_two3 = sub_two3,
      sub_three1 = sub_three1,sub_three2 = sub_three2,sub_three3 = sub_three3)

try:
  Main().main1
  Sub_one().sub_one1
  Sub_two().sub_two1
  Sub_three().sub_three1
  Class_all('','','','','','','','','','','','').sub_three1
except AttributeError:pass

print(getattr(Class_all(
  'Main value1','Main value2','Main value3',
  'Sub_one value1','Sub_one value2','Sub_one value3',
  'Sub_two value1','Sub_two value2','Sub_two value3',
  'Sub_three value1','Sub_three value2','Sub_three value3'),'main3'))

print(getattr(Main,'__doc__'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  """Main"""
  def __init__(
    self,main1 = '',main2 = '',main3 = '',**kwargs):

    self.main1 = main1
    self.main2 = main2
    self.main3 = main3
    super().__init__(**kwargs)

class Sub_one:
  """Sub_one"""
  def __init__(
    self,sub_one1 = '',sub_one2 = '',sub_one3 = '',**kwargs):

    self.sub_one1 = sub_one1
    self.sub_one2 = sub_one2
    self.sub_one3 = sub_one3
    super().__init__(**kwargs)

class Sub_two:
  """Sub_two"""
  def __init__(
    self,sub_two1 = '',sub_two2 = '',sub_two3 = '',**kwargs):

    self.sub_two1 = sub_two1
    self.sub_two2 = sub_two2
    self.sub_two3 = sub_two3
    super().__init__(**kwargs)

class Sub_three:
  """Sub_three"""
  def __init__(
    self,sub_three1 = '',sub_three2 = '',sub_three3 = '',**kwargs):

    self.sub_three1 = sub_three1
    self.sub_three2 = sub_three2
    self.sub_three3 = sub_three3
    super().__init__(**kwargs)

class Class_all(Main,Sub_one,Sub_two,Sub_three):
  """Class_all"""
  __slots__ = (
      'main1','main2','main3',
      'sub_one1','sub_one2','sub_one3',
      'sub_two1','sub_two2','sub_two3',
      'sub_three1','sub_three2','sub_three3')
  def __init__(
    self,main1,main2,main3,
    sub_one1,sub_one2,sub_one3,
    sub_two1,sub_two2,sub_two3,
    sub_three1,sub_three2,sub_three3):
    super().__init__(
      main1 = 'main1',main2 = 'main2',main3 = 'main3',
      sub_one1 = 'sub_one1',sub_one2 = 'sub_one2',sub_one3 = 'sub_one3',
      sub_two1 = 'sub_two1',sub_two2 = 'sub_two2',sub_two3 = 'sub_two3',
      sub_three1 = 'sub_three1',sub_three2 = 'sub_three2',sub_three3 = 'sub_three3')

try:
  Main().main1
  Sub_one().sub_one1
  Sub_two().sub_two1
  Sub_three().sub_three1
  Class_all('','','','','','','','','','','','').sub_three1
except AttributeError:pass

print(getattr(Class_all(
  'Main value1','Main value2','Main value3',
  'Sub_one value1','Sub_one value2','Sub_one value3',
  'Sub_two value1','Sub_two value2','Sub_two value3',
  'Sub_three value1','Sub_three value2','Sub_three value3'),'sub_three3'))

print(getattr(Main,'__doc__'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  """Main"""
  def __init__(
    self,main1 = '',main2 = '',main3 = '',**kwargs):

    self.main1 = main1
    self.main2 = main2
    self.main3 = main3
    super().__init__(**kwargs)

class Sub_one(Main):
  """Sub_one"""
  def __init__(
    self,sub_one1 = '',sub_one2 = '',sub_one3 = '',**kwargs):

    self.sub_one1 = sub_one1
    self.sub_one2 = sub_one2
    self.sub_one3 = sub_one3
    super().__init__(**kwargs)

class Sub_two(Sub_one):
  """Sub_two"""
  def __init__(
    self,sub_two1 = '',sub_two2 = '',sub_two3 = '',**kwargs):

    self.sub_two1 = sub_two1
    self.sub_two2 = sub_two2
    self.sub_two3 = sub_two3
    super().__init__(**kwargs)

class Sub_three(Sub_two):
  """Sub_three"""
  def __init__(
    self,sub_three1 = '',sub_three2 = '',sub_three3 = '',**kwargs):

    self.sub_three1 = sub_three1
    self.sub_three2 = sub_three2
    self.sub_three3 = sub_three3
    super().__init__(**kwargs)

class Class_all(Sub_three,Sub_two,Sub_one,Main):
  """Class_all"""
  __slots__ = (
      'main1','main2','main3',
      'sub_one1','sub_one2','sub_one3',
      'sub_two1','sub_two2','sub_two3',
      'sub_three1','sub_three2','sub_three3')
  def __init__(
    self,main1,main2,main3,
    sub_one1,sub_one2,sub_one3,
    sub_two1,sub_two2,sub_two3,
    sub_three1,sub_three2,sub_three3):
    super().__init__(
      main1 = 'main1',main2 = 'main2',main3 = 'main3',
      sub_one1 = 'sub_one1',sub_one2 = 'sub_one2',sub_one3 = 'sub_one3',
      sub_two1 = 'sub_two1',sub_two2 = 'sub_two2',sub_two3 = 'sub_two3',
      sub_three1 = 'sub_three1',sub_three2 = 'sub_three2',sub_three3 = 'sub_three3')

try:
  Main().main1
  Sub_one().sub_one1
  Sub_two().sub_two1
  Sub_three().sub_three1
  Class_all('','','','','','','','','','','','').sub_three1
except AttributeError:pass

print(getattr(Class_all(
  'Main value1','Main value2','Main value3',
  'Sub_one value1','Sub_one value2','Sub_one value3',
  'Sub_two value1','Sub_two value2','Sub_two value3',
  'Sub_three value1','Sub_three value2','Sub_three value3'),'sub_three3'))

print(getattr(Main,'__doc__'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  """Main"""
  def __init__(self,main1,main2,main3):

    self.main1 = 'main1'
    self.main2 = 'main2'
    self.main3 = 'main3'

class Sub_one:
  """Sub_one"""
  def __init__(self,sub_one1,sub_one2,sub_one3):

    self.sub_one1 = 'sub_one1'
    self.sub_one2 = 'sub_one2'
    self.sub_one3 = 'sub_one3'

class Sub_two:
  """Sub_two"""
  def __init__(self,sub_two1,sub_two2,sub_two3):

    self.sub_two1 = 'sub_two1'
    self.sub_two2 = 'sub_two2'
    self.sub_two3 = 'sub_two3'

class Sub_three:
  """Sub_three"""
  def __init__(self,sub_three1,sub_three2,sub_three3):

    self.sub_three1 = 'sub_three1'
    self.sub_three2 = 'sub_three2'
    self.sub_three3 = 'sub_three3'

class Class_all(Main):
  """Class_all"""
  __slots__ = (
      'main1','main2','main3',
      'sub_one1','sub_one2','sub_one3',
      'sub_two1','sub_two2','sub_two3',
      'sub_three1','sub_three2','sub_three3')
  def __init__(
    self,main1,main2,main3,
    sub_one1,sub_one2,sub_one3,
    sub_two1,sub_two2,sub_two3,
    sub_three1,sub_three2,sub_three3):

    Main.__init__(self,main1,main2,main3)
    Sub_one.__init__(self,sub_one1,sub_one2,sub_one3)
    Sub_two.__init__(self,sub_two1,sub_two2,sub_two3)
    Sub_three.__init__(self,sub_three1,sub_three2,sub_three3)

try:
  Main('','','').main1
  Sub_one('','','').sub_one1
  Sub_two('','','').sub_two1
  Sub_three('','','').sub_three1
  Class_all('','','','','','','','','','','','').main1
except AttributeError:pass

print(getattr(Class_all(
  'argument placeholder value','argument placeholder value',
  'argument placeholder value','argument placeholder value',
  'argument placeholder value','argument placeholder value',
  'argument placeholder value','argument placeholder value',
  'argument placeholder value','argument placeholder value',
  'argument placeholder value','argument placeholder value'),'main1'))

print(getattr(Main,'__doc__'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  """Main"""
  def __init__(self):

    self.main1 = 'main1'
    self.main2 = 'main2'
    self.main3 = 'main2'

class Sub_one():
  """Sub_one"""
  def __init__(self):

    self.sub_one1 = 'sub_one1'
    self.sub_one2 = 'sub_one2'
    self.sub_one3 = 'sub_one3'

class Sub_two():
  """Sub_two"""
  def __init__(self):

    self.sub_two1 = 'sub_two1'
    self.sub_two2 = 'sub_two2'
    self.sub_two3 = 'sub_two3'

class Sub_three():
  """Sub_three"""
  def __init__(self):

    self.sub_three1 = 'sub_three1'
    self.sub_three2 = 'sub_three2'
    self.sub_three3 = 'sub_three3'

class Class_all(Main):
  """Class_all"""
  __slots__ = (
      'main1','main2','main3',
      'sub_one1','sub_one2','sub_one3',
      'sub_two1','sub_two2','sub_two3',
      'sub_three1','sub_three2','sub_three3')
  def __init__(self):
    super().__init__()

    Sub_one.__init__(self)
    Sub_two.__init__(self)

try:
  Main().main1
  Sub_one().sub_one1
  Sub_two().sub_two1
  Sub_three().sub_three1
  Class_all().main1
except AttributeError:pass

print(getattr(Class_all(),'main1'))

print(getattr(Main,'__doc__'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  """Main"""
  def __init__(self,*args):

    self.main1 = 'main1'
    self.main2 = 'main2'
    self.main3 = 'main3'

class Sub_one:
  """Sub_one"""
  def __init__(self,*args):

    self.sub_one1 = 'sub_one1'
    self.sub_one2 = 'sub_one2'
    self.sub_one3 = 'sub_one3'

class Sub_two:
  """Sub_two"""
  def __init__(self,*args):

    self.sub_two1 = 'sub_two1'
    self.sub_two2 = 'sub_two2'
    self.sub_two3 = 'sub_two3'

class Sub_three:
  """Sub_three"""
  def __init__(self,*args):

    self.sub_three1 = 'sub_three1'
    self.sub_three2 = 'sub_three2'
    self.sub_three3 = 'sub_three3'

class Class_all(Main):
  """Class_all"""
  __slots__ = (
      'main1','main2','main3',
      'sub_one1','sub_one2','sub_one3',
      'sub_two1','sub_two2','sub_two3',
      'sub_three1','sub_three2','sub_three3')
  def __init__(
    self,main1,main2,main3,
    sub_one1,sub_one2,sub_one3,
    sub_two1,sub_two2,sub_two3,
    sub_three1,sub_three2,sub_three3):

    Main.__init__(self,main1,main2,main3)
    Sub_one.__init__(self,sub_one1,sub_one2,sub_one3)
    Sub_two.__init__(self,sub_two1,sub_two2,sub_two3)
    Sub_three.__init__(self,sub_three1,sub_three2,sub_three3)

try:
  Main().main1
  Sub_one().sub_one1
  Sub_two().sub_two1
  Sub_three().sub_three1
  Class_all('','','','','','','','','','','','').main1
except AttributeError:pass

print(getattr(Class_all(
  'argument placeholder value','argument placeholder value',
  'argument placeholder value','argument placeholder value',
  'argument placeholder value','argument placeholder value',
  'argument placeholder value','argument placeholder value',
  'argument placeholder value','argument placeholder value',
  'argument placeholder value','argument placeholder value'),'main1'))

print(getattr(Main,'__doc__'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  """Main"""
  def __init__(self,*args):

    self.main1 = 'main1'
    self.main2 = 'main2'
    self.main3 = 'main3'

class Sub_one:
  """Sub_one"""
  def __init__(self,*args):

    self.sub_one1 = 'sub_one1'
    self.sub_one2 = 'sub_one2'
    self.sub_one3 = 'sub_one3'

class Sub_two:
  """Sub_two"""
  def __init__(self,*args):

    self.sub_two1 = 'sub_two1'
    self.sub_two2 = 'sub_two2'
    self.sub_two3 = 'sub_two3'

class Sub_three:
  """Sub_two"""
  def __init__(self,*args):

    self.sub_three1 = 'sub_three1'
    self.sub_three2 = 'sub_three2'
    self.sub_three3 = 'sub_three3'

class Class_all(Main):
  """Class_all"""
  __slots__ = (
      'main1','main2','main3',
      'sub_one1','sub_one2','sub_one3',
      'sub_two1','sub_two2','sub_two3',
      'sub_three1','sub_three2','sub_three3')
  def __init__(self):
    super().__init__()

    Sub_one.__init__(self)
    Sub_two.__init__(self)
    Sub_three.__init__(self)

try:
  Main().main1
  Sub_one().sub_one1
  Sub_two().sub_two1
  Sub_three().sub_three1
  Class_all().main1
except AttributeError:pass

print(getattr(Class_all(),'main1'))

print(getattr(Main,'__doc__'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  """Main"""
  def __init__(self,main1,main2,main3):

    self.main1 = 'main1'
    self.main2 = 'main2'
    self.main3 = 'main3'

class Sub_one(Main):
  """Sub_one"""
  def __init__(self,sub_one1,sub_one2,sub_one3):

    self.sub_one1 = 'sub_one1'
    self.sub_one2 = 'sub_one2'
    self.sub_one3 = 'sub_one3'

class Sub_two(Sub_one):
  """Sub_two"""
  def __init__(self,sub_two1,sub_two2,sub_two3):

    self.sub_two1 = 'sub_two1'
    self.sub_two2 = 'sub_two2'
    self.sub_two3 = 'sub_two3'

class Sub_three(Sub_two):
  """Sub_three"""
  def __init__(self,sub_two1,sub_two2,sub_two3):

    self.sub_three1 = 'sub_three1'
    self.sub_three2 = 'sub_three2'
    self.sub_three3 = 'sub_three3'

class Class_all(Sub_three,Sub_two,Sub_one,Main):
  """Class_all"""
  __slots__ = (
      'main1','main2','main3',
      'sub_one1','sub_one2','sub_one3',
      'sub_two1','sub_two2','sub_two3',
      'sub_three1','sub_three2','sub_three3')
  def __init__(
    self,main1,main2,main3,
    sub_one1,sub_one2,sub_one3,
    sub_two1,sub_two2,sub_two3,
    sub_three1,sub_three2,sub_three3):

    Main.__init__(self,main1,main2,main3)
    Sub_one.__init__(self,sub_one1,sub_one2,sub_one3)
    Sub_two.__init__(self,sub_two1,sub_two2,sub_two3)
    Sub_three.__init__(self,sub_three1,sub_three2,sub_three3)

try:
  Main('','','').main1
  Sub_one('','','').sub_one1
  Sub_two('','','').sub_two1
  Sub_three('','','').sub_three1
  Class_all('','','','','','','','','','','','').main1
except AttributeError:pass

print(getattr(Class_all(
  'argument placeholder value','argument placeholder value',
  'argument placeholder value','argument placeholder value',
  'argument placeholder value','argument placeholder value',
  'argument placeholder value','argument placeholder value',
  'argument placeholder value','argument placeholder value',
  'argument placeholder value','argument placeholder value'),'main1'))

print(getattr(Main,'__doc__'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  """Main"""
  def __init__(self,*args):

    self.main1 = 'main1'
    self.main2 = 'main2'
    self.main3 = 'main3'

class Sub_one(Main):
  """Sub_one"""
  def __init__(self,*args):

    self.sub_one1 = 'sub_one1'
    self.sub_one2 = 'sub_one2'
    self.sub_one3 = 'sub_one3'

class Sub_two(Sub_one):
  """Sub_two"""
  def __init__(self,*args):

    self.sub_two1 = 'sub_two1'
    self.sub_two2 = 'sub_two2'
    self.sub_two3 = 'sub_two3'

class Sub_three(Sub_two):
  """Sub_three"""
  def __init__(self,*args):

    self.sub_three1 = 'sub_three1'
    self.sub_three2 = 'sub_three2'
    self.sub_three3 = 'sub_three3'

class Class_all(Sub_three,Sub_two,Sub_one,Main):
  __slots__ = (
      'main1','main2','main3',
      'sub_one1','sub_one2','sub_one3',
      'sub_two1','sub_two2','sub_two3',
      'sub_three1','sub_three2','sub_three3')
  def __init__(
    self,main1,main2,main3,
    sub_one1,sub_one2,sub_one3,
    sub_two1,sub_two2,sub_two3,
    sub_three1,sub_three2,sub_three3):

    Main.__init__(self,main1,main2,main3)
    Sub_one.__init__(self,sub_one1,sub_one2,sub_one3)
    Sub_two.__init__(self,sub_two1,sub_two2,sub_two3)
    Sub_three.__init__(self,sub_three1,sub_three2,sub_three3)

try:
  Main('','','').main1
  Sub_one('','','').sub_one1
  Sub_two('','','').sub_two1
  Sub_three('','','').sub_three1
  Class_all('','','','','','','','','','','','').main1
except AttributeError:pass

print(getattr(Class_all(
  'argument placeholder value','argument placeholder value',
  'argument placeholder value','argument placeholder value',
  'argument placeholder value','argument placeholder value',
  'argument placeholder value','argument placeholder value',
  'argument placeholder value','argument placeholder value',
  'argument placeholder value','argument placeholder value'),'main1'))

print(getattr(Main,'__doc__'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  """Main"""
  def __init__(self,main1,main2,main3,**kwargs):

    self.main1 = 'main1'
    self.main2 = 'main2'
    self.main3 = 'main3'

class Sub_one:
  """Sub_one"""
  def __init__(self,sub_one1,sub_one2,sub_one3,**kwargs):

    self.sub_one1 = 'sub_one1'
    self.sub_one2 = 'sub_one2'
    self.sub_one3 = 'sub_one3'

class Sub_two:
  """Sub_two"""
  def __init__(self,sub_two1,sub_two2,sub_two3,**kwargs):

    self.sub_two1 = 'sub_two1'
    self.sub_two2 = 'sub_two2'
    self.sub_two3 = 'sub_two3'

class Sub_three:
  """Sub_three"""
  def __init__(self,sub_three1,sub_three2,sub_three3,**kwargs):

    self.sub_three1 = 'sub_three1'
    self.sub_three2 = 'sub_three2'
    self.sub_three3 = 'sub_three3'

class Class_all(Main,Sub_one,Sub_two,Sub_three):
  """Class_all"""
  __slots__ = (
      'main1','main2','main3',
      'sub_one1','sub_one2','sub_one3',
      'sub_two1','sub_two2','sub_two3',
      'sub_three1','sub_three2','sub_three3')
  def __init__(
    self,main1,main2,main3,
    sub_one1,sub_one2,sub_one3,
    sub_two1,sub_two2,sub_two3,
    sub_three1,sub_three2,sub_three3):

    Main.__init__(self,main1 = main1,main2 = main2,main3 = main3)
    Sub_one.__init__(self,sub_one1 = sub_one1,sub_one2 = sub_one2,sub_one3 = sub_one3)
    Sub_two.__init__(self,sub_two1 = sub_two1,sub_two2 = sub_two2,sub_two3 = sub_two3)
    Sub_three.__init__(self,sub_three1 = sub_three1,sub_three2 = sub_three2,sub_three3 = sub_three3)

try:
  Main('','','').main1
  Sub_one('','','').sub_one1
  Sub_two('','','').sub_two1
  Sub_three('','','').sub_three1
  Class_all('','','','','','','','','','','','').main1
except AttributeError:pass

print(getattr(Class_all(
  'argument placeholder value','argument placeholder value',
  'argument placeholder value','argument placeholder value',
  'argument placeholder value','argument placeholder value',
  'argument placeholder value','argument placeholder value',
  'argument placeholder value','argument placeholder value',
  'argument placeholder value','argument placeholder value'),'main1'))

print(getattr(Main,'__doc__'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  """Main"""
  def __init__(self,main1,main2,main3,**kwargs):

    self.main1 = 'main1'
    self.main2 = 'main2'
    self.main3 = 'main3'

class Sub_one(Main):
  """Sub_one"""
  def __init__(self,sub_one1,sub_one2,sub_one3,**kwargs):

    self.sub_one1 = 'sub_one1'
    self.sub_one2 = 'sub_one2'
    self.sub_one3 = 'sub_one3'

class Sub_two(Sub_one):
  """Sub_two"""
  def __init__(self,sub_two1,sub_two2,sub_two3,**kwargs):

    self.sub_two1 = 'sub_two1'
    self.sub_two2 = 'sub_two2'
    self.sub_two3 = 'sub_two3'

class Sub_three(Sub_two):
  """Sub_three"""
  def __init__(self,sub_three1,sub_three2,sub_three3,**kwargs):

    self.sub_three1 = 'sub_three1'
    self.sub_three2 = 'sub_three2'
    self.sub_three3 = 'sub_three3'

class Class_all(Sub_three,Sub_two,Sub_one,Main):
  """Class_all"""
  __slots__ = (
      'main1','main2','main3',
      'sub_one1','sub_one2','sub_one3',
      'sub_two1','sub_two2','sub_two3',
      'sub_three1','sub_three2','sub_three3')
  def __init__(
    self,main1,main2,main3,
    sub_one1,sub_one2,sub_one3,
    sub_two1,sub_two2,sub_two3,
    sub_three1,sub_three2,sub_three3):

    Main.__init__(self,main1 = main1,main2 = main2,main3 = main3)
    Sub_one.__init__(self,sub_one1 = sub_one1,sub_one2 = sub_one2,sub_one3 = sub_one3)
    Sub_two.__init__(self,sub_two1 = sub_two1,sub_two2 = sub_two2,sub_two3 = sub_two3)
    Sub_three.__init__(self,sub_three1 = sub_three1,sub_three2 = sub_three2,sub_three3 = sub_three3)

try:
  Main('','','').main1
  Sub_one('','','').sub_one1
  Sub_two('','','').sub_two1
  Sub_three('','','').sub_three1
  Class_all('','','','','','','','','','','','').main1
except AttributeError:pass

print(getattr(Class_all(
  'argument placeholder value','argument placeholder value',
  'argument placeholder value','argument placeholder value',
  'argument placeholder value','argument placeholder value',
  'argument placeholder value','argument placeholder value',
  'argument placeholder value','argument placeholder value',
  'argument placeholder value','argument placeholder value'),'main1'))

print(getattr(Main,'__doc__'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  """Main"""
  def __init__(self,arg1,arg2,arg3):

    self.arg1 = arg1
    self.arg2 = arg2
    self.arg3 = arg3

  def print_message1():
    print('print_message1')

class Super1(Main):
  def __init__(self,arg1,arg2,arg3,arg4):
    super().__init__(arg1,arg2,arg3)

    self.arg4 = arg4

class Super2(Super1):
  def __init__(self,arg1,arg2,arg3,arg4,arg5):
    super().__init__(arg1,arg2,arg3,arg4)

    self.arg5 = arg5

class Super3(Super2):
  def __init__(self,arg1,arg2,arg3,arg4,arg5,arg6):
    super().__init__(arg1,arg2,arg3,arg4,arg5)

    self.arg6 = arg6

class Super4(Super3):
  def __init__(self,arg1,arg2,arg3,arg4,arg5,arg6,arg7):
    super().__init__(arg1,arg2,arg3,arg4,arg5,arg6)

    self.arg7 = arg7

class Sub_class:
  """Sub_class"""

  def print_message2():
    print('print_message2')

class Class_all(Sub_class,Main):
  """Class_all"""
  __slots__ = ('arg1','arg2','arg3','arg4','arg5','arg6','arg7')

try:
  Class_all('','','').arg1
except AttributeError:pass

getattr(Class_all,'print_message1')()

print(getattr(Main,'__doc__'))

print([cls.__name__ for cls in Super4.mro()])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  """Main"""
  def main():
    print('Main Class Act.')

class Sub_one(Main):
  """Sub_one"""
  def sub1():
    print('Sub One Class Act.')

class Sub_two(Sub_one):
  """Sub_two"""
  def sub2():
    print('Sub Two Class Act.')

class Class_all(Sub_two,Sub_one,Main):
  """Class_all"""

getattr(Class_all,'main')()

print(getattr(Main,'__doc__'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  """Main"""
  def __init__(self,par1,par2,par3):
    self.par1 = par1
    self.par2 = par2
    self.par3 = par3

class Sub_one(Main):
  """Sub_one"""
  def __init__(self,par1,par2,par3):pass

  def __init__(self,par1,par2,par3):
    super().__init__(par1,par2,par3)

class Sub_two(Sub_one):
  """Sub_two"""
  def __init__(self,par1,par2,par3):pass

  def __init__(self,par1,par2,par3):
    super().__init__(par1,par2,par3)

class Class_all(Sub_two,Sub_one,Main):
  """Class_all"""
  __slots__ = ('par1','par2','par3')

try:
  Main('','','').par1
  Sub_one('','','').par1
  Sub_two('','','').par1
  Class_all('','','').par1
except AttributeError:pass

print(getattr(Class_all('Main Class Act.','Sub One Class Act.','Sub Two Class Act.'),'par3'))

print(getattr(Main,'__doc__'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  """Main"""
  __slots__ = ('arg1','arg2','arg3')
  def __init__(self,arg1,arg2,arg3):

    self.arg1 = arg1
    self.arg2 = arg2
    self.arg3 = arg3

try:
  Main('','','').arg1
except AttributeError:pass

print(getattr(Main('arg1','arg2','arg3'),'arg3'))

print(getattr(Main,'__doc__'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  """Main"""
  __slots__ = ('arg1','arg2','arg3')
  def __init__(self):

    self.arg1 = 'arg1'
    self.arg2 = 'arg2'
    self.arg3 = 'arg3'

try:
  Main().arg1
except AttributeError:pass

print(getattr(Main(),'arg1'))

print(getattr(Main,'__doc__'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  """Main"""
  __slots__ = ('arg1','arg2','arg3')
  def __init__(self,arg1,arg2,arg3):

    self.arg1 = arg1
    self.arg2 = arg2
    self.arg3 = arg3

  def return_data(self):
    return self.arg1,self.arg2,self.arg3

try:
  Main('','','').arg1
except AttributeError:pass

print(getattr(Main('arg1','arg2','arg3'),'return_data')()[0])

print(getattr(Main,'__doc__'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  """Main"""
  __slots__ = ('arg1','arg2','arg3')
  def __init__(self):
    self.arg1 = 'arg1'
    self.arg2 = 'arg2'
    self.arg3 = 'arg3'

  def return_data(self):
    return self.arg1,self.arg2,self.arg3

try:
  Main().arg1
except AttributeError:pass

print(getattr(Main(),'return_data')()[0])

print(getattr(Main,'__doc__'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  """Main"""
  __slots__ = ('arg1','arg2','arg3')
  def __init__(self,arg1,arg2,arg3):

    self.arg1 = 'arg1'
    self.arg2 = 'arg2'
    self.arg3 = 'arg3'

  def return_data(self):
    return self.arg1,self.arg2,self.arg3

try:
  Main('','','').arg1
except AttributeError:pass

print(getattr(Main(
  'argument placeholder',
  'argument placeholder',
  'argument placeholder'),'return_data')()[0])

print(getattr(Main,'__doc__'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  """Main"""
  __slots__ = ('arg1','arg2','arg3')
  def __init__(self,arg3):

    self.arg1 = 'arg1'
    self.arg2 = 'arg2'
    self.arg3 = arg3

  def return_args(self):
    return self.arg1,self.arg2,self.arg3

try:
  Main('').arg1
except AttributeError:pass

print(getattr(Main('argument placeholder'),'return_args')()[0])

print(getattr(Main,'__doc__'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  """Main"""
  def __init__(self,arg1,arg2,arg3):

    self.arg1 = arg1
    self.arg2 = arg2
    self.arg3 = arg3

class Sub_one:
  """Sub one"""
  def __init__(self,arg4,arg5,arg6):

    self.arg4 = arg4
    self.arg5 = arg5
    self.arg6 = arg6

class Sub_two:
  """Sub two"""
  def __init__(self,arg7,arg8,arg9):

    self.arg7 = arg7
    self.arg8 = arg8
    self.arg9 = arg9

class Sub_three:
  """Sub three"""
  def __init__(self,arg10,arg11,arg12):

    self.arg10 = arg10
    self.arg11 = arg11
    self.arg12 = arg12

class Class_all(Main):
  """Class_all"""
  __slots__ = (
    'arg1','arg2','arg3','arg4','arg5','arg6',
    'arg7','arg8','arg9','arg10','arg11','arg12')
  def __init__(
    self,arg1,arg2,arg3,arg4,arg5,arg6,
    arg7,arg8,arg9,arg10,arg11,arg12):

    Main.__init__(self,arg1,arg2,arg3)
    Sub_one.__init__(self,arg4,arg5,arg6)
    Sub_two.__init__(self,arg7,arg8,arg9)
    Sub_three.__init__(self,arg10,arg11,arg12)

try:
  Main('','','').arg1
  Sub_one('','','').arg4
  Sub_two('','','').arg7
  Sub_three('','','').arg10
  Class_all('','','','','','','','','','','','').arg12
except AttributeError:pass

print(getattr(Class_all(
  'arg1','arg2','arg3','arg4','arg5','arg6',
  'arg7','arg8','arg9','arg10','arg11','arg12'),'arg12'))

print(getattr(Class_all,'__doc__'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  """Main"""
  def __init__(self,arg1,arg2):

    self.arg1 = arg1
    self.arg2 = arg2

class Sub_one(Main):
  """Sub one"""
  def __init__(self,arg3,arg4):

    self.arg3 = arg3
    self.arg4 = arg4

class Sub_two(Sub_one):
  """Sub two"""
  def __init__(self,arg5,arg6):

    self.arg5 = arg5
    self.arg6 = arg6

class Sub_three(Sub_two):
  """Sub three"""
  def __init__(self,arg7,arg8):

    self.arg7 = arg7
    self.arg8 = arg8

class Class_all(Sub_three,Sub_two,Sub_one,Main):
  """Class_all"""
  __slots__ = ('arg1','arg2','arg3','arg4','arg5','arg6','arg7','arg8')
  def __init__(self,arg1,arg2,arg3,arg4,arg5,arg6,arg7,arg8):

    Main.__init__(self,arg1,arg2)
    Sub_one.__init__(self,arg3,arg4)
    Sub_two.__init__(self,arg5,arg6)
    Sub_three.__init__(self,arg7,arg8)

try:
  Main('','').arg1
  Sub_one('','').arg3
  Sub_two('','').arg5
  Sub_three('','').arg7
  Class_all('','','','','','','','').arg8
except AttributeError:pass

print(getattr(Class_all(
  'Explicit one','Explicit two','Explicit three','Explicit four',
  'Explicit five','Explicit six','Explicit seven','Explicit eight'),'arg1'))

print(getattr(Class_all,'__doc__'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  """Main"""
  def __init__(self):

    self.arg1 = 'arg1'
    self.arg2 = 'arg2'

class Sub_one:
  """Sub one"""
  def __init__(self):

    self.arg3 = 'arg3'
    self.arg4 = 'arg4'

class Sub_two:
  """Sub two"""
  def __init__(self):

    self.arg5 = 'arg5'
    self.arg6 = 'arg6'

class Sub_three:
  """Sub three"""
  def __init__(self):

    self.arg7 = 'arg7'
    self.arg8 = 'arg8'

class Class_all(Main):
  """Class_all"""
  __slots__ = ('arg1','arg2','arg3','arg4','arg5','arg6','arg7','arg8')
  def __init__(self,arg1,arg2,arg3,arg4,arg5,arg6,arg7,arg8):

    Main.__init__(self)
    Sub_one.__init__(self)
    Sub_two.__init__(self)
    Sub_three.__init__(self)

try:
  Main().arg1
  Sub_one().arg3
  Sub_two().arg5
  Sub_three().arg7
  Class_all('','','','','','','','')
except AttributeError:pass

print(getattr(Class_all(
  'argument placeholder','argument placeholder',
  'argument placeholder','argument placeholder',
  'argument placeholder','argument placeholder',
  'argument placeholder','argument placeholder'),'arg8'))

print(getattr(Class_all,'__doc__'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  """Main"""
  def __init__(self):

    self.arg1 = 'arg1'
    self.arg2 = 'arg2'

class Sub_one(Main):
  """Sub one"""
  def __init__(self):

    self.arg3 = 'arg3'
    self.arg4 = 'arg4'

class Sub_two(Sub_one):
  """Sub one"""
  def __init__(self):

    self.arg5 = 'arg5'
    self.arg6 = 'arg6'

class Sub_three(Sub_two):
  """Sub one"""
  def __init__(self):

    self.arg7 = 'arg7'
    self.arg8 = 'arg8'

class Class_all(Sub_three,Sub_two,Sub_one,Main):
  """Class_all"""
  __slots__ = ('arg1','arg2','arg3','arg4','arg5','arg6','arg7','arg8')
  def __init__(self,arg1,arg2,arg3,arg4,arg5,arg6,arg7,arg8):

    Main.__init__(self)
    Sub_one.__init__(self)
    Sub_two.__init__(self)
    Sub_three.__init__(self)

try:
  Main().arg1
  Sub_one().arg3
  Sub_two().arg5
  Sub_three().arg7
  Class_all('','','','','','','','').arg8
except AttributeError:pass

print(getattr(Class_all(
  'argument placeholder','argument placeholder',
  'argument placeholder','argument placeholder',
  'argument placeholder','argument placeholder',
  'argument placeholder','argument placeholder'),'arg8'))

print(getattr(Class_all,'__doc__'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  """Main"""
  def __init__(self,main1 = '',main2 = '',main3 = ''):

    self.main_explicit_value_1 = main1
    self.main_explicit_value_2 = main2
    self.main_explicit_value_3 = main3

class Sub_one:
  """Sub one"""
  def __init__(self,sub_one1 = '',sub_one2 = '',sub_one3 = ''):

    self.sub_one_explicit_value_1 = sub_one1
    self.sub_one_explicit_value_2 = sub_one2
    self.sub_one_explicit_value_3 = sub_one3

class Sub_two:
  """Sub two"""
  def __init__(self,sub_two1 = '',sub_two2 = '',sub_two3 = ''):

    self.sub_two_explicit_value_1 = sub_two1
    self.sub_two_explicit_value_2 = sub_two2
    self.sub_two_explicit_value_3 = sub_two3

class Sub_three:
  """Sub three"""
  def __init__(self,sub_three1 = '',sub_three2 = '',sub_three3 = ''):

    self.sub_three_explicit_value_1 = sub_three1
    self.sub_three_explicit_value_2 = sub_three2
    self.sub_three_explicit_value_3 = sub_three3

class Class_all(Main):
  """Class all"""
  __slots__ = (
    'main_explicit_value_1','main_explicit_value_2','main_explicit_value_3',
    'sub_one_explicit_value_1','sub_one_explicit_value_2','sub_one_explicit_value_3'
    'sub_two_explicit_value_1','sub_two_explicit_value_2','sub_two_explicit_value_3',
    'sub_three_explicit_value_1','sub_three_explicit_value_2','sub_three_explicit_value_3')
  def __init__(
    self,main_explicit_value_1,main_explicit_value_2,main_explicit_value_3,
    sub_one_explicit_value_1,sub_one_explicit_value_2,sub_one_explicit_value_3,
    sub_two_explicit_value_1,sub_two_explicit_value_2,sub_two_explicit_value_3,
    sub_three_explicit_value_1,sub_three_explicit_value_2,sub_three_explicit_value_3):

    Main.__init__(self,main_explicit_value_1,main_explicit_value_2,main_explicit_value_3)
    Sub_one.__init__(self,sub_one_explicit_value_1,sub_one_explicit_value_2,sub_one_explicit_value_3)
    Sub_two.__init__(self,sub_two_explicit_value_1,sub_two_explicit_value_2,sub_two_explicit_value_3)
    Sub_three.__init__(self,sub_three_explicit_value_1,sub_three_explicit_value_2,sub_three_explicit_value_3)

try:
  Main().main_explicit_value_1
  Sub_one().sub_one_explicit_value_1
  Sub_two().sub_two_explicit_value_1
  Sub_three().sub_three_explicit_value_1
  Class_all('','','','','','','','','','','','').sub_three_explicit_value_1
except AttributeError:pass

print(getattr(Class_all(
  'Main explicit value 1','Main explicit value 2','Main explicit value 3',
  'Sub one explicit value 1','Sube one explicit value 2','Sube one explicit value 3',
  'Sub two explicit value 1','Sub two explicit value 2','Sub two explicit value 3',
  'Sub three explicit value 1','Sub three explicit value 2','Sub three explicit value 3'),'main_explicit_value_1'))

print(getattr(Class_all,'__doc__'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  """Main"""
  def __init__(self,main1 = '',main2 = '',main3 = ''):

    self.main_explicit_value_1 = main1
    self.main_explicit_value_2 = main2
    self.main_explicit_value_3 = main3

class Sub_one(Main):
  """Sub one"""
  def __init__(self,sub_one1 = '',sub_one2 = '',sub_one3 = ''):

    self.sub_one_explicit_value_1 = sub_one1
    self.sub_one_explicit_value_2 = sub_one2
    self.sub_one_explicit_value_3 = sub_one3

class Sub_two(Sub_one):
  """Sub two"""
  def __init__(self,sub_two1 = '',sub_two2 = '',sub_two3 = ''):

    self.sub_two_explicit_value_1 = sub_two1
    self.sub_two_explicit_value_2 = sub_two2
    self.sub_two_explicit_value_3 = sub_two3

class Sub_three(Sub_two):
  """Sub three"""
  def __init__(self,sub_three1 = '',sub_three2 = '',sub_three3 = ''):

    self.sub_three_explicit_value_1 = sub_three1
    self.sub_three_explicit_value_2 = sub_three2
    self.sub_three_explicit_value_3 = sub_three3

class Class_all(Sub_three,Sub_two,Sub_one,Main):
  """Class all"""
  __slots__ = (
    'main_explicit_value_1','main_explicit_value_2','main_explicit_value_3',
    'sub_one_explicit_value_1','sub_one_explicit_value_2','sub_one_explicit_value_3'
    'sub_two_explicit_value_1','sub_two_explicit_value_2','sub_two_explicit_value_3',
    'sub_three_explicit_value_1','sub_three_explicit_value_2','sub_three_explicit_value_3')
  def __init__(
    self,main_explicit_value_1,main_explicit_value_2,main_explicit_value_3,
    sub_one_explicit_value_1,sub_one_explicit_value_2,sub_one_explicit_value_3,
    sub_two_explicit_value_1,sub_two_explicit_value_2,sub_two_explicit_value_3,
    sub_three_explicit_value_1,sub_three_explicit_value_2,sub_three_explicit_value_3):

    Main.__init__(self,main_explicit_value_1,main_explicit_value_2,main_explicit_value_3)
    Sub_one.__init__(self,sub_one_explicit_value_1,sub_one_explicit_value_2,sub_one_explicit_value_3)
    Sub_two.__init__(self,sub_two_explicit_value_1,sub_two_explicit_value_2,sub_two_explicit_value_3)
    Sub_three.__init__(self,sub_three_explicit_value_1,sub_three_explicit_value_2,sub_three_explicit_value_3)

try:
  Main().main_explicit_value_1
  Sub_one().sub_one_explicit_value_1
  Sub_two().sub_two_explicit_value_1
  Sub_three().sub_three_explicit_value_1
  Class_all('','','','','','','','','','','','').sub_three_explicit_value_1
except AttributeError:pass

print(getattr(Class_all(
  'Main explicit value 1','Main explicit value 2','Main explicit value 3',
  'Sub one explicit value 1','Sube one explicit value 2','Sube one explicit value 3',
  'Sub two explicit value 1','Sub two explicit value 2','Sub two explicit value 3',
  'Sub three explicit value 1','Sub three explicit value 2','Sub three explicit value 3'),'main_explicit_value_1'))

print(getattr(Class_all,'__doc__'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  """Main"""
  def __init__(self):

    self.main1 = 'Main implicit value 1'
    self.main2 = 'Main implicit value 2'
    self.main3 = 'Main implicit value 3'

class Sub_one:
  """Sub one"""
  def __init__(self):

    self.sub_one1 = 'Sub one implicit value 1'
    self.sub_one2 = 'Sub one implicit value 2'
    self.sub_one3 = 'Sub one implicit value 3'

class Sub_two:
  """Sub two"""
  def __init__(self):

    self.sub_two1 = 'Sub two implicit value 1'
    self.sub_two2 = 'Sub two implicit value 2'
    self.sub_two3 = 'Sub two implicit value 3'

class Sub_three:
  """Sub three"""
  def __init__(self):

    self.sub_three1 = 'Sub three implicit value 1'
    self.sub_three2 = 'Sub three implicit value 2'
    self.sub_three3 = 'Sub three implicit value 3'

class Class_all(Main):
  """Class all"""
  __slots__ = (
    'main1','main2','main3',
    'sub_one1','sub_one2','sub_one3',
    'sub_two1','sub_two2','sub_two3',
    'sub_three1','sub_three2','sub_three3')
  def __init__(
    self,main1,main2,main3,
    sub_one1,sub_one2,sub_one3,
    sub_two1,sub_two2,sub_two3,
    sub_three1,sub_three2,sub_three3):

    Main.__init__(self)
    Sub_one.__init__(self)
    Sub_two.__init__(self)
    Sub_three.__init__(self)

try:
  Main().main1
  Sub_one().sub_one1
  Sub_two().sub_two1
  Sub_three().sub_three1
  Class_all('','','','','','','','','','','','').sub_three1
except AttributeError:pass

print(getattr(Class_all(
  'argument placeholder','argument placeholder',
  'argument placeholder','argument placeholder',
  'argument placeholder','argument placeholder',
  'argument placeholder','argument placeholder',
  'argument placeholder','argument placeholder',
  'argument placeholder','argument placeholder'),'sub_three1'))

print(getattr(Class_all,'__doc__'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Computer:
  """Computer"""
  __slots__ = ('computer',)
  def __init__(self,computer):

    self.computer = computer

class Science(Computer):
  """Science"""
  __slots__ = ('science',)
  def __init__(self,science):

    self.science = science

class Class_all(Science,Computer):
  """Class_all"""
  __slots__ = ()
  def __init__(self,computer,science):

    Computer.__init__(self,computer)
    Science.__init__(self,science)

try:
  Computer('').compter
  Science('').science
  Class_all('').compter
except AttributeError:pass

print(getattr(Computer('Computer'),'computer'))
print(getattr(Science('Science'),'science'))

print(getattr(Class_all('Computer','Science'),'computer'))
print(getattr(Class_all('Computer','Science'),'science'))

print(getattr(Class_all,'__doc__'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Computer:
  """Computer"""
  __slots__ = ('computer',)
  def __init__(self,computer):

    self.computer = 'Computer'

class Science(Computer):
  """Science"""
  __slots__ = ('science',)
  def __init__(self,science):

    self.science = 'Science'

class Class_all(Science,Computer):
  """Class_all"""
  __slots__ = ()
  def __init__(self,computer,science):

    Computer.__init__(self,computer)
    Science.__init__(self,science)

try:
  Computer('').compter
  Science('').science
  Class_all('').compter
except AttributeError:pass

print(getattr(Computer(''),'computer'))
print(getattr(Science(''),'science'))

print(getattr(Class_all('',''),'computer'))
print(getattr(Class_all('',''),'science'))

print(getattr(Class_all,'__doc__'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Computer:
  """Computer"""
  __slots__ = ('computer',)
  def __init__(self,computer):

    self.computer = 'Computer'

class Science(Computer):
  """Science"""
  __slots__ = ('science',)
  def __init__(self,science):

    self.science = science

class Class_all(Science,Computer):
  """Class_all"""
  __slots__ = ()
  def __init__(self,computer,science):

    Computer.__init__(self,computer)
    Science.__init__(self,science)

try:
  Computer('').compter
  Science('').science
  Class_all('').compter
except AttributeError:pass

print(getattr(Computer(''),'computer'))
print(getattr(Science('Science'),'science'))

print(getattr(Class_all('','Science'),'computer'))
print(getattr(Class_all('','Science'),'science'))

print(getattr(Class_all,'__doc__'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Computer:
  """Computer"""
  __slots__ = ('computer',)
  def __init__(self,computer):

    self.computer = computer

class Science(Computer):
  """Science"""
  __slots__ = ('science',)
  def __init__(self,science):

    self.science = 'Science'

class Class_all(Science,Computer):
  """Class_all"""
  __slots__ = ()
  def __init__(self,computer,science):

    Computer.__init__(self,computer)
    Science.__init__(self,science)

try:
  Computer('').compter
  Science('').science
  Class_all('').compter
except AttributeError:pass

print(getattr(Computer('Computer'),'computer'))
print(getattr(Science(''),'science'))

print(getattr(Class_all('Computer',''),'computer'))
print(getattr(Class_all('Computer',''),'science'))

print(getattr(Class_all,'__doc__'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  """Main"""
  __slots__ = ('main',)
  def __init__(self,main = ''):

    self.main = main

class Sub_one:
  """Sub_one"""
  __slots__ = ('sub_one',)
  def __init__(self,sub_one = ''):

    self.sub_one = sub_one

class Class_all(Main):
  """Class_all"""
  __slots__ = ('main','sub_one')
  def __init__(self,main,sub_one):

    Main.__init__(self,main = main)
    Sub_one.__init__(self,sub_one = sub_one)

try:
  Main('').main
  Sub_one('').sub_one
  Class_all('','').main
except AttributeError:pass

print(getattr(Main('Main value'),'main'))
print(getattr(Sub_one('Sub_one value'),'sub_one'))

print(getattr(Class_all('Main value','Sub_one'),'main'))
print(getattr(Class_all('Main','Sub_one value'),'sub_one'))

print(getattr(Class_all,'__doc__'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  """Main"""
  __slots__ = ('main',)
  def __init__(self,main = ''):

    self.main = main

class Sub_one(Main):
  """Sub_one"""
  __slots__ = ('sub_one',)
  def __init__(self,sub_one = ''):

    self.sub_one = sub_one

class Class_all(Sub_one,Main):
  """Class_all"""
  __slots__ = ('main','sub_one')
  def __init__(self,main,sub_one):

    Sub_one.__init__(self,sub_one = sub_one)
    Main.__init__(self,main = main)

try:
  Main('').main
  Sub_one('').sub_one
  Class_all('','').main
except AttributeError:pass

print(getattr(Main('Main value'),'main'))
print(getattr(Sub_one('Sub_one value'),'sub_one'))

print(getattr(Class_all('Main value','Sub_one'),'main'))
print(getattr(Class_all('Main','Sub_one value'),'sub_one'))

print(getattr(Class_all,'__doc__'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  """Main"""
  __slots__ = ('main',)
  def __init__(self,main = ''):

    self.main = 'Main value'

class Sub_one(Main):
  """Sub_one"""
  __slots__ = ('sub_one',)
  def __init__(self,sub_one = ''):

    self.sub_one = 'Sub_one value'

class Class_all(Sub_one,Main):
  """Class_all"""
  __slots__ = ('main','sub_one')
  def __init__(self,main,sub_one):

    Sub_one.__init__(self,sub_one = sub_one)
    Main.__init__(self,main = main)

try:
  Main('').main
  Sub_one('').sub_one
  Class_all('','').main
except AttributeError:pass

print(getattr(Main(''),'main'))
print(getattr(Sub_one(''),'sub_one'))

print(getattr(Class_all('',''),'main'))
print(getattr(Class_all('',''),'sub_one'))

print(getattr(Class_all,'__doc__'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  """Main"""
  __slots__ = ('main',)
  def __init__(self,main = '',**kwargs):

    self.main = main
    super().__init__(**kwargs)

class Sub_one(Main):
  """Sub_one"""
  __slots__ = ('sub_one',)
  def __init__(self,sub_one = '',**kwargs):

    self.sub_one = sub_one
    super().__init__(**kwargs)

class Class_all(Sub_one,Main):
  """Class_all"""
  __slots__ = ('main','sub_one')
  def __init__(self,main,sub_one):
    super().__init__(main = main,sub_one = sub_one)

try:
  Main('').main
  Sub_one('').sub_one
  Class_all('','').main
except AttributeError:pass

print(getattr(Main('Main value'),'main'))
print(getattr(Sub_one('Sub_one value'),'sub_one'))

print(getattr(Class_all('Main value','Sub_one'),'main'))
print(getattr(Class_all('Main','Sub_one value'),'sub_one'))

print(getattr(Class_all,'__doc__'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  """Main"""
  __slots__ = ('main',)
  def __init__(self,main = '',**kwargs):

    self.main = 'Main value'
    super().__init__(**kwargs)

class Sub_one(Main):
  """Sub_one"""
  __slots__ = ('sub_one',)
  def __init__(self,sub_one = '',**kwargs):

    self.sub_one = 'Sub_one value'
    super().__init__(**kwargs)

class Class_all(Sub_one,Main):
  """Class_all"""
  __slots__ = ('main','sub_one')
  def __init__(self,main,sub_one):
    super().__init__(main = main,sub_one = sub_one)

try:
  Main('').main
  Sub_one('').sub_one
  Class_all('','').main
except AttributeError:pass

print(getattr(Main(''),'main'))
print(getattr(Sub_one(''),'sub_one'))

print(getattr(Class_all('',''),'main'))
print(getattr(Class_all('',''),'sub_one'))

print(getattr(Class_all,'__doc__'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  """Main"""
  __slots__ = ('main1','main2','main3')
  def __init__(self,main1 = '',main2 = '',main3 = ''):

    self.main1 = main1
    self.main2 = main2
    self.main3 = main3

class Sub_one:
  """Sub_one"""
  __slots__ = ('sub_one1','sub_one2','sub_one3')
  def __init__(self,sub_one1 = '',sub_one2 = '',sub_one3 = ''):

    self.sub_one1 = sub_one1
    self.sub_one2 = sub_one2
    self.sub_one3 = sub_one3

class Class_all(Main):
  """Class_all"""
  __slots__ = ('main1','main2','main3','sub_one1','sub_one2','sub_one3')
  def __init__(
    self,main1,main2,main3,
    sub_one1,sub_one2,sub_one3):

    Main.__init__(self,main1 = main1,main2 = main2,main3 = main3)
    Sub_one.__init__(self,sub_one1 = sub_one1,sub_one2 = sub_one2,sub_one3 = sub_one3)

try:
  Main('','','').main1
  Sub_one('','','').sub_one1
  Class_all('','','','','','').main1
except AttributeError:pass

print(getattr(Main('main1 value','main2 value','main3 value'),'main1'))
print(getattr(Sub_one('sub_one1 value','sub_one2 value','sub_one3 value'),'sub_one1'))

print(getattr(Class_all(
  'main1 value','main2 value','main3 value',
  'sub_one1 value','sub_one2 value','sub_one3 value'),'main1'))
print(getattr(Class_all(
  'main1 value','main2 value','main3 value',
  'sub_one1 value','sub_one2 value','sub_one3 value'),'sub_one1'))

print(getattr(Class_all,'__doc__'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  """Main"""
  __slots__ = ('main1','main2','main3')
  def __init__(self):

    self.main1 = 'main1 value'
    self.main2 = 'main2 value'
    self.main3 = 'main3 value'

class Sub_one:
  """Sub_one"""
  __slots__ = ('sub_one1','sub_one2','sub_one3')
  def __init__(self):

    self.sub_one1 = 'sub_one1 value'
    self.sub_one2 = 'sub_one2 value'
    self.sub_one3 = 'sub_one3 value'

class Class_all(Main):
  """Class_all"""
  __slots__ = (
    'main1','main2','main3',
    'sub_one1','sub_one2','sub_one3')
  def __init__(self):

    Main.__init__(self)
    Sub_one.__init__(self)

try:
  Main.main1
  Sub_one.sub_one1
  Class_all.main1
except AttributeError:pass

print(getattr(Main(),'main1'))
print(getattr(Sub_one(),'sub_one1'))

print(getattr(Class_all(),'main1'))
print(getattr(Class_all(),'sub_one1'))

print(getattr(Class_all,'__doc__'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
first = 'John'
last = 'Smith'

class Name:
  """Name"""
  __slots__ = ('first','last')
  def __init__(self,first,last):

    self.first = first
    self.last = last

try:
  Name('','').first
except AttributeError:pass

print(getattr(Name(first,last),'first'))

print(getattr(Name,'__doc__'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Name:
  """Name"""
  __slots__ = ('_first','_last')
  def __init__(self,first,last):
    self._first = first
    self._last = last

  @property
  def first(self):
    return self._first

  @property
  def last(self):
    return self._last

  @first.setter
  def first(self,first):
    self._first = first

  @last.setter
  def last(self,last):
    self._last = last

  def __repr__(self):
    full_name1 = str(self.first),str(self.last)
    full_name2 = str(self.first)+str(self.last)
    return str(len(full_name2))

  @first.deleter
  def first(self):
    del self._first
    print('first name is deleted:')

  @last.deleter
  def last(self):
    del self._last
    print('last name is deleted:')

name = Name('Jane','Doe')
name.first = 'John'
name.last = 'Smith'

try:
  Name('','').first
except AttributeError:pass

print(getattr(name,'first'),getattr(name,'last'))

print(getattr(Name,'__doc__'))

print(name)

del Name('','').first
del Name('','').last
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
RGB = (
  '\033[38;2;255;0;0m',  # index 0 = red
  '\033[38;2;255;255;0m',  # index 1 = yellow
  '\033[38;2;0;0;255m',  # index 2 = blue
  '\033[38;2;0;255;0m',  # index 3 = green
  '\033[38;2;255;0;255m',  # index 4 = pink
  '\033[38;2;0;255;255m',  # index 5 = cyan
  '\033[38;2;255;255;255m')  # index 6 = white

colour_name = (
  RGB[0]+'A red',  # index 0 = colour name red
  RGB[1]+'A yellow',  # index 1 = colour name yellow
  RGB[2]+'A blue',  # index 2 = colour name blue
  RGB[3]+'A green',  # index 3 = colour name green
  RGB[4]+'A pink',  # index 4 = colour name pink
  RGB[5]+'A cyan',  # index 5 = colour name cyan
  RGB[6]+'A white')  # index 6 = colour name white

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

sides = (
  'has three equal sides.',  # index[0]
  'has four equal sides.',  # index[1]
  'has five equal sides.',  # index[2]
  'has six equal sides.',  # index[3]
  'has seven equal sides.',  # index[4]
  'has eight equal sides.',  # index[5]
  'has nine equal sides.',  # index[6]
  'has ten equal sides.',  # index[7]
  'has eleven equal sides.',  # index[8]
  'has twelve equal sides.',  # index[9]
  'has thirteen equal sides.',  # index[10]
  'has fourteen equal sides.',  # index[11]
  'has fifteen equal sides.',  # index[12]
  'has sixteen equal sides.',  # index[13]
  'has seventeen equal sides.',  # index[14]
  'has eighteen equal sides.',  # index[15]
  'has nineteen equal sides.',  # index[16]
  'has twenty equal sides.')  # index[17]

class Polygons:
  """Polygons"""
  __slots__ = ('_colour','_polygon','_sides')
  def __init__(self,colour,polygon,sides):

    self._colour = colour
    self._polygon = polygon
    self._sides = sides

try:
  Polygons('','','')._colour
  Polygons('','','')._polygon
  Polygons('','','')._sides
except AttributeError:pass

for i in range(18):
  print(
    getattr(Polygons(colour_name[0],polygons[i],sides[i]),'_colour'),
    getattr(Polygons(colour_name[0],polygons[i],sides[i]),'_polygon'),
    getattr(Polygons(colour_name[0],polygons[i],sides[i]),'_sides'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
global_var = 'Non Dedicated Variable'

class Dedicated_var:
  """Dedicated_var"""
  def dedicated_var():
    global global_var

    global_var = 'Dedicated Variable'

print(global_var)

Dedicated_var.dedicated_var()

print(global_var)

print(getattr(Dedicated_var,'__doc__'))
