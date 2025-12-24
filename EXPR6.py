class Grandmother:
  def __init__(self,*args):

    self.args = args

class Grandfather:
  def __init__(self,*args):

    self.args = args

class Mother:
  def __init__(self,*args):

    self.args = args

class Father:
  def __init__(self,*args):

    self.args = args

class Daughter:
  def __init__(self,*args):

    self.args = args

class Son:
  def __init__(self,*args):

    self.args = args

class Class_all(Grandmother):
  print('MRO = "Method Resolution Order"\n')

lazy_0 = (Grandmother('Argument Vaue 0','Argument Vaue 1','Argument Vaue 2'))
lazy_1 = (Grandfather('Argument Vaue 0','Argument Vaue 1','Argument Vaue 2'))
lazy_2 = (Mother('Argument Vaue 0','Argument Vaue 1','Argument Vaue 2'))
lazy_3 = (Father('Argument Vaue 0','Argument Vaue 1','Argument Vaue 2'))
lazy_4 = (Daughter('Argument Vaue 0','Argument Vaue 1','Argument Vaue 2'))
lazy_5 = (Son('Argument Vaue 0','Argument Vaue 1','Argument Vaue 2'))
lazy_6 = (Class_all('Argument Vaue 0','Argument Vaue 1','Argument Vaue 2'))

try:
  print(lazy_0.args[0])
except (NameError,IndexError,TypeError):
  print('Name or Index Not Found:')

'''
class Grandmother:
    def __init__(self, *args):
        print("Inside Grandmother")
        self.args = args

class Grandfather:
    def __init__(self, *args):
        super().__init__(*args) # Passes arguments to the next class in MRO
        print("Inside Grandfather")

print(All.mro())

print(All.__mro__)
'''
