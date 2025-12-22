class Main:
  def __init__(self,*args):
    self.args = args

class Main_super(Main):
  def __init__(self,*args):
    super().__init__(*args)

class Sub_super(Main):
  def __init__(self,*args):
    super().__init__(*args)

a1 = Main_super('parameter1','parameter2','parameter3')

a2 = Sub_super('parameter1','parameter2','parameter3','parameter4')

text1 = a1.args[2]

text2 = a2.args[3]

try:
  for i in range(5):
    print(a2.args[i])
except IndexError:
  print('Index Not Found:')


