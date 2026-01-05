class Main:
  def __init__(self,arg1,arg2):

    self.arg1 = arg1
    self.arg2 = arg2

print(Main('arg1','arg2').arg1)
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

  def return_self(self):
    return 'arg1','arg2'

  def class_data(self):
    print(self.arg1)

Main('arg1','arg2').class_data()

print(Main.return_self('Agument Placeholder Value')[0])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  def __init__(self,arg1,arg2):

    self.arg1 = arg1
    self.arg2 = arg2

  def return_args(*args):
    return args

main = Main.return_args(
  'args1','args2','args3','args4','args5')

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
  kwarg3 = 'karg3',kwarg4 = 'karg4'
  )

print(Main.get('kwarg4','Attribute Not Found:'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  def __init__(self,**kwargs):

    self.args = kwargs

  def return_keyword_args(**kwargs):
    return kwargs

main = Main.return_keyword_args(
  kwarg1 = 'karg1',kwarg2 = 'karg2',
  kwarg3 = 'karg3',kwarg4 = 'karg4'
  )

print(main.get('kwarg3','Attribute Not Found:'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
    def __init__(self,**kwargs):

        self.kwargs = kwargs

class Sub(Main):pass

main = Sub(
  kwarg1 = 'keyword argument1',
  kwarg2 = 'keyword argument2',
  kwarg3 = 'keyword argument3')

print(main.kwargs.get('kwarg3','Attribute Not Found:'))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
    def __init__(self,**kwargs):

        self.__dict__.update(kwargs)

class Sub(Main):pass

main = Main(
  kwarg1 = 'keyword argument1',
  kwarg2 = 'keyword argument2',
  kwarg3 = 'keyword argument3')

print(main.kwarg1)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Main:
  def __init__(self,*args):

    self.args = args

  def class_data(self):
    print(self.args[0])

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
    print(self.kwargs.get('kwarg5','Attribute Not Found:'))

Main(
  kwarg1 = 'karg1',kwarg2 = 'karg2',
  kwarg3 = 'karg3',kwarg4 = 'karg4',
  kwarg5 = 'karg5',kwarg6 = 'karg6',
  kwarg7 = 'karg7',kwarg8 = 'karg8',
  kwarg9 = 'karg9',kwarg10 = 'karg10'
  ).class_data()
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

class Superclass2(Main):

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

class Superclass2(Main):

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
class Grandmother:
    def __init__(
        self,grandmother1,grandmother2,grandmother3):

        self.grandmother1 = grandmother1
        self.grandmother2 = grandmother2
        self.grandmother3 = grandmother3

class Grandfather:
    def __init__(
        self, grandfather1,grandfather2,grandfather3):

        self.grandfather1 = grandfather1
        self.grandfather2 = grandfather2
        self.grandfather3 = grandfather3

class Mom:
    def __init__(self, mom1,mom2,mom3):

        self.mom1 = mom1
        self.mom2 = mom2
        self.mom3 = mom3

class Dad:
    def __init__(self,dad1,dad2,dad3):

        self.dad1 = dad1
        self.dad2 = dad2
        self.dad3 = dad3

class Child(Grandmother):
    def __init__(
        self,grandmother1,grandmother2,grandmother3,
        grandfather1,grandfather2,grandfather3,
        mom1,mom2,mom3,dad1,dad2,dad3):

        Grandmother.__init__(self,grandmother1,grandmother2,grandmother3)
        Grandfather.__init__(self,grandfather1,grandfather2,grandfather3)
        Mom.__init__(self,mom1,mom2,mom3)
        Dad.__init__(self,dad1,dad2,dad3)

grandmother = Grandmother('Grandmother1','Grandmother2','Grandmother3')

grandfather = Grandfather('Grandfather1','Grandfather2','Grandfather3')

mom = Mom('Mom1','Mom2','Mom3');dad = Dad('Dad1', 'Dad2','Dad3')

child = Child(
    'Grandmother1','Grandmother2','Grandmother3',
    'Grandfather1','Grandfather2','Grandfather3',
    'Dad1','Dad2','Dad3','Mom1', 'Mom2','Mom3')

print(grandmother.grandmother1)

print(grandfather.grandfather1)

print(mom.mom1)

print(dad.dad1)

print(child.grandmother1)

print(child.grandfather1)

print(child.mom1)

print(child.dad1)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Grandmother:
    def __init__(
        self,grandmother1,grandmother2,grandmother3,*args):

        self.grandmother1 = grandmother1
        self.grandmother2 = grandmother2
        self.grandmother3 = grandmother3

        super().__init__(*args)

class Grandfather:
    def __init__(
        self, grandfather1,grandfather2,grandfather3,*args):

        self.grandfather1 = grandfather1
        self.grandfather2 = grandfather2
        self.grandfather3 = grandfather3
        super().__init__(*args)

class Mom:
    def __init__(self, mom1,mom2,mom3,*args):

        self.mom1 = mom1
        self.mom2 = mom2
        self.mom3 = mom3

        super().__init__(*args)

class Dad:
    def __init__(self,dad1,dad2,dad3,*args):

        self.dad1 = dad1
        self.dad2 = dad2
        self.dad3 = dad3

        super().__init__(*args)

class Child(Grandmother,Grandfather,Mom,Dad):
    def __init__(
      self,grandmother1, grandmother2, grandmother3,
      grandfather1, grandfather2, grandfather3,
      mom1, mom2, mom3,dad1, dad2, dad3):

      super().__init__(
            grandmother1,grandmother2,grandmother3,
            grandfather1,grandfather2,grandfather3,
            mom1,mom2,mom3,dad1,dad2,dad3)

grandmother = Grandmother('Grandmother1','Grandmother2','Grandmother3')

grandfather = Grandfather('Grandfather1','Grandfather2','Grandfather3')

mom = Mom('Mom1','Mom2','Mom3');dad = Dad('Dad1', 'Dad2','Dad3')

child = Child(
    'Grandmother1','Grandmother2','Grandmother3',
    'Grandfather1','Grandfather2','Grandfather3',
    'Mome1','Mom2','Mom3','Dad1','Dad2','Dad3')

print(grandmother.grandmother1)

print(grandfather.grandfather1)

print(mom.mom1)

print(dad.dad1)

print(child.grandmother1)

print(child.grandfather1)

print(child.mom1)

print(child.dad1)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Grandmother:
    def __init__(
        self,grandmother1,grandmother2,grandmother3,**kwargs):

        self.grandmother1 = grandmother1
        self.grandmother2 = grandmother2
        self.grandmother3 = grandmother3

        super().__init__(**kwargs)

class Grandfather:
    def __init__(
        self, grandfather1,grandfather2,grandfather3,**kwargs):

        self.grandfather1 = grandfather1
        self.grandfather2 = grandfather2
        self.grandfather3 = grandfather3

        super().__init__(**kwargs)

class Mom:
    def __init__(self, mom1,mom2,mom3,**kwargs):

        self.mom1 = mom1
        self.mom2 = mom2
        self.mom3 = mom3

        super().__init__(**kwargs)

class Dad:
    def __init__(self,dad1,dad2,dad3,**kwargs):

        self.dad1 = dad1
        self.dad2 = dad2
        self.dad3 = dad3

        super().__init__(**kwargs)

class Child(Grandmother,Grandfather,Mom,Dad):
    def __init__(
      self,grandmother1, grandmother2, grandmother3,
      grandfather1, grandfather2, grandfather3,
      mom1, mom2, mom3,dad1, dad2, dad3):

      super().__init__(
            grandmother1 = grandmother1,
            grandmother2 = grandmother2,
            grandmother3 = grandmother3,
            grandfather1 = grandfather1,
            grandfather2 = grandfather2,
            grandfather3 = grandfather3,
            mom1= mom1,mom2 = mom2,
            mom3 = mom3,dad1 = dad1,
            dad2 = dad2,dad3 = dad3)

grandmother = Grandmother('Grandmother1','Grandmother2','Grandmother3')

grandfather = Grandfather('Grandfather1','Grandfather2','Grandfather3')

mom = Mom('Mom1','Mom2','Mom3');dad = Dad('Dad1', 'Dad2','Dad3')

child = Child(
    'Grandmother1','Grandmother2','Grandmother3',
    'Grandfather1','Grandfather2','Grandfather3',
    'Dad1','Dad2','Dad3','Mom1', 'Mom2','Mom3')

print(grandmother.grandmother1)

print(grandfather.grandfather1)

print(mom.mom1)

print(dad.dad1)

print(child.grandmother1)

print(child.grandfather1)

print(child.mom1)

print(child.dad1)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Names1:
  def __init__(self,name1,name2):

    self.name1 = 'Bob'
    self.name2 = 'Rob'

class Names2:
  def __init__(self,name3,name4):

    self.name3 = 'Tom'
    self.name4 = 'John'

class Names3:
  def __init__(self,name5,name6):

    self.name5 = 'Mary'
    self.name6 = 'Terry'

class Child(Names1): # MRO doesn't matter. No ladder.
  def __init__(
    self,name1,name2,name3,name4,name5,name6):

    Names1.__init__(self,name1,name2)
    Names2.__init__(self,name3,name4)
    Names3.__init__(self,name5,name6)

print(Names1(
  'argument placeholder value',
  'argument placeholder value').name2)

print(Names2(
  'argument placeholder value',
  'argument placeholder value').name4)

print(Names3(
  'argument placeholder value',
  'argument placeholder value').name6)

print(Child(
  'argument placeholder value',
  'argument placeholder value',
  'argument placeholder value',
  'argument placeholder value',
  'argument placeholder value',
  'argument placeholder value'
  ).name6)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Names1:
  def __init__(self,name1,name2):

    self.name1 = 'Bob'
    self.name2 = 'Rob'

class Names2(Names1):
  def __init__(self,name3,name4):

    self.name3 = 'Tom'
    self.name4 = 'John'

class Names3(Names2):
  def __init__(self,name5,name6):

    self.name5 = 'Mary'
    self.name6 = 'Terry'

class Child(Names3,Names2,Names1): # MRO does matter
  def __init__(
    self,name1,name2,name3,name4,name5,name6):

    Names1.__init__(self,name1,name2)
    Names2.__init__(self,name3,name4)
    Names3.__init__(self,name5,name6)

print(Names1(
  'argument placeholder value',
  'argument placeholder value').name2)

print(Names2(
  'argument placeholder value',
  'argument placeholder value').name4)

print(Names3(
  'argument placeholder value',
  'argument placeholder value').name6)

print(Child(
  'argument placeholder value',
  'argument placeholder value',
  'argument placeholder value',
  'argument placeholder value',
  'argument placeholder value',
  'argument placeholder value'
  ).name6)
