class Main:
  def __init__(self,arg1,arg2):

    self.arg1 = arg1
    self.arg2 = arg2

print(Main('arg1','arg2').arg1)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  def __init__(self,arg1,arg2):

    self.arg1 = arg1
    self.arg2 = arg2

  def class_datta(self):
    print(self.arg2)

Main('arg1','arg2').class_datta()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  def __init__(self,*args):

    self.args = args

print(Main('arg1','arg2').args[0])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  def __init__(self,arg1,arg2):

    self.arg1 = arg1
    self.arg2 = arg2

  def return_args(arg1,arg2):
    return 'arg1','arg2'

Main = Main.return_args(
  'argument placeholder','argument placeholder')

print(Main[0])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  def __init__(self,arg1,arg2):

    self.arg1 = arg1
    self.arg2 = arg2

  def return_args(*args):
    return args

main = Main.return_args('args1','args2','args3','args4','args5')

print(main[4])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  def __init__(self,arg1,arg2):

    self.arg1 = arg1
    self.arg2 = arg2

  def return_keyword_args(**kwargs):
    return kwargs

Main = Main.return_keyword_args(
  kwarg1 = 'karg1',kwarg2 = 'karg2',
  kwarg3 = 'karg3',kwarg4 = 'karg4')

print(Main.get('kwarg4','Attribute Not Found:'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  def __init__(self,**kwargs):

    self.args = kwargs

  def return_keyword_args(**kwargs):
    return kwargs

main = Main.return_keyword_args(
  kwarg1 = 'karg1',kwarg2 = 'karg2',
  kwarg3 = 'karg3',kwarg4 = 'karg4')

print(main.get('kwarg3','Attribute Not Found:'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  def __init__(self,**kwargs):

    self.kwargs = kwargs

class Sub(Main):
  pass

main = Sub(
  kwarg1 = 'keyword argument1',
  kwarg2 = 'keyword argument2',
  kwarg3 = 'keyword argument3')

print(main.kwargs.get('kwarg3','Attribute Not Found:'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  def __init__(self,**kwargs):

    self.__dict__.update(kwargs)

class Sub(Main):
  pass

main = Main(
  kwarg1 = 'keyword argument1',
  kwarg2 = 'keyword argument2',
  kwarg3 = 'keyword argument3')

print(main.kwarg1)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  def __init__(self,*args):

    self.args = args

  def class_datta(self):
    print(self.args[0])

Main(
  'arg1','arg2','arg3',
  'arg4','arg5','arg6',
  'arg7','arg8','arg9').class_datta()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  def __init__(self,**kwargs):

    self.kwargs = kwargs

  def class_datta(self):
    print(self.kwargs.get('kwarg5','Attribute Not Found:'))

Main(
  kwarg1 = 'karg1',kwarg2 = 'karg2',
  kwarg3 = 'karg3',kwarg4 = 'karg4',
  kwarg5 = 'karg5',kwarg6 = 'karg6',
  kwarg7 = 'karg7',kwarg8 = 'karg8',
  kwarg9 = 'karg9',kwarg10 = 'karg10').class_datta()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  def __init__(self,attribute1,attribute2):

    self.attribute1 = attribute1
    self.attribute2 = attribute2

  def return_value(variable_value):
    return 'Returned Variable Value from Main.'

class Superclass1(Main):
  def __init__(self,attribute1,attribute2):
    super().__init__(attribute1,attribute2)

class Superclass2(Superclass1):
  def __init__(
    self,attribute1,attribute2,attribute3,attribute4):
    super().__init__(attribute1,attribute2)

    self.attribute3 = attribute3
    self.attribute4 = attribute4

class_attribute_values = Main(
  'I am the attribute property value of attribute1',
  'I am the attribute property value of attribute2')

superclass1_attribute_values = Superclass1(
  'I am the attribute property value of attribute1',
  'I am the attribute property value of attribute2')

superclass2_attribute_values = Superclass2(
  'I am the attribute property value of attribute1',
  'I am the attribute property value of attribute2',
  'I am the attribute property value of attribute3',
  'I am the attribute property value of attribute4')

return_value1 = Main.return_value('argument placeholder')

return_value2 = Superclass1.return_value('argument placeholder')

return_value3 = Superclass2.return_value('argument placeholder')

print(class_attribute_values.attribute1)

print(superclass1_attribute_values.attribute1)

print(superclass2_attribute_values.attribute1)

print(return_value1)
print(return_value2)
print(return_value3)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
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

class_attribute_values = Main(
  'I am the attribute property value of attribute1',
  'I am the attribute property value of attribute2')

superclass1_attribute_values = Superclass1(
  'I am the attribute property value of attribute1',
  'I am the attribute property value of attribute2')

superclass2_attribute_values = Superclass2(
  'I am the attribute property value of attribute1',
  'I am the attribute property value of attribute2',
  'I am the attribute property value of attribute3',
  'I am the attribute property value of attribute4')

return_value1 = Main.return_value('argument placeholder')

return_value2 = Superclass1.return_value('argument placeholder')

return_value3 = Superclass2.return_value('argument placeholder')

print(class_attribute_values.args[0])

print(superclass1_attribute_values.args[0])

print(superclass2_attribute_values.args[0])

print(return_value1)
print(return_value2)
print(return_value3)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
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

class_attribute_values = Main(
  kwarg1 = 'I am the attribute property value of attribute1',
  kwarg2 = 'I am the attribute property value of attribute2')

superclass1_attribute_values = Superclass1(
  kwarg1 = 'I am the attribute property value of attribute1',
  kwarg2 = 'I am the attribute property value of attribute2')

superclass2_attribute_values = Superclass2(
  kwarg1 = 'I am the attribute property value of attribute1',
  kwarg2 = 'I am the attribute property value of attribute2',
  kwarg3 = 'I am the attribute property value of attribute3',
  kwarg4 = 'I am the attribute property value of attribute4')

return_value1 = Main.return_value('argument placeholder')

return_value2 = Superclass1.return_value('argument placeholder')

return_value3 = Superclass2.return_value('argument placeholder')

print(class_attribute_values.kwargs.get('kwarg1','Attribute Not Found:'))

print(superclass1_attribute_values.kwargs.get('kwarg1','Attribute Not Found:'))

print(superclass2_attribute_values.kwargs.get('kwarg1','Attribute Not Found:'))

print(return_value1)
print(return_value2)
print(return_value3)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
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

class_attribute_values = Main(
  kwarg1 = 'I am the attribute property value of attribute1',
  kwarg2 = 'I am the attribute property value of attribute2')

superclass1_attribute_values = Superclass1(
  kwarg1 = 'I am the attribute property value of attribute1',
  kwarg2 = 'I am the attribute property value of attribute2')

superclass2_attribute_values = Superclass2(
  kwarg1 = 'I am the attribute property value of attribute1',
  kwarg2 = 'I am the attribute property value of attribute2',
  kwarg3 = 'I am the attribute property value of attribute3',
  kwarg4 = 'I am the attribute property value of attribute4')

return_value1 = Main.return_value('argument placeholder')

return_value2 = Superclass1.return_value('argument placeholder')

return_value3 = Superclass2.return_value('argument placeholder')

print(class_attribute_values.kwarg1)

print(superclass1_attribute_values.kwarg1)

print(superclass2_attribute_values.kwarg1)

print(return_value1)
print(return_value2)
print(return_value3)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  def __init__(
    self,main1,main2,main3):

    self.main1 = main1
    self.main2 = main2
    self.main3 = main3

class Sub_one:
  def __init__(self,sub_one1,sub_one2,sub_one3):

    self.sub_one1 = sub_one1
    self.sub_one2 = sub_one2
    self.sub_one3 = sub_one3

class Sub_two:
  def __init__(self,sub_two1,sub_two2,sub_two3):

    self.sub_two1 = sub_two1
    self.sub_two2 = sub_two2
    self.sub_two3 = sub_two3

class Sub_three:
  def __init__(self,sub_three1,sub_three2,sub_three3):

    self.sub_three1 = sub_three1
    self.sub_three2 = sub_three2
    self.sub_three3 = sub_three3

class Class_all(Main,Sub_one,Sub_two,Sub_three):
  def __init__(
    self,main1,main2,main3,
    sub_one1,sub_one2,sub_one3,
    sub_two1,sub_two2,sub_two3,sub_three1,sub_three2,sub_three3):

    Main.__init__(self,main1,main2,main3)
    Sub_one.__init__(self,sub_one1,sub_one2,sub_one3)
    Sub_two.__init__(self,sub_two1,sub_two2,sub_two3)
    Sub_three.__init__(self,sub_three1,sub_three2,sub_three3)

main = Main('Main value1','Main value2','Main value3')

sub_one = Sub_one('Sub_one value1','Sub_one value2','Sub_one value3')

sub_two = Sub_two('Sub_two value1','Sub_two value2','Sub_two value3')

sub_three = Sub_three('Sub_three value1','Sub_three value2','Sub_three value3')

class_all = Class_all(
  'Main value1','Main value2','Main value3',
  'Sub_one value1','Sub_one value2',
  'Sub_one value3','Sub_three value1',
  'Sub_three value2','Sub_three value3',
  'Sub_two value1','Sub_two value2','Sub_two value3')

print(main.main1)

print(sub_one.sub_one1)

print(sub_two.sub_two1)

print(sub_three.sub_three1)

print(class_all.main1)
print(class_all.sub_one1)
print(class_all.sub_two1)
print(class_all.sub_three1)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  def __init__(
    self,main1,main2,main3,*args):

    self.main1 = main1
    self.main2 = main2
    self.main3 = main3
    super().__init__(*args)

class Sub_one:
  def __init__(
    self,sub_one1,sub_one2,sub_one3,*args):

    self.sub_one1 = sub_one1
    self.sub_one2 = sub_one2
    self.sub_one3 = sub_one3
    super().__init__(*args)

class Sub_two:
  def __init__(self,sub_two1,sub_two2,sub_two3,*args):

    self.sub_two1 = sub_two1
    self.sub_two2 = sub_two2
    self.sub_two3 = sub_two3
    super().__init__(*args)

class Sub_three:
  def __init__(self,sub_three1,sub_three2,sub_three3,*args):

    self.sub_three1 = sub_three1
    self.sub_three2 = sub_three2
    self.sub_three3 = sub_three3
    super().__init__(*args)

class Class_all(Main,Sub_one,Sub_two,Sub_three):
  def __init__(
    self,main1,main2,main3,
    sub_one1,sub_one2,sub_one3,
    sub_two1,sub_two2,sub_two3,sub_three1,sub_three2,sub_three3):
    super().__init__(
      main1,main2,main3,
      sub_one1,sub_one2,sub_one3,
      sub_two1,sub_two2,sub_two3,sub_three1,sub_three2,sub_three3)

main = Main('Main value1','Main value2','Main value3')

sub_one = Sub_one('Sub_one value1','Sub_one value2','Sub_one value3')

sub_two = Sub_two('Sub_two value1','Sub_two value2','Sub_two value3')

sub_three = Sub_three('Sub_three value1','Sub_three value2','Sub_three value3')

class_all = Class_all(
  'Main value1','Main value2','Main value3',
  'Sub_one value1','Sub_one value2',
  'Sub_one value3','Mome1','Sub_two value2',
  'Sub_two value3','Sub_three value1',
  'Sub_three value2','Sub_three value3')

print(main.main1)

print(sub_one.sub_one1)

print(sub_two.sub_two1)

print(sub_three.sub_three1)

print(class_all.main1)
print(class_all.sub_one1)
print(class_all.sub_two1)
print(class_all.sub_three1)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  def __init__(
    self,main1,main2,main3,**kwargs):

    self.main1 = main1
    self.main2 = main2
    self.main3 = main3
    super().__init__(**kwargs)

class Sub_one:
  def __init__(
    self,sub_one1,sub_one2,sub_one3,**kwargs):

    self.sub_one1 = sub_one1
    self.sub_one2 = sub_one2
    self.sub_one3 = sub_one3
    super().__init__(**kwargs)

class Sub_two:
  def __init__(self,sub_two1,sub_two2,sub_two3,**kwargs):

    self.sub_two1 = sub_two1
    self.sub_two2 = sub_two2
    self.sub_two3 = sub_two3
    super().__init__(**kwargs)

class Sub_three:
  def __init__(self,sub_three1,sub_three2,sub_three3,**kwargs):

    self.sub_three1 = sub_three1
    self.sub_three2 = sub_three2
    self.sub_three3 = sub_three3
    super().__init__(**kwargs)

class Class_all(Main,Sub_one,Sub_two,Sub_three):
  def __init__(
    self,main1,main2,main3,
    sub_one1,sub_one2,sub_one3,
    sub_two1,sub_two2,sub_two3,
    sub_three1,sub_three2,sub_three3):
    super().__init__(
      main1 = main1,main2 = main2,
      main3 = main3,sub_one1 = sub_one1,
      sub_one2 = sub_one2,sub_one3 = sub_one3,
      sub_two1= sub_two1,sub_two2 = sub_two2,
      sub_two3 = sub_two3,sub_three1 = sub_three1,
      sub_three2 = sub_three2,sub_three3 = sub_three3)

main = Main('Main value1','Main value2','Main value3')

sub_one = Sub_one('Sub_one value1','Sub_one value2','Sub_one value3')

sub_two = Sub_two('Sub_two value1','Sub_two value2','Sub_two value3')

sub_three = Sub_three('Sub_three value1','Sub_three value2','Sub_three value3')

class_all = Class_all(
  'Main value1','Main value2','Main value3',
  'Sub_one value1','Sub_one value2','Sub_one value3',
  'Sub_three value1','Sub_three value2','Sub_three value3',
  'Sub_two value1','Sub_two value2','Sub_two value3')

print(main.main1)

print(sub_one.sub_one1)

print(sub_two.sub_two1)

print(sub_three.sub_three1)

print(class_all.main1)
print(class_all.sub_one1)
print(class_all.sub_two1)
print(class_all.sub_three1)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  def __init__(self,main1,main2):

    self.main1 = 'Main class value1'
    self.main2 = 'Main class value2'

class Sub_one:
  def __init__(self,sub_one1,sub_one2):

    self.sub_one1 = 'Sub_one class value1'
    self.sub_one2 = 'Sub_one class value2'

class Sub_two:
  def __init__(self,sub_two1,sub_two2):

    self.sub_two1 = 'Sub_two class value1'
    self.sub_two2 = 'Sub_two class value2'

class Child(Main,Sub_one,Sub_two):
  def __init__(self,main1,main2,sub_one1,sub_one2,sub_two1,sub_two2):

    Main.__init__(self,main1,main2)
    Sub_one.__init__(self,sub_one1,sub_one2)
    Sub_two.__init__(self,sub_two1,sub_two2)

print(Main(
  'argument placeholder value',
  'argument placeholder value').main2)

print(Sub_one(
  'argument placeholder value',
  'argument placeholder value').sub_one2)

print(Sub_two(
  'argument placeholder value',
  'argument placeholder value').sub_two2)

print(Child(
  'argument placeholder value',
  'argument placeholder value',
  'argument placeholder value',
  'argument placeholder value',
  'argument placeholder value',
  'argument placeholder value').main2)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  def __init__(self):

    self.main1 = 'Main class value1'
    self.main2 = 'Main class value2'

class Sub_one():
  def __init__(self):

    self.sub_one1 = 'Sub_one class value1'
    self.sub_one2 = 'Sub_one class value2'

class Sub_two():
  def __init__(self):

    self.sub_two1 = 'Sub_two class value1'
    self.sub_two2 = 'Sub_two class value2'

class Child(Main,Sub_one,Sub_two):
  def __init__(self):
    super().__init__()

    Sub_one.__init__(self)
    Sub_two.__init__(self)

print(Main().main1)
print(Sub_one().sub_one1)
print(Sub_two().sub_two1)
print(Child().main1)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  def __init__(self,*args):

    self.main1 = 'Main class value1'
    self.main2 = 'Main class value2'

class Sub_one:
  def __init__(self,*args):

    self.sub_one1 = 'Sub_one class value1'
    self.sub_one2 = 'Sub_one class value2'

class Sub_two:
  def __init__(self,*args):

    self.sub_two1 = 'Sub_two class value1'
    self.sub_two2 = 'Sub_two class value2'

class Child(Main,Sub_one,Sub_two):
  def __init__(self,main1,main2,sub_one1,sub_one2,sub_two1,sub_two2):

    Main.__init__(self,main1,main2)
    Sub_one.__init__(self,sub_one1,sub_one2)
    Sub_two.__init__(self,sub_two1,sub_two2)

print(Main(
  'argument placeholder value',
  'argument placeholder value').main2)

print(Sub_one(
  'argument placeholder value',
  'argument placeholder value').sub_one2)

print(Sub_two(
  'argument placeholder value',
  'argument placeholder value').sub_two2)

print(Child(
  'argument placeholder value',
  'argument placeholder value',
  'argument placeholder value',
  'argument placeholder value',
  'argument placeholder value',
  'argument placeholder value').sub_two2)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  def __init__(self,*args):

    self.main1 = 'Main class value1'
    self.main2 = 'Main class value2'

class Sub_one:
  def __init__(self,*args):

    self.sub_one1 = 'Sub_one class value1'
    self.sub_one2 = 'Sub_one class value2'

class Sub_two:
  def __init__(self,*args):

    self.sub_two1 = 'Sub_two class value1'
    self.sub_two2 = 'Sub_two class value2'

class Child(Main,Sub_one,Sub_two):
  def __init__(self):
    super().__init__()

    Sub_one.__init__(self)
    Sub_two.__init__(self)

print(Main().main2)
print(Sub_one().sub_one2)
print(Sub_two().sub_two2)
print(Child().main1)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  def __init__(self,main1,main2):

    self.main1 = 'Main class value1'
    self.main2 = 'Main class value2'

class Sub_one(Main):
  def __init__(self,sub_one1,sub_one2):

    self.sub_one1 = 'Sub_one class value1'
    self.sub_one2 = 'Sub_one class value2'

class Sub_two(Sub_one):
  def __init__(self,sub_two1,sub_two2):

    self.sub_two1 = 'Sub_two class value1'
    self.sub_two2 = 'Sub_two class value2'

class Child(Sub_two,Sub_one,Main):
  def __init__(self,main1,main2,sub_one1,sub_one2,sub_two1,sub_two2):

    Main.__init__(self,main1,main2)
    Sub_one.__init__(self,sub_one1,sub_one2)
    Sub_two.__init__(self,sub_two1,sub_two2)

print(Main(
  'argument placeholder value',
  'argument placeholder value').main2)

print(Sub_one(
  'argument placeholder value',
  'argument placeholder value').sub_one2)

print(Sub_two(
  'argument placeholder value',
  'argument placeholder value').sub_two2)

print(Child(
  'argument placeholder value',
  'argument placeholder value',
  'argument placeholder value',
  'argument placeholder value',
  'argument placeholder value',
  'argument placeholder value').sub_two2)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  def __init__(self,*args):

    self.main1 = 'Main class value1'
    self.main2 = 'Main class value2'

class Sub_one(Main):
  def __init__(self,*args):

    self.sub_one1 = 'Sub_one class value1'
    self.sub_one2 = 'Sub_one class value2'

class Sub_two(Sub_one):
  def __init__(self,*args):

    self.sub_two1 = 'Sub_two class value1'
    self.sub_two2 = 'Sub_two class value2'

class Child(Sub_two,Sub_one,Main):
  def __init__(self,main1,main2,sub_one1,sub_one2,sub_two1,sub_two2):

    Main.__init__(self,main1,main2)
    Sub_one.__init__(self,sub_one1,sub_one2)
    Sub_two.__init__(self,sub_two1,sub_two2)

print(Main(
  'argument placeholder value',
  'argument placeholder value').main2)

print(Sub_one(
  'argument placeholder value',
  'argument placeholder value').sub_one2)

print(Sub_two(
  'argument placeholder value',
  'argument placeholder value').sub_two2)

print(Child(
  'argument placeholder value',
  'argument placeholder value',
  'argument placeholder value',
  'argument placeholder value',
  'argument placeholder value',
  'argument placeholder value').sub_two2)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  def __init__(self,main1,main2,**kwargs):

    self.main1 = 'Main class value1'
    self.main2 = 'Main class value2'

class Sub_one:
  def __init__(self,sub_one1,sub_one2,**kwargs):

    self.sub_one1 = 'Sub_one class value1'
    self.sub_one2 = 'Sub_one class value2'

class Sub_two:
  def __init__(self,sub_two1,sub_two2,**kwargs):

    self.sub_two1 = 'Sub_two class value1'
    self.sub_two2 = 'Sub_two class value2'

class Child(Main,Sub_one,Sub_two):
  def __init__(self,main1,main2,sub_one1,sub_one2,sub_two1,sub_two2):

    Main.__init__(self,main1 = main1,main2 = main2)
    Sub_one.__init__(self,sub_one1 = sub_one1,sub_one2 = sub_one2)
    Sub_two.__init__(self,sub_two1 = sub_two1,sub_two2 = sub_two2)

print(Main(
  'argument placeholder value',
  'argument placeholder value').main2)

print(Sub_one(
  'argument placeholder value',
  'argument placeholder value').sub_one2)

print(Sub_two(
  'argument placeholder value',
  'argument placeholder value').sub_two2)

print(Child(
  'argument placeholder value',
  'argument placeholder value',
  'argument placeholder value',
  'argument placeholder value',
  'argument placeholder value',
  'argument placeholder value').sub_two2)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  def __init__(self,main1,main2,**kwargs):

    self.main1 = 'Main class value1'
    self.main2 = 'Main class value2'

class Sub_one(Main):
  def __init__(self,sub_one1,sub_one2,**kwargs):

    self.sub_one1 = 'Sub_one class value1'
    self.sub_one2 = 'Sub_one class value2'

class Sub_two(Sub_one):
  def __init__(self,sub_two1,sub_two2,**kwargs):

    self.sub_two1 = 'Sub_two class value1'
    self.sub_two2 = 'Sub_two class value2'

class Child(Sub_two,Sub_one,Main):
  def __init__(self,main1,main2,sub_one1,sub_one2,sub_two1,sub_two2):

    Main.__init__(self,main1 = main1,main2 = main2)
    Sub_one.__init__(self,sub_one1 = sub_one1,sub_one2 = sub_one2)
    Sub_two.__init__(self,sub_two1 = sub_two1,sub_two2 = sub_two2)

print(Main(
  'argument placeholder value',
  'argument placeholder value').main2)

print(Sub_one(
  'argument placeholder value',
  'argument placeholder value').sub_one2)

print(Sub_two(
  'argument placeholder value',
  'argument placeholder value').sub_two2)

print(Child(
  'argument placeholder value',
  'argument placeholder value',
  'argument placeholder value',
  'argument placeholder value',
  'argument placeholder value',
  'argument placeholder value').sub_two2)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  def __init__(self,par1,par2,par3):

    self.parameter1 = par1
    self.parameter2 = par2
    self.parameter3 = par3

  def print_message1():
    print('Print_message one','Print_message two')

class Super1(Main):
  def __init__(self,parameter1,parameter2,parameter3,par4):
    super().__init__(parameter1,parameter2,parameter3)

    self.parameter4 = par4

class Super2(Super1):
  def __init__(self,parameter1,parameter2,parameter3,parameter4,par5):
    super().__init__(parameter1,parameter2,parameter3,parameter4)

    self.parameter5 = par5

class Super3(Super2):
  def __init__(self,parameter1,parameter2,parameter3,parameter4,parameter5,par6):
    super().__init__(parameter1,parameter2,parameter3,parameter4,parameter5)

    self.parameter6 = par6

class Super4(Super3):
  def __init__(self,parameter1,parameter2,parameter3,parameter4,parameter5,parameter6,par7):
    super().__init__(parameter1,parameter2,parameter3,parameter4,parameter5,parameter6)

    self.parameter7 = par7

class Sub_class:
  def print_message2():
    print('Print_message one','Print_message two')

class Child(Sub_class,Main):
  pass

text1 = Main(
  'parameter1','parameter2',
  'parameter3').parameter3

text2 = Super1(
  'parameter1','parameter2',
  'parameter3','parameter4').parameter4

text3 = Super2(
  'parameter1','parameter2',
  'parameter3','parameter4',
  'parameter5').parameter5

text4 = Super3(
  'parameter1','parameter2',
  'parameter3','parameter4',
  'parameter5','parameter6').parameter6

text5 = Super4(
  'parameter1','parameter2',
  'parameter3','parameter4',
  'parameter5','parameter6',
  'parameter7').parameter7

Child.print_message1()
Child.print_message2()

text6 = Main

print(text1)

print(text2)

print(text3)

print(text4)

print(text5)

print([cls.__name__ for cls in Super4.mro()])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main_class_skeleton_structure:
  def main():
    print('Main Class Act.')

class Sub_class_skeleton_structure_one(Main_class_skeleton_structure):
  def sub1():
    print('Sub One Class Act.')

class Sub_class_skeleton_structure_two(Sub_class_skeleton_structure_one):
  def sub2():
    print('Sub Two Class Act.')

class Class_all(
  Sub_class_skeleton_structure_two,
  Sub_class_skeleton_structure_one,
  Main_class_skeleton_structure):
  pass

Class_all.main()
Class_all.sub1()
Class_all.sub2()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main_class_skeleton_structure:
  def __init__(self,parameter1,parameter2,parameter3):
    self.parameter1 = parameter1
    self.parameter2 = parameter2
    self.parameter3 = parameter3

class Sub_super_class_skeleton_structure_one(Main_class_skeleton_structure):
  def __init__(self,parameter1,parameter2,parameter3):
    pass

  def __init__(self,parameter1,parameter2,parameter3):
    super().__init__(parameter1,parameter2,parameter3)

class Sub_super_class_skeleton_structure_two(Sub_super_class_skeleton_structure_one):
  def __init__(self,parameter1,parameter2,parameter3):
    pass

  def __init__(self,parameter1,parameter2,parameter3):
    super().__init__(parameter1,parameter2,parameter3)

class Class_all(
  Sub_super_class_skeleton_structure_two,
  Sub_super_class_skeleton_structure_one,
  Main_class_skeleton_structure):
  pass

print(Class_all('Main Class Act.','Sub One Class Act.','Sub Two Class Act.').parameter1)
print(Class_all('Main Class Act.','Sub One Class Act.','Sub Two Class Act.').parameter2)
print(Class_all('Main Class Act.','Sub One Class Act.','Sub Two Class Act.').parameter3)
