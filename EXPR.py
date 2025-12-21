class Mom:
  def __init__(self,*args):

    self.args = args

class Dad:
  def __init__(self,*args):

    self.args = args

class Sister:
  def __init__(self,*args):

    self.args = args

class Brother:
  def __init__(self,*args):

    self.args = args

class All(Brother,Sister,Dad,Mom): # have to shout here.
  pass

print(Mom('argument1','argument2','argument3').args[2])

print(Dad('argument1','argument2','argument3','argument4').args[3])

print(Sister('argument1','argument2','argument3','argument4','argument5').args[4])

print(Brother('argument1','argument2','argument3','argument4','argument5','argument6').args[5])

print(All('argument1','argument2','argument3','argument4','argument5','argument6').args[2])

print(All('argument1','argument2','argument3','argument4','argument5','argument6').args[3])

print(All('argument1','argument2','argument3','argument4','argument5','argument6').args[4])

print(All('argument1','argument2','argument3','argument4','argument5','argument6').args[5])




