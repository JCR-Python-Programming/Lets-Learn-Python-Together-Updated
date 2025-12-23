class Main:

  def __init__(self,**kwargs):

    self.kwargs = kwargs

class Main_super(Main):

  def __init__(self,**kwargs):

    super().__init__(**kwargs)

lazy1 = Main(kw_arg1 = 'argument1',kw_arg2 = 'argument2',kw_arg3 = 'argument3')

lazy2 = Main_super(kw_arg1 = 'argument1',kw_arg2 = 'argument2',kw_arg3 = 'argument3')

print(lazy1.kwargs.get('kw_arg3','Attribute does not exist'))

print(lazy2.kwargs.get('kw_arg4','Attribute does not exist'))


class Main:

  def __init__(self,**kwargs):

    self.__dict__.update(kwargs)

class Main_super1(Main):

  def __init__(self,**kwargs):

    super().__init__(**kwargs)

class Main_super2(Main):

  def __init__(self,**kwargs):

    super().__init__(**kwargs)

lazy1 = Main(kw_arg1 = 'argument1',kw_arg2 = 'argument2',kw_arg3 = 'argument3')

lazy2 = Main_super1(kw_arg1 = 'argument1',kw_arg2 = 'argument2',kw_arg3 = 'argument3')

lazy3 = Main_super2(kw_arg1 = 'argument1',kw_arg2 = 'argument2',kw_arg3 = 'argument3')

try:
  print(lazy1.kw_arg1)

  print(lazy2.kw_arg2)

  print(lazy3.kw_arg3)
except (AttributeError,TypeError):
  print('Attribute Not Found:')


class Main:
  def __init__(self,**kwargs):

    self.__dict__.update(kwargs)

class Sub(Main):pass

lazy1 = Main(kw_arg1 = 'argument1',kw_arg2 = 'argument2',kw_arg3 = 'argument3')

lazy2 = Sub(kw_arg1 = 'argument1',kw_arg2 = 'argument2',kw_arg3 = 'argument3')

try:
  print(lazy1.kw_arg1)

  print(lazy2.kw_arg2)
except (AttributeError,TypeError):
  pass


from dataclasses import dataclass

@dataclass
class Main:

  kw_arg1: str
  kw_arg2: str
  kw_arg3: str

class MainSuper(Main):
  pass

lazy1 = Main(kw_arg1='arg1', kw_arg2='arg2', kw_arg3='arg3')

lazy2 = Main(kw_arg1='arg1', kw_arg2='arg2', kw_arg3='arg3')

try:
  print(lazy1.kw_arg1)

  print(lazy1.kw_arg2)
except (AttributeError,TypeError):
  print('Attribute Not Found:')


class Mom:pass

class Dad:pass

class Brother:pass

class Sister:pass

class Pet:pass

class All(Pet,Sister,Brother,Dad,Mom):
  print('MRO = Method Resolution Order')

print(All.mro())

print(All.__mro__)


class FamilyMember:
    registry = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.registry.append(cls.__name__)
        print(f"Registered new family member: {cls.__name__}")

class Mom(FamilyMember): pass
class Dad(FamilyMember): pass
class Child(Mom, Dad): pass

print(FamilyMember.registry)
