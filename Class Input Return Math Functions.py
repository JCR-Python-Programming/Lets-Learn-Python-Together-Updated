import math

class Math:

  def __init__(self,user_input1,user_input2):

    self.user_input1 = user_input1  # attribute1 property:

    self.user_input2 = user_input2  # attribute2 property:

  def return_addition(self):
    return  self.user_input1+self.user_input2

  def return_subtraction(self):
    return  self.user_input1-self.user_input2

  def return_multiplication(self):
    return  self.user_input1*self.user_input2

  def return_division(self):
    return  self.user_input1/self.user_input2

  def return_exponent(self):
    return  self.user_input1**self.user_input2

  def return_power(self):
    return  pow(self.user_input1,self.user_input2)

  def return_root(self):
    return  math.sqrt(self.user_input2)

class Great_work(Math):

  def __init__(self,user_input1,user_input2,user_input3):
    super().__init__(user_input1,user_input2)

    self.user_input3 = user_input3  # super attribute3 property:

  def return_super(self):
    return self.user_input3

message1 = 'Please type a number, the press enter: '
message2 = 'Please type a second number, then press enter: '

while True:

  try:
    user_input1 = int(input(message1).strip())
    user_input2 = int(input(message2).strip())
    break

  except ValueError:
    print('Numbers only please:')

print(Math(user_input1,user_input2).return_addition())
print(Math(user_input1,user_input2).return_subtraction())
print(Math(user_input1,user_input2).return_multiplication())
print(Math(user_input1,user_input2).return_division())
print(Math(user_input1,user_input2).return_exponent())
print(Math(user_input1,user_input2).return_power())
print(Math(user_input1,user_input2).return_root())

print(Great_work(user_input1,user_input2,'Great Work!!').user_input3)

print(Great_work(user_input1,user_input2,'Great Work!!').return_super())
