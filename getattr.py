class Main:
  def __init__(self,arg1,arg2):

    self.arg1 = arg1
    self.arg2 = arg2

  def class_datta(self):
    print(self.arg2)

  def __getattr__(self, arg1):
    return 'Attribute not found:'

Main('arg1','arg2').class_datta()
