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

class Sub(Main):pass

lazy1 = Main(kw_arg1 = 'argument1',kw_arg2 = 'argument2',kw_arg3 = 'argument3')

lazy2 = Sub(kw_arg1 = 'argument1',kw_arg2 = 'argument2',kw_arg3 = 'argument3')

try:
  print(lazy1.kw_arg1)

  print(lazy2.kw_arg2)
except (AttributeError,TypeError):
  pass
