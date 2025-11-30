user_input1 = input('Please type a number, or letter key, then press enter: ')
user_input2 = input('Please type second number, or letter key, then press enter: ')

class Input_text:

  def __init__(self,user_input1,user_input2):

    self.user_input1 = user_input1  # attribute1 property:

    self.user_input2 = user_input2  # attribute2 property:

  def return_user_input(self):
    return f'{self.user_input1} {self.user_input2}'

print(Input_text(user_input1,user_input2).user_input1)
print(Input_text(user_input1,user_input2).user_input2)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
user_input1 = input('Please type a number, or letter key, then press enter: ')
user_input2 = input('Please type second number, or letter key, then press enter: ')

class Input_text:

  def __init__(self,user_input1,user_input2):

    self.user_input1 = user_input1  # attribute1 property:

    self.user_input2 = user_input2  # attribute2 property:

  def return_user_input(self):
    return f'{self.user_input1}\n{self.user_input2}'

print(Input_text(user_input1,user_input2).return_user_input())
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
user_input1 = input('Please type a number, or letter key, then press enter: ')
user_input2 = input('Please type second number, or letter key, then press enter: ')

class Input_text:

  def __init__(self,user_input1,user_input2):

    self.user_input1 = user_input1  # attribute1 property:

    self.user_input2 = user_input2  # attribute2 property:

  def return_user_input(self):
    return f'{self.user_input1}\n{self.user_input2}'

print(Input_text(user_input1,user_input2).user_input1)
print(Input_text(user_input1,user_input2).user_input2)

print(Input_text(user_input1,user_input2).return_user_input())
